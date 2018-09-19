from PerceptronNetwork import  PerceptronNetwork as PNetwork
import numpy as np
import pandas as pd
from ast import literal_eval

hiddenLayers = 0
featureSize = 3

def main( ):
    weights = readCSV( )
    Predictor = PNetwork( featureSize, hiddenLayers )
    print(weights)
    if len(weights) == len(Predictor.getWeights()) and len( weights[0] ) == len(Predictor.getWeights()[0] ):
        Predictor.loadWeights( weights )
    weights = Predictor.getWeights( )
    print(weights)
    writeCSV( weights)

def readCSV( ):
    df = pd.read_csv( 'weights.csv', header=None, na_values=[''])
    df = df.T
    df = df.where( ( pd.notnull( df ) ), None)
    for i in range( hiddenLayers + 2 ):
        for j in range( featureSize ):
            if df[i][j] != None:
                df[i][j] = literal_eval( df[i][j] )
            else:
                df[i][j] = None
    return df.T.values.tolist( )

def writeCSV( weights ):
    df = pd.DataFrame( weights )
    df.to_csv( 'weights.csv', index=False, header=False )
    
    
if __name__ == "__main__":
    main( )