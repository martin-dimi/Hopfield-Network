import numpy as np
from utilities import seven_segment

class Network(object):

    def __init__(self, neuron_amount, submission_service):
        self.submission_service = submission_service

        self.num_neurons = neuron_amount
        self.weights = np.zeros((self.num_neurons, self.num_neurons))
        self.threshold = 0

    # Heavysite Step Function
    def activation_function(self, x):
        if x > self.threshold:
            return 1
        else:
            return -1

    def learn(self, patterns):
        num_of_patterns = len(patterns)

        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i == j: continue

                activation_sum = 0
                for pattern in patterns:
                    activation_sum += pattern[i] * pattern[j]

                self.weights[i][j] = 1/num_of_patterns * activation_sum

    def predict(self, pattern):
        steps_taken = 0
        self.output_pattern(pattern)

        while True:
            new_pattern = self.weights @ pattern - self.threshold
            new_pattern = np.array([self.activation_function(x) for x in new_pattern])
            
            if np.array_equal(new_pattern, pattern):
                break

            pattern = new_pattern
            steps_taken += 1
            self.output_pattern(pattern)
        
        print(f"Convergence after {steps_taken} steps")
        return pattern

    def output_pattern(self, pattern):
        seven_segment(pattern)
        self.submission_service.seven_segment(pattern)


