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

    def getWeights(self):
        weights = []
        for i in range( len( self.perceptrons ) ):
            weights.append( self.perceptrons[i].getWeights() )
        return weights