from PerceptronNetwork import  PerceptronNetwork as PNetwork
import csv

def main():
    Predictor = PNetwork(3,0)
    weights = Predictor.getWeights()
    fp = open("weights.csv", 'w')
    with fp:
        writer = csv.writer(fp)
        writer.writerows(weights)
    print(weights)

if __name__ == "__main__":
    main()