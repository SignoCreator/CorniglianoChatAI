from flask import Flask, request
from flask_cors import CORS
from chat import chat

app = Flask(__name__)
CORS(app)


@app.route('/chat/<message>', methods=['GET'])
def getResponse(message):
    return chat(message)

if __name__ == "__main__":
    app.run()
