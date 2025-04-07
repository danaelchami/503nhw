from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from langdetect import detect, LangDetectException
import logging

app = FastAPI()

# Load model from Hugging Face
model_name = "tabularisai/multilingual-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

class TextInput(BaseModel):
    text: str


@app.post("/analyze")
def analyze_sentiment(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty.")
    
    result = sentiment_pipeline(input.text)
    return {"input": input.text, "result": result}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/language-detect")
def detect_language(input: TextInput):
    try:
        if not input.text or len(input.text.strip()) < 5:
            raise ValueError("Text is too short to detect language.")

        language = detect(input.text)
        logging.info(f"Detected language: {language} for text: {input.text}")
        return {"input": input.text, "language": language}

    except LangDetectException:
        logging.error("LangDetectException: Could not detect language.")
        raise HTTPException(status_code=400, detail="Could not detect language. Try a longer or clearer sentence.")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")