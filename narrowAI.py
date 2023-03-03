import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

#creo un dizionario di parole
lemmatizer = WordNetLemmatizer()
#leggo gli intenti
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
#caratteri ignorati per incrementare la precisione
ignore_letters = ["?", "!", ".", ","]

#per ogni intento
for intent in intents['intents']:
    #per ogni domanda dell'intento
    for pattern in intent['patterns']:
        #divido la frase in parole
        word_list = nltk.word_tokenize(pattern)
        #aggiungo alle parole la frase tokenizzata
        words.extend(word_list)
        #aggiungo ai documenti la tupla (parole e relativo argomento)
        documents.append((word_list, intent['tag']))
        #salvo la classe se non esiste
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
#pulisco ogni parola-> forma base della parola + ignoro alcune lettere
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
#ordine alfabetico
words = sorted(set(words))
classes = sorted(set(classes))
#pickle -> compresso, leggibile e calcolabile in memoria senza ricalcoli e ricostruzioni
#salvo i dati nei file .pkl
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))
#
# PARTE DI ALLENAMENTO
#
training = []
output_empty = [0] * len(classes)
#per ogni intent(document)
for document in documents:
    #bag contiene 1 se la parola è presente nel pattern, altrimenti 0
    bag = []
    #scorro la prima domanda
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    #output row contiene tanti zeri quanto il numero di classi
    output_row = list(output_empty)
    #prendo la classe appartenente e la setto ad 1
    output_row[classes.index(document[1])] = 1
    #aggiorno il training
    training.append([bag, output_row])
#evito che il modello memorizzi l'ordine e impari a rispondere solo in un ordine
random.shuffle(training)
#matrice di 0 e 1
#ogni riga una frase di input
#ogni colonna una di output(1 presente 0 assente)
train_x = np.asarray([i[0] for i in training])
#contiene l'etichetta di output del pattern di input
#ogni riga una frase di input e ogni colonna una classe di output(1 presente 0 assente)
train_y = np.asarray([i[1] for i in training])

#Neural Network
#Dense Layers->strati

model = Sequential()
#128 è il numero di neuroni dello strato
#Relu restituisce il valore se l'input è positivo
#input shape è la dimensione dell'input
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
#Dropout serve per evitare l'overfitting
model.add(Dropout(0.5))
#secondo layer con meno neuroni per generalizzare
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
#softmax converte il vettore di output in un vettore di probabilità relativa di ogni classe
model.add(Dense(len(train_y[0]), activation='softmax'))
#learning_rate -> quanto cambia il peso ad ogni iterazione
#momentum -> accelerazione di aggiornamento dei pesi. Si usa per ottimizzare il cambio dei pesi in base alle iterazioni precendenti.
#nesterov -> cerca di prevedere dove sara il gradiente all'iterazione sucessiva per aumentare l'accuratezza
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
#loss -> funzione di perdita. In questo caso si usa una funzione per la categorizzazione
#optimizer -> ottimizzatore utilizzato
#valuto in base all'accuratezza
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
#addestro il modello
#le epoche sono il numero di volte che addestro il modello
#il batch_size dice su quanti campioni viene addestrata una batch prima di cambiare il peso
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.model', hist)
print("Done")
