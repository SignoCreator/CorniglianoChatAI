###### by Diego Signorastri & Stefano Calderaro
# CHAT AI 


## what is it

This is an AI able to assist clients anwering their question about app.
It thinks what's the better answer to the client question thanks to its
neural network trained with data.

---

---

## - For Advanced developers and Stefano

## how it works

### Data

It's important to write a good answers-responses file with a correct logic.  
Each answer and response is stored in a tag( like an argument).
Each answer can have more responses.
The perfect intent is structured like this:\
`
   {
      "tag":"saluti",
      "patterns":["ciao","buongiorno"], 
      "responses": ["ciao!","hey"]
   },`

#### Tokenization and Lemmatization

Every single phrase on input and on the database will be tokenized, that means
that phrases will be divided in words.  
Every single word will be lemmatized, that means that the word will be processed and reduced to its canonical form.
With the lemmatization is common to also remove the forbidden characters.

Code : 
- Implement a lemmatizer :  
`from nltk.stem import WordNetLemmatizer`


- Create a lemmatizer :  
`lemmatizer = WordNetLemmatizer()`


- Lemmatize a word :  
`lemmatizer.lemmatize(word)`
---
### Training

This is a crucial part of the code, because it is responsible for output.
we have to save the data by separating the data into input and output.

We have to store into an array named words every word in answers of intents.(row 25-45)
After we can prepare the training array, containing train_x(input) and train_y(output).  
Per ogni intent creo uno zaino contenente 0 o 1 in base a se contiene o no una parola.  
We save also the class that contains it.
---
### Neural Network

It works thanks to a neural network that processes an input phrase and gets\
the best response based on its database.
This neural network has been created using the tensorFlow python library.



We've divided that in 3 layers:

- Input layer &rarr; 128 neurons, **Re**ctified **L**inear **U**nit function as activator
- hidden layer &rarr; 64 neurons, **Re**ctified **L**inear **U**nit function as activator\
we have choosen to reduce neurons number to **generalize** the input
- Output layer &rarr; as many neurons as the number of type of questions, it activated by softMax function(probability function converter)

---

### Stochastic gradient descend(SGD)

This is an iterative method for otimizing an objective function.
It is a stochastic approximation of gradient descend, that is a tecnique
used to estimate the value of a function. It is used when is difficult
to calculate the exact result of a problem and that's 
enough to approximate the solution using stochastic approximation.
SGD is an algorithm of iterative optimization  for finding a local best output.

Code :

-implement **SGD**  
`from tensorflow.keras.optimizers import SGD`  

-create **SGD**  
`SGD(learning_rate=0.01, momentum=0.9, nesterov=True)`  
#### Settings

we've set SGD with these params:

- learning rate &rarr; 0.01, this param says how much the weight of neuron changes at each iteration
- momentum &rarr; 0.9, it says the acceleration of weights. It used to optimize the change of weights basing on preview iterations
- nesterov &rarr; True, this is a predictive tecnique used to prevent where will be the gradient descend at the next iteration. It increases the accuracy

---




 