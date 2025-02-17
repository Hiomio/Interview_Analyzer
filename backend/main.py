from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .processing import transcribe_audio, analyze_sentiment, extract_entities, analyze_with_gpt

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze_audio/")
async def analyze_audio(file: UploadFile = File(...)):
    """API to handle audio file and analyze interview response"""
    
    # Save file temporarily
    audio_path = f"temp_audio.wav"
    with open(audio_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Process audio
    transcript = transcribe_audio(audio_path)
    sentiment = analyze_sentiment(transcript)
    entities = extract_entities(transcript)
    gpt_analysis = analyze_with_gpt(transcript)

    return {
        "transcript": transcript,
        "sentiment": sentiment,
        "entities": entities,
        "gpt_analysis": gpt_analysis
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
