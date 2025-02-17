import streamlit as st
import requests
from styles import set_page_config, apply_custom_styles

# Configure Streamlit
set_page_config()
apply_custom_styles()

st.markdown('<p class="big-title">Automated Interview Analyzer 🎤</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload an interview audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Analyze Interview"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/analyze_audio/", files=files)

        if response.status_code == 200:
            result = response.json()

            st.markdown('<p class="small-title">Transcript</p>', unsafe_allow_html=True)
            st.write(result["transcript"])

            st.markdown('<p class="small-title">Sentiment Analysis</p>', unsafe_allow_html=True)
            st.json(result["sentiment"])

            st.markdown('<p class="small-title">Named Entities</p>', unsafe_allow_html=True)
            st.json(result["entities"])

            st.markdown('<p class="small-title">GPT-4 Analysis</p>', unsafe_allow_html=True)
            st.write(result["gpt_analysis"])
        else:
            st.error("Error processing the file. Please try again.")
