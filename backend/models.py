import whisper
from transformers import pipeline
import openai

# Load Whisper Model (use "small" for lightweight processing)
whisper_model = whisper.load_model("base")

# Load NLP Models
sentiment_model = pipeline("sentiment-analysis")
ner_model = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# OpenAI API Key (Use environment variable for security)
openai.api_key = "YOUR_OPENAI_API_KEY"
