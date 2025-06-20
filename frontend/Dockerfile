# Use the official Streamlit image
FROM python:3.11-slim


# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all files
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
