FROM python:3.11-slim

# Set up working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project
COPY . .

# Expose the port Cloud Run uses
EXPOSE 8000

# Start the FastAPI app (points to the inner main.py)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0"]
