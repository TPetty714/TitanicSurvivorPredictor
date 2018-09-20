from PerceptronNetwork import  PerceptronNetwork as PNetwork
import numpy as np
import pandas as pd
import pickle
import os
from ast import literal_eval

hiddenLayers = 0
featureSize = 2

def main( ):
    # weights = readCSV( )
    weights = readFile()
    Predictor = PNetwork( featureSize, hiddenLayers )
    print(weights)
    if len(weights) == len(Predictor.getWeights()) and len( weights[0] ) == len(Predictor.getWeights()[0] ):
        Predictor.loadWeights( weights )
    sum = Predictor.train( [1,2], [1.5] )
    print( sum )
    weights = Predictor.getWeights( )
    # print(weights)
    # writeCSV( weights)
    writeFile( weights )

def readFile( ):
    weights = []
    if os.path.isfile("weights.txt"):
        with open( "weights.txt", 'rb' ) as fp:
            weights = pickle.load(fp)
    return weights

def writeFile( weights ):
    if os.path.isfile("weights.txt"):
        os.remove("weights.txt")
    fp = open( "weights.txt", 'wb' )
    pickle.dump(weights, fp)


def readCSV( ):
    df = pd.read_csv( 'weights.csv', header=None, na_values=[''])
    df = df.T
    df = df.where( ( pd.notnull( df ) ), None)
    for i in range( len( df ) ):
        for j in range( len( df[0] ) ):
            try:
                if df[i][j] != None:
                    df[i][j] = literal_eval( df[i][j] )
                else:
                    df[i][j] = None
            except KeyError:
                continue
    return df.T.values.tolist( )

def writeCSV( weights ):
    df = pd.DataFrame( weights )
    df.to_csv( 'weights.csv', index=False, header=False )
    
    
if __name__ == "__main__":
    main( )