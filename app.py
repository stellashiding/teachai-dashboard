import streamlit as st
import plotly.graph_objects as go
import json
from evaluate import evaluate_response

st.set_page_config(page_title="TEACH-AI Dashboard", page_icon="🧠", layout="centered")

st.title("TEACH-AI BenchmarkDashboard (Prototype)")
st.write("""
Evaluate generative AI tutors across 10 educational dimensions using the TEACH-AI benchmark.
This prototype applies the **LLM-as-Judge** method to automatically generate scores.
""")

model_name = st.selectbox("Select Model", ["GPT-4", "Claude-3", "Gemini-1.5"])
response_text = st.text_area("Paste AI Tutor Response:", height=180)

if st.button("Evaluate"):
    with st.spinner("Evaluating with TEACH-AI Benchmark..."):
        scores = evaluate_response(response_text)
        st.success("Evaluation complete!")
        st.json(scores)

        labels = list(scores.keys())
        values = list(scores.values())
        fig = go.Figure(data=go.Scatterpolar(
            r=values + [values[0]],
            theta=labels + [labels[0]],
            fill="toself",
            name=model_name
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0,5])),
            showlegend=False,
            title="TEACH-AI Evaluation Profile"
        )
        st.plotly_chart(fig)
