FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Download and cache the model during build
RUN python -c "from transformers import pipeline; pipeline('translation', model='mmuniversity/rutooro-multilingual-translator')"

# Expose the port the app runs on
EXPOSE 5000

# Use gunicorn as the production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 