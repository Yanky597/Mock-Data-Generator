def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data


if __name__ == '__main__':

    salesPeople = getValuesFromFile("txtFiles/salesPeople.txt")


    print("INSERT INTO SALESPEOPLE VALUES")
    for i in range(len(salesPeople)):
        print(f"({salesPeople[i]}, 0)", end='')

        if(i != len(salesPeople) - 1):
            print(",")
