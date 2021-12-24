import random
import math

def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data


if __name__ == '__main__':
    InvoiceIDS = getValuesFromFile("txtFiles/InvoiceIDS.txt")
