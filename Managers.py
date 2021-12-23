
import random
import math

def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data

if __name__ == '__main__':
    managers = getValuesFromFile("Managers.txt")
    departments = getValuesFromFile("DepartmentIDS.txt")

    print("INSERT INTO MANAGERS VALUES")
    for i in range(len(managers)):
        print(F"({managers[i]}, {departments[random.randint(0, len(departments) - 1)]})", end='')

        if (i != len(managers) - 1):
            print(",")



