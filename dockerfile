# start by pulling the python image
FROM python:3.9-slim-buster



# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
# copy every content from the local file to the image
COPY .. /app
# switch working directory
WORKDIR /app

RUN python3 -m venv venv
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install nltk
RUN pip install tensorflow

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["serve.py" ]