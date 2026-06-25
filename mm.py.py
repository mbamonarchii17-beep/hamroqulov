import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="SportMax — Sport Do'koni",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu { visibility: hidden; }
    header[data-testid="stHeader"] { display: none; }
    footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0; }
    [data-testid="stVerticalBlock"] { gap: 0 !important; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

# index.html ni o'qib yuklash
html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    HTML_CONTENT = f.read()

components.html(HTML_CONTENT, height=6000, scrolling=False)
