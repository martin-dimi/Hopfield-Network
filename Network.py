import numpy as np

class Network(object):

    def __init__(self, neurons):
        self.num_neurons = neurons
        self.num_synapses = neurons * neurons - neurons

        self.weights = np.zeros((self.num_neuron, self.num_neuron))
        self.threshold = 0

    # Heavysite Step Function
    def activation_function(self, x):
        if x > self.threshold:
            return 1
        else:
            return -1

    def learn(self, patterns):

        num_of_patterns = len(patterns)

        


