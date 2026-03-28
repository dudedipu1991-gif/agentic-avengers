import os
import streamlit as st
from core.orchestration import MarketResearchWorkflow

st.write("DEBUG: starting app")
st.write("DEBUG: GROQ_MODEL =", os.getenv("GROQ_MODEL"))
st.write("DEBUG: GROQ_API_KEY set =", bool(os.getenv("GROQ_API_KEY")))

from core.orchestration import MarketResearchWorkflow

with st.sidebar:
    st.header("Settings")
    use_competitor = st.checkbox("Include competitor analysis", value=True)
    model_name = st.text_input(
        "GROQ model",
        value=os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile"),
    )
    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        float(os.getenv("GROQ_TEMPERATURE", "0.2")),
        0.05,
    )

    os.environ["GROQ_MODEL"] = model_name
    os.environ["GROQ_TEMPERATURE"] = str(temperature)