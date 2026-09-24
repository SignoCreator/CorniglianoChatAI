FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && python -m nltk.downloader -d /usr/local/share/nltk_data punkt_tab wordnet

COPY . .

EXPOSE 5000
CMD ["python", "serve.py"]
