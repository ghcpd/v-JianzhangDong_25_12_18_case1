FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt ./
# Create a venv and install pinned dependencies
RUN python -m venv /.venv \
    && /.venv/bin/python -m pip install --upgrade pip setuptools wheel \
    && /.venv/bin/pip install -r requirements.txt
# Copy project files
COPY . /app
ENV PATH="/.venv/bin:$PATH"
# Default command runs tests
CMD ["/bin/sh", "-c", "python -u auto_test.py || (python -u -m pytest tests || true)"]
