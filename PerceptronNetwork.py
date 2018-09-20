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

    def train( self, data, actuals ):
        layerSums = []
        layerSums.append( self.Layers[0].train( data ) )
        for i in range( len( self.Layers ) ):
            layerSums.append( self.Layers[i].train( layerSums[i] ) )
        # sum = 0.0
        # for i in range( len( layerSums ) ):
        #     for j in range( len( layerSums[i] ) ):
        #         sum += layerSums[i][j]
        print( sum )
        self.backpropogate( layerSums[ len( layerSums ) - 1 ], actuals )
        # return self.calculateSign( sum )
        return layerSums[ len( self.Layers ) - 1 ]

    def calculateSign(self, value):
        if value <= 0:
            return -1
        else:
            return 1

    def calculateError(self, predicted, actual):
        error = actual - predicted
        return error

    def getWeights(self):
        weights = []
        for i in range( len( self.Layers ) ):
            weights.append( self.Layers[i].getWeights() )
        return weights

    def loadWeights(self, weights):
        for i in range(len(self.Layers)):
            if weights[i] !=None:
                print( "Replacing weights on layer ", i )
                self.Layers[i].loadWeights(weights[i])

    def backpropogate(self, sums, actuals):
        errors = []
        layerError = []
        perceptronError = 0.0
        # increment through each perceptron in last layer
        for i in range( len( self.Layers[ len( self.Layers ) - 1 ].perceptrons ), 0, -1 ):
            errors.append( self.calculateError( sums[i - 1], actuals[i - 1] ) )
            self.Layers[len(self.Layers) - 1].perceptrons[i - 1].adjustWeights( errors[i - 1] )
        #     Increment from second to last layer to first layer
        for layer in range(len(self.Layers) - 1, 0, -1):
            # Increment over each perceptron
            for j in range(len(self.Layers[ layer-1].perceptrons) - 1, 0, -1):
                # Increment over each weight
                for k in range(len(self.Layers[ layer-1 ].perceptrons[j].weights)):
                    perceptronError += (self.Layers[layer-1].perceptrons[j].weights[k]/self.Layers[layer-1].perceptrons[j].sumWeights()) * errors[k]
                layerError.append(perceptronError)
                self.Layers[layer-1].perceptrons[j].adjustWeights(perceptronError)
            errors = layerError




