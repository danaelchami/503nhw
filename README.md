# 503nhw
This is a sentiment analysis API built using FastAPI and a pre-trained Hugging Face model. It was built as part of an assignment involving deploying AI models as API services and gaining experience with collaborative version control using GitHub.

The API accepts a string of text and returns a sentiment classification result (positive, negative, or neutral) and a confidence score. The service is exposed via RESTful endpoints and includes additional features such as input validation,language detection, and a health check endpoint.


(Optional) Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate      # Windows
source venv/bin/activate     # Mac/Linux
```


### `POST /language-detect`
Detects the language of the provided text.  
**Request:**
```json
{ "text": "Bonjour tout le monde" }
```
**Response:**
```json
{
  "input": "Bonjour tout le monde",
  "language": "fr"
}
```

---

### `GET /health`
Simple health check to verify the API is live.  
**Response:**
```json
{ "status": "ok", "message": "API is running smoothly." }
```

---

## 🧠 Features

- ✅ Sentiment analysis with Hugging Face Transformers
- 🌍 Language detection using `langdetect`
- ❤️ Health check endpoint
- 🧪 Input validation for better reliability
- 📝 Logging of inputs and predictions to `app.log`
- 🔀 Fully RESTful API with interactive Swagger docs

---

## 📌 Versioning & Changelog

### v1.0
- Initial implementation of sentiment analysis API using FastAPI and Hugging Face

### v1.1
- Added `/health` check endpoint
- Added input validation against empty strings
- Added `test_data.py` with sample inputs

### v1.2
- Added `/language-detect` endpoint using `langdetect`
- Added logging and robust exception handling

All updates are tracked via GitHub commits and pull requests for full transparency.

---

## 🤝 Collaboration Workflow

This project was developed collaboratively through GitHub:

- Developers created and worked on **feature branches**
- Each branch was merged via **pull requests**
- Code reviews and comments were used to improve quality
- Full version history is visible through GitHub commits and PRs

---

## 📁 Project Files

| File             | Description |
|------------------|-------------|
| `main.py`        | Main FastAPI app with all route definitions |
| `requirements.txt` | Lists all dependencies |
| `README.md`      | Documentation (this file) |
| `test_data.py`   | Sample input cases for testing |
| `app.log`        | Logs of predictions and system status |

How to Run:

Install dependencies by running: pip install -r requirements.txt

Run the API server with: uvicorn main:app --reload

Open a browser and navigate to: http://127.0.0.1:8000/docs
This will open the interactive Swagger UI where you can experiment with the endpoints.

Available Endpoints:

POST /analyze
Accepts a JSON body with text. Example request:
{ "text": "I love this project!" }
Returns the sentiment classification and confidence score.

GET /health
Returns a plain status message to verify the API is running. Example response:
{ "status": "ok" }

POST /language-detect
Detects the language of the provided text.  
{ "text": "Bonjour tout le monde" }
Returns the language of the input.

Versioning:

v1.0 - Initial implementation of sentiment analysis API using FastAPI and Hugging Face
v1.1 - Added health check endpoint, input validation against empty strings, and test_data.py with sample inputs
v1.2 - Added /language-detect endpoint using langdetect with logging and robust exception handling

All updates are tracked via GitHub commits and pull requests for full transparency.

Collaboration:

This project was developed collaboratively through GitHub. Each developer worked on their own branches, pushed commits with good commit messages, and created pull requests for code review and merging. It was all versioned and tracked through commits and pull requests following standard Git workflow and best practices.

Project Files:

main.py - Defines API routes and logic
model.py - Imports the sentiment analysis model
test_data.py - Contains test cases for development and verification
requirements.txt - All Python packages required
README.md - Documentation and how to install
.gitignore -Informs Git which files or folders to ignore