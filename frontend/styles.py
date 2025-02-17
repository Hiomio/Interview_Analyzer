import streamlit as st

def set_page_config():
    """Set Streamlit page configuration"""
    st.set_page_config(
        page_title="Automated Interview Analyzer",
        page_icon="🎤",
        layout="wide"
    )

def apply_custom_styles():
    """Apply CSS for a better UI"""
    st.markdown("""
        <style>
            .big-title { font-size: 30px; font-weight: bold; }
            .small-title { font-size: 20px; font-weight: bold; color: #ff4b4b; }
            .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; }
            .stAudio audio { width: 100% !important; }
        </style>
    """, unsafe_allow_html=True)
