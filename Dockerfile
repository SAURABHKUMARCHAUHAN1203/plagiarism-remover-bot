FROM python:3.9-slim

WORKDIR /app
COPY . .

# Install lightweight PyTorch + dependencies
RUN pip install --no-cache-dir \
    python-telegram-bot==13.7 \
    transformers==4.30.0 \
    torch==1.13.1+cpu --index-url https://download.pytorch.org/whl/cpu \
    sentencepiece==0.1.99 \
    openai==0.27.8 \
    language-tool-python==2.7 \
    gunicorn==20.1.0

CMD gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 bot:main
