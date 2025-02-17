import whisper
from .models import whisper_model, sentiment_model, ner_model, openai

def transcribe_audio(audio_path: str) -> str:
    """Convert speech to text using Whisper"""
    return whisper_model.transcribe(audio_path)["text"]

def analyze_sentiment(text: str):
    """Perform sentiment analysis"""
    return sentiment_model(text)

def extract_entities(text: str):
    """Extract keywords using Named Entity Recognition (NER)"""
    return ner_model(text)

def analyze_with_gpt(text: str):
    """Use GPT-4 for advanced interview analysis"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Analyze the interview response for clarity and depth."},
                  {"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"]
