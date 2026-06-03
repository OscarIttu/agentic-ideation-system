from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from src.state import GraphState

def tracker_node(state: GraphState):
    """
    Nodo Rastreador: Busca últimas tendencias y herramientas de IA sobre el tema.
    Utiliza Tavily Search API y Gemini 1.5 Flash.
    """
    # Configurar la herramienta de búsqueda de Tavily
    # Se espera que TAVILY_API_KEY esté en el entorno
    search = TavilySearchResults(max_results=5)
    
    # Consultas para cumplir con el requerimiento del usuario (última semana)
    query_tools_1 = "Lanzamientos de nuevas herramientas de Inteligencia Artificial en los últimos 7 días (Google, OpenAI, Claude, startups)"
    query_tools_2 = "New AI tools open source github trending releases last 7 days"
    
    try:
        # Ejecutar búsquedas
        results_1 = search.invoke({"query": query_tools_1})
        results_2 = search.invoke({"query": query_tools_2})
        
        raw_info = f"--- Búsqueda 1 ---\n{results_1}\n\n--- Búsqueda 2 ---\n{results_2}"
    except Exception as e:
        raw_info = f"Error al buscar en Tavily: {e}"

    # Utilizar Gemini 2.5 Flash para procesar y estructurar la información encontrada
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    
    prompt = f"""
    Eres un experto analista tecnológico y rastreador de información.
    
    He realizado búsquedas en la web usando Tavily API sobre lanzamientos de nuevas herramientas de IA en los últimos 7 días y obtuve los siguientes resultados en bruto:
    
    {raw_info}
    
    Tu única tarea es redactar un listado de EXACTAMENTE 10 herramientas novedosas de IA que hayan salido o se hayan actualizado de forma importante en la última semana. 
    Debes incluir de todo: gigantes tecnológicos (Google, OpenAI, Anthropic, Cloud providers), startups llamativas y funcionalidades open-source llamativas de GitHub.
    
    Para cada herramienta, incluye obligatoriamente:
    1. El nombre de la herramienta.
    2. Enlace o URL de donde se ha sacado la información (búscalo en los resultados en bruto).
    3. Una descripción clara de para qué sirve.
    4. Para qué tipo de casos de uso o proyectos se va a implementar.
    
    Haz un listado claro en formato Markdown.
    """
    
    response = llm.invoke(prompt)
    
    return {"news": response.content}

def architect_node(state: GraphState):
    """
    Nodo Arquitecto: Genera ideas de proyectos basados en las noticias.
    Utiliza Gemini 1.5 Pro.
    """
    news = state["news"]
    
    # Utilizar Gemini 2.5 Pro para la ideación profunda
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)
    
    prompt = f"""
    Eres un Arquitecto de Software Senior y Visionario de IA.
    
    El agente Rastreador ha recopilado el siguiente informe con 10 nuevas herramientas de IA lanzadas en los últimos 7 días:
    
    {news}
    
    Tu tarea es diseñar exactamente 6 ideas de proyectos técnicos (2 nivel fácil, 2 nivel medio, y 2 nivel difícil) implementando o basándose en las nuevas herramientas recopiladas en este informe.
    
    Debes devolver la respuesta en formato Markdown estricto. 
    Para cada uno de los 6 proyectos debes incluir estas secciones obligatoriamente:
    
    ### Proyecto [Número] - Nivel [Fácil/Medio/Difícil]: [Nombre del Proyecto]
    - **Propósito**: ¿Qué problema concreto resuelve aprovechando las nuevas herramientas mencionadas y por qué es relevante ahora mismo?
    - **Implementación**: Describe la arquitectura técnica, los componentes principales, el flujo de datos y qué herramientas específicas de IA del informe vas a utilizar.
    - **Costes**: Haz una estimación estructurada de los costes asociados (infraestructura en la nube, consumo de APIs de IA, tiempo de desarrollo esperado).
    """
    
    response = llm.invoke(prompt)
    
    return {"project_ideas": response.content}
