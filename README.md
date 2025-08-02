# Deep Learning Translation API

A FastAPI-based translation service that uses the T5 (Text-To-Text Transfer Transformer) model to provide high-quality translations between multiple languages. The service supports asynchronous translation processing with background task execution to handle long-running translations efficiently.

## 🌟 Features

- **Multi-language Support**: Translate between English, French, German, and Romanian
- **Asynchronous Processing**: Background task execution for long translations
- **RESTful API**: Clean and intuitive API endpoints
- **Database Storage**: SQLite database for storing translation requests and results
- **Docker Support**: Easy deployment with Docker containerization
- **Azure Deployment**: Production-ready deployment on Microsoft Azure
- **Input Validation**: Robust validation for language codes and text input

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd langtranslator_dl
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn api_main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 🐳 Docker Deployment

### Build and run with Docker

```bash
# Build the Docker image
docker build -t langtranslator .

# Run the container
docker run -p 80:80 langtranslator
```

The API will be available at `http://localhost:80`

## ☁️ Azure Deployment

This application is deployed on Microsoft Azure for production use.

### Azure App Service Deployment

The application is configured to run on Azure App Service with the following setup:

- **Service Type**: Azure App Service (Web App)
- **Runtime**: Python 3.12
- **Deployment Method**: Docker container deployment
- **Scaling**: Auto-scaling enabled for high availability

## 📚 API Documentation

### Base URL
- Development: `http://localhost:8000`
- Docker: `http://localhost:80`
- Production: `https://your-app-name.azurewebsites.net`

### Endpoints

#### 1. Health Check
- **GET** `/`
- **Response**: `{"message": "Deep Learning Translator"}`

#### 2. Submit Translation Request
- **POST** `/translate`
- **Request Body**:
  ```json
  {
    "text": "Hello, how are you?",
    "initial_lang": "English",
    "final_lang": "French"
  }
  ```
- **Response**: `{"task id": 123}`

#### 3. Retrieve Translation Result
- **GET** `/results?translation_id=123`
- **Response**: `{"translation": "Bonjour, comment allez-vous?"}`

### Supported Languages
- English
- French
- German
- Romanian

## 🔧 Usage Examples

### Using curl

```bash
# Submit a translation request
curl -X POST "http://localhost:8000/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Good morning, everyone!",
    "initial_lang": "English",
    "final_lang": "German"
  }'

# Retrieve the translation result
curl "http://localhost:8000/results?translation_id=1"
```

### Using Python requests

```python
import requests

# Submit translation request
response = requests.post("http://localhost:8000/translate", json={
    "text": "Hello world",
    "initial_lang": "English",
    "final_lang": "French"
})
task_id = response.json()["task id"]

# Retrieve translation result
result = requests.get(f"http://localhost:8000/results?translation_id={task_id}")
translation = result.json()["translation"]
print(translation)
```

## 🏗️ Project Structure

```
langtranslator_dl/
├── api_main.py          # FastAPI application and routes
├── tasks.py             # Translation logic and background tasks
├── models.py            # Database models and configuration
├── requirements.txt     # Python dependencies
├── dockerfile          # Docker configuration
├── translations.db     # SQLite database
└── README.md          # This file
```

## 🔍 Technical Details

### Architecture
- **Framework**: FastAPI for high-performance API development
- **Database**: SQLite with Peewee ORM for data persistence
- **ML Model**: T5-small transformer model for translation
- **Background Tasks**: Asynchronous processing for long-running translations

### Database Schema
The `TranslationModel` table stores:
- `text`: Original text to translate
- `initial_lang`: Source language
- `final_lang`: Target language
- `translation`: Translated text (null while processing)

### Translation Process
1. Client submits translation request via POST `/translate`
2. Request is stored in database and task ID is returned immediately
3. Translation runs in background using T5 model
4. Client can poll GET `/results` to retrieve completed translation