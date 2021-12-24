import random
import math

def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data

# def CreateEmpID():
#     createFile = open("InvoiceIDS.txt", "w")
#     for i in range(3000):
#         createFile.write(f'{random.randint(1000000, 9999999)}\n')
#     createFile.close()
#
# def makeItASet():
#     readFile = open("InvoiceIDS.txt")
#     dataSet = set(readFile.read().split("\n"))
#     readFile.close()
#     createFile = open("InvoiceIDS.txt", "w")
#     for i in dataSet:
#         createFile.write(f'{i}\n')
#
#     createFile.close()

if __name__ == '__main__':
    InvoiceIDS = getValuesFromFile("txtFiles/InvoiceIDS.txt")
    customerIDs = getValuesFromFile("txtFiles/listOfMyCustomerPKs.txt")
    Emp_IDS = getValuesFromFile("txtFiles/salesPeople.txt")
    Dates = getValuesFromFile("txtFiles/dates.txt")
    referallCode = getValuesFromFile("txtFiles/referallCode.txt")

    print("INSERT INTO INVOICES VALUES")
    num = 2000
    for i in range(num):
        bool = random.randint(0, 1)
        if(bool == 1):
            salesPerson = Emp_IDS[random.randint(0, len(Emp_IDS) - 1)]
        else:
            salesPerson = 0
        print(f"({i}, "
              f"{customerIDs[random.randint(0, len(customerIDs) - 1 )]},"
              f" {salesPerson}, "
              f"'{Dates[random.randint(0, len(Dates)-1)]}'"
              f"{0},"
              f"'{referallCode[random.randint(0, len(referallCode) - 1)]}')", end="")
        if (i != num - 1):
            print(",")


