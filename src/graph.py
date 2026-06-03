from langgraph.graph import StateGraph, START, END
from src.state import GraphState
from src.nodes import tracker_node, architect_node

def build_graph():
    """
    Construye y compila el grafo de estado para el sistema de ideación.
    """
    # Inicializar el grafo con nuestro estado definido
    builder = StateGraph(GraphState)
    
    # Añadir los nodos al grafo
    builder.add_node("tracker", tracker_node)
    builder.add_node("architect", architect_node)
    
    # Definir el flujo (edges)
    builder.add_edge(START, "tracker")
    builder.add_edge("tracker", "architect")
    builder.add_edge("architect", END)
    
    # Compilar el grafo
    graph = builder.compile()
    
    return graph
