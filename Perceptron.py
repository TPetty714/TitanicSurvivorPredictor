import random

class Perceptron:
    weights = []
    def __init__( self, featureSize, layerNum ):
        self.weights = []
        for i in range(featureSize+1):
            self.weights.append(random.uniform(-1,1))
        print("Perceptron with " + str( len( self.weights ) ) + " weights created at layer " + str( layerNum ) )

    def getWeights(self):
        return self.weights

    def loadWeights(self, weights):
        for i in range( len( self.weights ) ):
            if weights[i] != None:
                print( "Replacing weight ", i)
                self.weights[i] = weights[i]
