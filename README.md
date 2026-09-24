# CorniglianoChatAI

An Italian-language FAQ chatbot for **CorniglianoCoin**, a loyalty app built by students of the Calvino technical high school in Genoa (Sestri Ponente) to support small food shops in the Cornigliano district. Customers earn points ("cornicoin") when they shop and redeem them for prizes; the chatbot answers their questions about points, prizes, shops and accounts.

Built in 2023 as a school team project by **Diego Signorastri** and **Stefano Calderaro** ([@Steficalde](https://github.com/Steficalde)).

## How it works

The bot is an intent classifier: every question is mapped to one of 48 topics ("intents"), and the bot replies with one of that topic's answers.

```
question ──► tokenize + lemmatize (NLTK) ──► bag-of-words vector ──► neural network ──► intent ──► random answer
```

- **Data:** [`intents.json`](intents.json) holds 48 intents, each with example questions (`patterns`) and answers (`responses`), written by hand for the app.
- **Model:** a Keras feed-forward network — Dense 1024 (ReLU) → Dropout 0.5 → Dense 512 (ReLU) → Dropout 0.5 → softmax over the intents. Trained with SGD (learning rate 0.01, momentum 0.9, Nesterov) for 200 epochs.
- **Fallback:** if no intent scores above 0.5, the bot says it can't answer and suggests contacting the team.
- **API:** a small Flask server exposes the bot at `POST /chat`.

| File | Purpose |
| --- | --- |
| `narrowAI.py` | Builds the vocabulary and trains the model |
| `chat.py` | Loads the model and answers a question |
| `serve.py` | Flask API used by the mobile app |

## Run it

With Python 3.9–3.11:

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python serve.py            # add FLASK_DEBUG=1 for debug mode
```

Or with Docker:

```bash
docker compose up --build  # API on http://localhost:5001
```

Ask a question:

```bash
curl -X POST http://localhost:5000/chat -d "message=come guadagno punti?"
# Per guadagnare cornicoin recati in un negozio associato e esegui un acquisto
```

To retrain after editing `intents.json`, run `python narrowAI.py`.

## What I'd do differently today

- NLTK's WordNet lemmatizer only knows English, so Italian words are mostly left as they are; an Italian model (e.g. spaCy `it_core_news_sm`) would generalize better.
- Bag-of-words ignores word order and synonyms; sentence embeddings or a small fine-tuned transformer would handle rephrased questions far better.
- The network is much larger than 48 intents need — a smaller model would train faster with the same accuracy.
