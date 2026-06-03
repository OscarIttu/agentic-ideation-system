# 🤖 Agentic Ideation System (Sistema de Ideación con IA)

Una potente aplicación web construida con **Streamlit**, **LangGraph** y los modelos **Gemini 2.5** de Google que actúa como un investigador y arquitecto de software automatizado.

El sistema orquesta dos agentes de IA especializados para descubrir las herramientas más novedosas lanzadas en la última semana y generar automáticamente ideas de proyectos técnicos basadas en ellas.

---

## ✨ Características Principales

1. **Rastreador de Vanguardia (`gemini-2.5-flash`)**
   - Utiliza la API de Tavily para buscar las noticias más recientes (últimos 7 días).
   - Localiza **exactamente 10 herramientas de IA** (incluyendo gigantes tecnológicos, startups y repositorios open-source de GitHub).
   - Proporciona el nombre de la herramienta, para qué sirve, sus casos de uso y su URL oficial.

2. **Arquitecto de Software (`gemini-2.5-pro`)**
   - Toma el informe del Rastreador y diseña **6 ideas de proyectos técnicos**.
   - Clasifica los proyectos por dificultad: 2 Fáciles, 2 Medios y 2 Difíciles.
   - Detalla el propósito, la arquitectura técnica de implementación y una estimación de costes para cada idea.

3. **Interfaz Web Interactiva**
   - Totalmente funcional mediante Streamlit.
   - Indicadores visuales de estado que muestran qué agente está trabajando.
   - Presentación clara y estructurada en formato Markdown.

---

## 🛠️ Arquitectura Técnica

- **Framework de Orquestación:** [LangGraph](https://python.langchain.com/docs/langgraph)
- **Interfaz de Usuario:** [Streamlit](https://streamlit.io/)
- **Modelos de IA:** Google GenAI (`gemini-2.5-flash` y `gemini-2.5-pro`)
- **Motor de Búsqueda Web:** [Tavily Search API](https://tavily.com/)

---

## 🚀 Guía de Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/agentic-ideation-system.git
cd agentic-ideation-system
```

### 2. Crear y activar un entorno virtual
Se recomienda el uso de un entorno virtual para aislar las dependencias.
**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
**En macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno (Claves API)
El proyecto utiliza un archivo oculto `.env` para proteger tus claves API. **Este archivo está configurado en el `.gitignore` para que NUNCA se suba a GitHub por accidente.**

1. Renombra el archivo `.env.example` a `.env`.
2. Edita el archivo `.env` y añade tus claves reales:
```env
GOOGLE_API_KEY=tu_clave_de_google_ai_studio_aqui
TAVILY_API_KEY=tu_clave_de_tavily_aqui
```
*(Puedes obtener las claves gratuitamente en [Google AI Studio](https://aistudio.google.com/app/apikey) y en [Tavily](https://app.tavily.com/))*

---

## 💻 Uso

Para ejecutar la aplicación web, asegúrate de tener el entorno virtual activado y ejecuta:

```bash
streamlit run app.py
```

Esto abrirá automáticamente una pestaña en tu navegador web. Simplemente haz clic en el botón **"🚀 Iniciar Búsqueda e Ideación"** y observa cómo los agentes hacen el trabajo por ti.

---

## 📝 Estructura del Código

- `app.py`: Archivo principal e interfaz gráfica de Streamlit.
- `src/graph.py`: Definición y compilación del grafo de LangGraph.
- `src/nodes.py`: Lógica principal y "prompts" de los agentes (Rastreador y Arquitecto).
- `src/state.py`: Definición del estado compartido (memoria) entre los agentes.
- `requirements.txt`: Lista de librerías Python necesarias.
