# URL Shortener (FastAPI)

Simple asynchronous URL shortening service built with FastAPI.

---

## Requirements

- Python 3.12+
- pip

---

## Installation

```bash
# Create a virtual environment
python -m venv .venv
```

```bash
# Activate virtual environment
# Linux / macOS:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (cmd):
.venv\Scripts\activate.bat
```
# Install dependencies
pip install -r requirements.txt

# Run the server:

```bash
uvicorn app.main:app --reload
```
Server will be available at http://127.0.0.1:8000

API Usage
Create a shortened URL

POST /

Request body:
```json
{
  "url": "https://example.com/some/long/path"
}
```

Response (status 201):
```json
{
  "short_id": "abc123"
}
```

Redirect to original URL

GET /{short_id}

Redirects to the original URL (HTTP 307)

Returns 404 if short_id does not exist

Project Structure

url-shortener/
├── app/
│   ├── main.py              # FastAPI app and routes
│   ├── models.py            # Data models
│   ├── schemas.py           # Pydantic schemas
│   ├── services/            # Business logic
│   ├── storage/             # Storage implementation (in-memory)
│   └── utils/               # Utilities (ID generation)
├── tests/                   # Pytest tests
├── requirements.txt
├── README.md
└── .gitignore

Testing

# Run all tests
```bash
pytest -v
```

Tests cover URL creation, redirection, and 404 cases.

Make sure your virtual environment is active when running tests.
