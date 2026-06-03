from typing import TypedDict, Annotated, List

class GraphState(TypedDict):
    """
    Representa el estado del grafo de agentes.
    
    Atributos:
        topic: El tema inicial de búsqueda proporcionado por el usuario.
        news: Las noticias/tendencias y herramientas recopiladas por el rastreador.
        project_ideas: El documento Markdown generado por el arquitecto con las ideas de proyecto.
    """
    news: str
    project_ideas: str
