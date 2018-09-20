import random

class Perceptron:
    weights = []
    alpha = 0.1
    def __init__( self, featureSize, layerNum ):
        self.weights = []
        for i in range(featureSize+1):
            self.weights.append(random.uniform(-1,1))
        print("Perceptron with " + str( len( self.weights ) ) + " weights created at layer " + str( layerNum ) )

    def train( self, data ):
        sum = 0.0
        sum += self.alpha * self.weights[0]
        for i in range( len( data ) ):
            sum += data[i] * self.weights[i+1]
        return sum
        # prediction = self.calculateSign( sum )
        # error = self.calculateError( prediction, actual )

    def sumWeights(self):
        sum = 0.0
        for i in range(len(self.weights)-1):
            sum += self.weights[i]
        return sum
    def getWeights(self):
        return self.weights

    def loadWeights(self, weights):
        for i in range( len( self.weights ) ):
            if weights[i] != None:
                print( "Replacing weight ", i)
                self.weights[i] = weights[i]

    def adjustWeights( self, error ):
        self.weights[0] += self.weights[0] * error * self.alpha
        for i in range( 1, len( self.weights ) ):
            self.weights[i] += self.weights[i] * error
