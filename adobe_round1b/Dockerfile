FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

# Install system dependencies for PyMuPDF
RUN apt-get update && \
    apt-get install -y libglib2.0-0 libgl1-mesa-glx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]
