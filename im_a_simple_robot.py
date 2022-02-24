import numpy as np

CLASS0 = 0
CLASS1 = 1
CLASS2 = 2
CLASS3 = 3
CLASS4 = 4
CLASS5 = 5
CLASS6 = 6
CLASS7 = 7
CLASS8 = 8
CLASS9 = 9

class Perceptron: 
    def __init__(self):
        self.weights0 = []
        self.weights1 = []
        self.weights2 = []
        self.weights3 = []
        self.weights4 = []
        self.weights5 = []
        self.weights6 = []
        self.weights7 = []
        self.weights8 = []
        self.weights9 = []

    def get_array_from_class(self, train_class):
        if (train_class == CLASS0): return self.weights0
        elif (train_class == CLASS1): return self.weights1
        elif (train_class == CLASS2): return self.weights2
        elif (train_class == CLASS3): return self.weights3
        elif (train_class == CLASS4): return self.weights4
        elif (train_class == CLASS5): return self.weights5
        elif (train_class == CLASS6): return self.weights6
        elif (train_class == CLASS7): return self.weights7
        elif (train_class == CLASS8): return self.weights8
        elif (train_class == CLASS9): return self.weights9

    ## TODO: adjust for multiclass perceptron: change the weight adjustment to adjust for the class it got wrong and the class
    # it was supposed to guess 

    
    def train(self, train_set, train_labels, learning_rate, max_iter, train_class):
        # weights and bias param
        weights = np.zeros(len(train_set[0]))
        bias = 0
        
        for epoch in range(max_iter):
            for i in range(len(train_set)):
                prediction = self.predict(train_set[i], bias)
                if (train_labels[i] != prediction):
                    adjust = learning_rate * train_set[i]
                    if train_labels[i] < prediction:
                        adjust *= -1
                    weights += adjust
                    bias += learning_rate * (train_labels[i] - prediction)



        # return the trained weight and bias parameters
        w = self.get_array_from_class(train_class)
        w = weights
        return weights, bias

    def predict(self, weights, image, bias):
        if (np.dot(image, weights) + bias) > 0:
            return 1
        return 0


    def classify(self, weights, bias, dev_set, dev_class):
        #classify dev set
        dev_labels = []
        for image in dev_set:
            # dev_labels.append(0)
            result = self.predict(image, weights, bias)
            dev_labels.append(result)
        return dev_labels