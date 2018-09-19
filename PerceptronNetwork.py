from PerceptronLayer import PerceptronLayer as PLayer

class PerceptronNetwork:
    Layers = []
    def __init__( self, featureSize, numHidden, weights=[] ):
        self.Layers = []
        self.Layers.append( PLayer( featureSize, 0 ) )
        for i in range( numHidden ):
            self.Layers.append( PLayer( featureSize, i+1 ) )
        self.Layers.append(PLayer( featureSize, featureSize, True ))
        print( "Created % layers", numHidden + 1 )

    def getWeights(self):
        weights = []
        for i in range( len( self.Layers ) ):
            weights.append( self.Layers[i].getWeights() )
        return weights