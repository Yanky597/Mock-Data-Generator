
import random


'''
This file generates the data for the LOGIN table
'''

def getCustomerPks():
    getAFakeHash()

    hashes = []
    readPks = open("listOfMyCustomerPKs.txt")
    pkList = list(readPks.read().split("\n"))
    for i in pkList:
        hashes.append(getAFakeHash())
    return [pkList, hashes]


def getAFakeHash():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*0123456789'
    # upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # characters = '!@#$%^&*'
    # numbers = '0123456789'
    word = ''
    for i in range(256):
        word += letters[random.randint(0, len(letters)-1)]
    return word


if __name__ == '__main__':
    loginInfo = getCustomerPks()
    pks = loginInfo[0]
    hashes = loginInfo[1]

    print("INSERT INTO LOGIN")
    for i in range(len(pks)):
        print(f"VALUES('{pks[i]}', '{hashes[i]}')", end='')
        if i != (len(pks)-1):
            print(',')
