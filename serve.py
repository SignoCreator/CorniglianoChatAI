import os

from flask import Flask, request
from flask_cors import CORS
from chat import chat

app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def getResponse():
    data = request.form["message"]
    return chat(data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=os.environ.get('FLASK_DEBUG') == '1', host='0.0.0.0', port=port)

