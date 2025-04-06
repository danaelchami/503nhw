from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

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
