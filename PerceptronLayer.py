from Perceptron import Perceptron

class PerceptronLayer:
    perceptrons = []
    def __init__(self, featureSize, layerNum, finalLayer = False):
        self.perceptrons = []
        if not finalLayer:
            for i in range( featureSize ):
                self.perceptrons.append( Perceptron( featureSize, layerNum ) )
        else:
            self.perceptrons.append( Perceptron( featureSize, layerNum ) )

    def train( self, data ):
        sums = []
        for i in range( len( self.perceptrons ) ):
            sums.append( self.perceptrons[i].train( data ) )
        return sums

    def getWeights(self):
        weights = []
        for i in range( len( self.perceptrons ) ):
            weights.append( self.perceptrons[i].getWeights() )
        return weights

    def loadWeights(self, weights):
        for i in range( len( self.perceptrons ) ):
            if weights[i] != None:
                print( "Replacing weights on perceptron ", i)
                self.perceptrons[i].loadWeights(weights[i])

    # def calculateErrors( self, outputs, actuals ):
