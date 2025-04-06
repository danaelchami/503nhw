from fastapi import FastAPI
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
    result = sentiment_pipeline(input.text)
    return {"input": input.text, "result": result}
