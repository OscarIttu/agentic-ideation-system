import os
from dotenv import load_dotenv
from src.graph import build_graph

def main():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()
    
    # Verificar que las claves necesarias estén configuradas
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: Falta GOOGLE_API_KEY en el entorno o archivo .env")
        return
    if not os.getenv("TAVILY_API_KEY"):
        print("Error: Falta TAVILY_API_KEY en el entorno o archivo .env")
        return
    
    print("🤖 Bienvenido al Sistema de Ideación de Proyectos IA (Rastreador + Arquitecto)")
    print("-" * 75)
    print("\n🔍 Iniciando el Rastreador para buscar tendencias y herramientas de las últimas 24 horas...")
    
    # Construir el grafo
    graph = build_graph()
    
    # Estado inicial (sin topic)
    initial_state = {}
    
    # Ejecutar el grafo
    # stream nos permite ver los resultados a medida que los nodos finalizan
    for event in graph.stream(initial_state):
        if "tracker" in event:
            print("\n✅ Rastreador finalizado. Resumen de noticias y herramientas encontrado:")
            print("-" * 50)
            print(event["tracker"]["news"])
            print("-" * 50)
            print("\n🏗️  Iniciando el Arquitecto para generar ideas de proyectos...")
            
        elif "architect" in event:
            print("\n✅ Arquitecto finalizado. Aquí están tus ideas de proyectos:")
            print("=" * 75)
            print(event["architect"]["project_ideas"])
            print("=" * 75)

if __name__ == "__main__":
    main()
