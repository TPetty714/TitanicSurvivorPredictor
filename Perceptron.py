import random

class Perceptron:
    weights = []
    def __init__( self, featureSize, layerNum ):
        self.weights = []
        for i in range(featureSize):
            self.weights.append(random.uniform(-1,1))
        print("Perceptron with % weights created at layer %", len(self.weights), layerNum)

    def getWeights(self):
        return self.weights