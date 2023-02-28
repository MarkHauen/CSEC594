from os import path

dataFileName = "SurveyDataTrimed"
finalHeaders = "Cryptography_Score|BCDR_Score|Group|Gender|Education|Cryptography_Exp|BCDR_Exp"

def getRoot():
    return path.dirname(path.realpath(__file__))

def getDataPath(fileName):
    return "{r}\\{fn}.csv".format(r=getRoot(), fn=fileName)

def getFileLines(fileName):
    with open(getDataPath(fileName), mode='rt') as reader:
        return reader.readlines()

def getCorrectAnswers():
    return getFileLines(dataFileName)[1]

def getDataLines():
    return getFileLines(dataFileName)[2:]

def writeDataLines(fileName, dataLines):
    with open("{r}\\{fn}.csv".format(r=getRoot(), fn=fileName), mode='wt') as writer:
        writer.write("{h}\n{dl}".format(h=finalHeaders, dl=dataLines))