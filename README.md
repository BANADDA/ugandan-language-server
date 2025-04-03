# Rutooro Multilingual Translation Server

A Python-based API server for translating text from English to East African languages (Rutooro, Luganda, Acholi, and Runyankore) using the Hugging Face `mmuniversity/rutooro-multilingual-translator` model.

## Features

- Translate English text to Rutooro, Luganda, Acholi, or Runyankore
- Individual text translation endpoint
- Batch translation capabilities
- Dockerized for easy deployment

## Getting Started

### Prerequisites

- Python 3.9+
- pip
- Docker (optional)

### Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd rutooro-server
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the server:
   ```
   python app.py
   ```

The server will be available at `http://localhost:5000`.

### Using Docker

1. Build the Docker image:
   ```
   docker build -t rutooro-translator .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 rutooro-translator
   ```

## API Usage

### Health Check

```
GET /health
```

Returns:
```json
{
  "status": "healthy"
}
```

### Translate a Single Text

```
POST /translate
```

Request body:
```json
{
  "text": "Education is important for community development.",
  "language": "rutooro"
}
```

Supported languages: `rutooro`, `luganda`, `acholi`, `runyankore`

Response:
```json
{
  "original_text": "Education is important for community development.",
  "translated_text": "Okusoma nikwomuhendo ahabw'okukulaakulana.",
  "target_language": "rutooro"
}
```

### Batch Translation

```
POST /translate/batch
```

Request body:
```json
{
  "texts": [
    "Education is important for community development.",
    "Mobile phones have transformed communication in rural areas."
  ],
  "language": "rutooro"
}
```

Response:
```json
{
  "translations": [
    {
      "original_text": "Education is important for community development.",
      "translated_text": "Okusoma nikwomuhendo ahabw'okukulaakulana."
    },
    {
      "original_text": "Mobile phones have transformed communication in rural areas.",
      "translated_text": "Esimu zabyemikono zihindwireho enkoragana omubicweka byakyaro."
    }
  ],
  "target_language": "rutooro"
}
```

## Model Information

This server uses the `mmuniversity/rutooro-multilingual-translator` model from Hugging Face, which is a fine-tuned version of Helsinki-NLP/opus-mt-en-mul that specializes in translating from English to Rutooro and other East African languages.

## License

MIT License 