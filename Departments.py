import random


def getValuesFromFile(fileName):
    file = open(fileName)
    data = set(file.read().split("\n"))
    file.close()
    return data


if __name__ == '__main__':
    getDepartmentIDS = list(getValuesFromFile("DepartmentIDS.txt"))


    # openFile = open("DepartmentIDS.txt", "w")
    # for i in getDepartmentIDS:
    #     openFile.write(f'{i}"\n"')
    # openFile.close()

    getDeprtmentNames = list(getValuesFromFile("DepartmentNames.txt"))

    print("INSERT INTO DEPARTMENTS VALUES")
    for i in range(len(getDeprtmentNames)):
        print(f"({getDepartmentIDS[i]}, '{getDeprtmentNames[i]}')", end='')
        if i != len(getDeprtmentNames) - 1:
            print(",")


