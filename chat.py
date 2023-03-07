import random
import json
import pickle
import numpy as np
import re
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.model')


# pulisco le frasi
def clean_up_sentence(sentence):
    sentence = sentence.lower()
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    # bag of words
    bow = bag_of_words(sentence)
    # predizione
    res = model.predict(np.array([bow]))[0]
    # soglia per cui non prendo le classi
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # ordino in base alla probabilità
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    # creo un dizionario in cui ogni elemento ha la sua classe e la probabilità
    for r in results:
        return_list.append({'intent': classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    # prendo il tag con maggiore probabilità
    tag = intents_list[0]['intent']
    # prendo gli intenti
    list_of_intents = intents_json['intents']
    # prendo una risposta a caso di quell'argomento
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


#while True:
 #   message = input("<tu>")

  #  ints = predict_class(message)
 #   if len(ints) != 0:
 #       res = get_response(ints, intents)
 #   else:
 #       res = "sono stupida"
 #   print(res)


def chat(message):
    ints = predict_class(message)
    if len(ints) != 0:
        res = get_response(ints, intents)
    else:
        res = "sonon stupida"
    return res