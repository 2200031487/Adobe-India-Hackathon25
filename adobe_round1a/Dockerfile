FROM python:3.10-slim

WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY app /app

CMD ["python", "main.py"]
