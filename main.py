# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
import math

'''
This file generates the data for the customers table
'''

def generateCustomerIDS(amountOfNumbersToGenerate):
    writeToListOfCustomersPKs = open('listOfMyCustomerPKs.txt', 'w')
    pkList = [math.floor(random.random() * 1000000) for x in range(amountOfNumbersToGenerate)]
    for i in pkList:
        writeToListOfCustomersPKs.write(f"{str(i)}\n")
    writeToListOfCustomersPKs.close()
    return pkList


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
    return f"{areaCodeList[random.randint(0, len(areaCodeList) -1)]}" \
           f"-{random.randint(100, 999)}" \
           f"-{random.randint(1000, 9999)}"


def getAListOfEmails(lastNames, firstNames):
    emailList = []
    readEmailVendors = open('emailVendors.txt')
    emailVendorList = list(readEmailVendors.read().split("\n"))
    for i in range(1000):
        emailList.append(f"{firstNames[i]}{str(lastNames[i])[:2]}"
                         f"{str(random.randint(1,999))[:random.randint(1,3)]}@"
                         f"{emailVendorList[random.randint(0, len(emailVendorList) -1)]}")
    readEmailVendors.close()
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    randNum = random.randint(1000, 10000)
    num = 1000
    customerIDs = generateCustomerIDS(num)
    lastNames = getAListOfLastNames()
    firstNames = getAListOfFirstNames()
    emailList = getAListOfEmails(lastNames, firstNames)
    addressAndZip = getAddress()
    addresses = addressAndZip[0]
    zipCodes = addressAndZip[1]


    # print(generatePhoneNumbers())
    print("INSERT INTO CUSTOMERS", end='')
    for i in range(num):
        print(F" \nVALUES('{customerIDs[i]}', "
              F"'{lastNames[i]}', "
              F"'{firstNames[i]}', "
              F"'{generatePhoneNumbers()}', "
              F"'{emailList[i]}', '{addresses[i]}', '{zipCodes[i]}')",  end='')
        if(i != num-1):
            print(",", end='')

    # print(getAListOfFirstNames())
    # print(getAListOfLastNames())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
