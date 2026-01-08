FROM python:3.14-slim

# Create workdir
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY . /app

# Default command runs tests
CMD ["python", "auto_test.py"]
