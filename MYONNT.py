#Make your own neural network tutorial

import numpy as np

# neural network class definition
class neuralNetwork: 
    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    # set the number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes 
        self.onodes = outputnodes 
    # learning rate
        self.lr = learningrate 
        pass
    
    # train the neural network
    def train(): pass 
    
    # query the neural network
    def query(): pass 
    