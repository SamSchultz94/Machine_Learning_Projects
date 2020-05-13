from sklearn.datasets import load_iris

class Iris_Classification():
    def __init__(self):
        self.iris_dataset = load_iris()

    def PrintKeys(self):
        print("Keys of iris_dataset: \n{}".format(self.iris_dataset.keys()))

    def PrintDesc(self):
        print(self.iris_dataset['DESCR']+"\n")

    def PrintTargetNames(self):
        print("Target names: {}".format(self.iris_dataset['target_names']))

    
    





def testPrintKeys():
    classification = Iris_Classification()
    return classification.PrintKeys()

def testPrintDesc():
    classification = Iris_Classification()
    return classification.PrintDesc()

def testPrintTargetNames():
    classification = Iris_Classification()
    return classification.PrintTargetNames()
