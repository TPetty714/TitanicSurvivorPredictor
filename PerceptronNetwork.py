from PerceptronLayer import PerceptronLayer as PLayer

class PerceptronNetwork:
    Layers = []
    def __init__( self, featureSize, numHidden ):
        self.Layers = []
        self.Layers.append( PLayer( featureSize, 0 ) )
        for i in range( numHidden ):
            self.Layers.append( PLayer( featureSize, i+1 ) )
        self.Layers.append(PLayer( featureSize, numHidden + 1, True ))
        print( "Created " + str( numHidden + 2 ) + " layers")

    def getWeights(self):
        weights = []
        for i in range( len( self.Layers ) ):
            weights.append( self.Layers[i].getWeights() )
        return weights