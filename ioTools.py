from os import path

# Data file name
dataFileName = "SurveyDataTrimed"
# Headers for the final output file
headers = "Cryptography_Score|BCDR_Score|Group|Gender|Education|Cryptography_Exp|BCDR_Exp"

def getRoot(): # Get the root path of the project
    return path.dirname(path.realpath(__file__))

def getDataPath(fileName): # Get the path of the data file
    return "{r}\\{fn}.csv".format(r=getRoot(), fn=fileName)

def getFileLines(fileName): # Get the lines of the data file
    with open(getDataPath(fileName), mode='rt') as reader:
        return reader.readlines()

def getCorrectAnswers(): # Get the correct answers from the data file
    return getFileLines(dataFileName)[1].split(",")

def getDataLines(): # Get the data lines from the data file
    return getFileLines(dataFileName)[2:]

def writeDataLines(fileName, dataLines): # Write the data lines to the output file
    with open("{r}\\{fn}.csv".format(r=getRoot(), fn=fileName), mode='wt') as writer:
        writer.write("{h}\n{dl}".format(h=headers, dl=dataLines))