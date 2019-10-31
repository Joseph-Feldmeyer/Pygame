'''
2-SnakeAI-NN.py
~~~
Defind the NN to be used for 2-SnakeAI.py. 

Draft: 
- class NN 
-- def init 
-- def ??? 

'''


# Import libraries
import random
import numpy as np


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [ np.random.randn(y,1) for y in sizes[1:] ]
        self.weights = [ np.random.randn(y,x)
                         for x, y in zip(sizes[:-1], sizes[1:]) ]

    def feedforward(self, inputs):
        """ Return the output of the NN if the input is 'inputs' """
        for b, w in zip(self.biases, self.weights):
            inputs = sigmoid(np.dot(w, inputs) + b)
        return inputs

def sigmoid(z):
    
