# Dockerfile for Python 3.14 environment with all dependencies
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Copy project files
COPY app/ ./app/
COPY tests/ ./tests/

# Set default command
CMD ["python", "-m", "pytest", "tests/", "-v"]
