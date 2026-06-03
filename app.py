import os
import streamlit as st
from dotenv import load_dotenv
from src.graph import build_graph

# Cargar variables de entorno
load_dotenv()

st.set_page_config(page_title="Ideación IA", page_icon="🤖", layout="wide")

st.title("🤖 Sistema de Ideación de Proyectos IA")
st.markdown("Este sistema utiliza **Gemini 2.5** y **Tavily** para rastrear las herramientas de IA más novedosas de los últimos 7 días (Google, ChatGPT, open-source de GitHub, startups, etc.) y generar automáticamente 6 proyectos técnicos escalados por dificultad.")

# Verificación de claves
if not os.getenv("GOOGLE_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    st.error("Faltan claves API. Asegúrate de tener GOOGLE_API_KEY y TAVILY_API_KEY configuradas correctamente en tu archivo .env.")
else:
    if st.button("🚀 Iniciar Búsqueda e Ideación", type="primary", use_container_width=True):
        
        # Construir el grafo
        graph = build_graph()
        initial_state = {}
        
        # Contenedores visuales para mostrar resultados
        tracker_placeholder = st.empty()
        architect_placeholder = st.empty()
        
        # Indicador de estado
        with st.status("🔍 Rastreador web buscando 10 herramientas de los últimos 7 días...", expanded=True) as status:
            try:
                # Ejecutar el grafo de LangGraph evento a evento
                for event in graph.stream(initial_state):
                    if "tracker" in event:
                        status.update(label="✅ Herramientas encontradas. El Arquitecto está diseñando los proyectos...", state="running")
                        
                        # Mostrar los resultados del rastreador en la UI
                        with tracker_placeholder.container():
                            st.subheader("🛠️ Las 10 Nuevas Herramientas (Últimos 7 días)")
                            st.markdown(event["tracker"]["news"])
                            st.divider()
                            
                    elif "architect" in event:
                        status.update(label="✅ ¡Proceso completado con éxito!", state="complete", expanded=False)
                        
                        # Mostrar los resultados del arquitecto en la UI
                        with architect_placeholder.container():
                            st.subheader("🏗️ 6 Ideas de Proyectos Técnicos")
                            st.markdown(event["architect"]["project_ideas"])
                            
            except Exception as e:
                status.update(label="❌ Error durante la ejecución", state="error")
                st.error(f"Se ha producido un error: {str(e)}")
