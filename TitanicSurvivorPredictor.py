from PerceptronNetwork import  PerceptronNetwork as PNetwork

def main():
    Predictor = PNetwork(3,1)
    print(Predictor.getWeights())

if __name__ == "__main__":
    main()