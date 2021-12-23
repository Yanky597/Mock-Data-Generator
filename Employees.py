import random

import math

'''
This file generates the data for the customers table


REMEMBER to KEEP in mind the order of the files that write data!
for example this EMPLOYEES.py
'''


def generateCustomerIDS(amountOfNumbersToGenerate):
    writeToListOfCustomersPKs = open('listOfMyCustomerPKs.txt', 'w')
    pkList = [math.floor(random.random() * 1000000) for x in range(amountOfNumbersToGenerate)]
    setOfPks = set(pkList)
    newPkList = []
    for i in setOfPks:
        newPkList.append(i)
        writeToListOfCustomersPKs.write(f"{str(i)}\n")
    writeToListOfCustomersPKs.close()
    return newPkList


def getAListOfFirstNames():
    readFirstNamefile = open('firstNames.txt')
    nameList = list(readFirstNamefile.read().split("\n"))
    readFirstNamefile.close()
    return nameList


def getAListOfLastNames():
    readLastNamefile = open('lastNames.txt')
    nameList = list(readLastNamefile.read().split(",\n"))
    readLastNamefile.close()
    return nameList


def generatePhoneNumbers():
    readAreaCodes = open('areaCodes.txt')
    areaCodeList = list(readAreaCodes.read().split("\n"))
    readAreaCodes.close()
    return f"{areaCodeList[random.randint(0, len(areaCodeList) - 1)]}" \
           f"-{random.randint(100, 999)}" \
           f"-{random.randint(1000, 9999)}"


def getAListOfEmails(lastNames, firstNames):
    emailList = []
    # readEmailVendors = open('emailVendors.txt')
    # emailVendorList = list(readEmailVendors.read().split("\n"))
    for i in range(1000):
        emailList.append(f"{firstNames[i]}{str(lastNames[i])[:2]}"
                         f"{str(random.randint(1, 999))[:random.randint(1, 3)]}@EBD.COM")

    # readEmailVendors.close()
    return emailList


def getAddress():
    addresses = []
    zipCodes = []
    readAddresses = open('address.txt')
    addressList = list(readAddresses.read().split("\n"))
    for i in addressList:
        if 'NY' in i:
            zipCodes.append(i[i.index('NY') + 3:])
        else:
            addresses.append(i[:])

    return [addresses, zipCodes]


def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data


def getPositionIDsAndSalaries(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    IDS = []
    salaries = []
    for i in data:
        splitIt = i.split("|")
        IDS.append(splitIt[0].strip())
        salaries.append(splitIt[2].strip())
    file.close()
    return [IDS, salaries]


# def CreateEmpID():
#     createFile = open("EmployeeID.txt", "w")
#     for i in range(3000):
#         createFile.write(f'{random.randint(1000000, 9999999)}\n')
#     createFile.close()

# def makeItASet():
#     readFile = open("EmployeeID.txt")
#     dataSet = set(readFile.read().split("\n"))
#     readFile.close()
#     createFile = open("EmployeeID.txt", "w")
#     for i in dataSet:
#         createFile.write(f'{i}\n')
#
#     createFile.close()

def getManagers():
    managerList = []
    employeeIDS = getValuesFromFile("EmployeeID.txt")
    for i in range(math.floor(len(employeeIDS) / 15)):
        manager = employeeIDS[random.randint(0, len(employeeIDS) - 1)]
        while (manager in managerList):
            manager = employeeIDS[random.randint(0, len(employeeIDS) - 1)]
        managerList.append(manager)
    return managerList


if __name__ == '__main__':
    employeeIDS = getValuesFromFile("EmployeeID.txt")
    lastNameList = sorted(getValuesFromFile('lastNames.txt'), reverse=True)
    firstNameList = getValuesFromFile('firstNames.txt')
    emailList = getAListOfEmails(lastNameList, firstNameList)
    positionIDS = getPositionIDsAndSalaries("PositionID_Name_Salary.txt")
    posIDS = positionIDS[0]
    salaries = positionIDS[1]
    durationAtCompany = sorted(getValuesFromFile("dates.txt"), reverse=True)
    managersIDS = getManagers()
    writeToMangers = open("Managers.txt", "w")
    for i in managersIDS:
        writeToMangers.write(f"{i}\n")
    writeToMangers.close()

    num = 500

    createSales = open("salesPeople.txt", "w")

    manager = ''
    print("INSERT INTO EMPLOYEES VALUES", end='')
    for i in range(num):
        manager = managersIDS[random.randint(0, len(managersIDS) - 1)]

        if employeeIDS[i] in managersIDS:
            manager = "\'\'"
        elif employeeIDS[i] == manager:
            while employeeIDS[i] == manager:
                manager = managersIDS[random.randint(0, len(managersIDS) - 1)]

        position = random.randint(0, len(posIDS) - 1)
        salesPerson = '2537508041'
        if salesPerson == posIDS[position]:
            createSales.write(f"{employeeIDS[i]}\n")

        print(F"\n('{employeeIDS[i]}', "
              F"'{lastNameList[i]}', "
              F"'{firstNameList[i]}', "
              F"'{generatePhoneNumbers()}', "
              F"'{emailList[i]}', "
              F"'{posIDS[position]}', "
              F"'{int(salaries[position]) * random.randint(1, 3)}', "
              F"'{durationAtCompany[random.randint(0, len(durationAtCompany) - 1)]}',"
              F"{manager}"
              F")", end='')

        if (i != num - 1):
            print(",", end='')

    createSales.close()
