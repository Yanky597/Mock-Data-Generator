
import random
import math

def createProductId(amountNeeded):
    listOfProductIDs = [math.floor(random.random() * 1000) for x in range(amountNeeded)]
    writeToProductIDS = open("txtFiles/ProductIDS.txt", "w")

    for i in listOfProductIDs:
        writeToProductIDS.write(f'{i}\n')

    writeToProductIDS.close()
    return listOfProductIDs




    return listOfProductIDs

def getProductNames():
    readProductNames = open("txtFiles/productNames.txt")
    writeToProductSyle = open("txtFiles/productStyleNumbers", "w")
    listOfProductNames = readProductNames.read().split("\n")
    for i in range(len(listOfProductNames)):
        writeToProductSyle.write(f"PN-{str(listOfProductNames[i])[:2]}{math.floor(random.random()*100000)}\n")
    readProductNames.close()
    writeToProductSyle.close()

    return listOfProductNames

def getProductStyleNums():
    readProductStyles = open("txtFiles/productStyleNumbers")
    productStyles = readProductStyles.read().split("\n")
    readProductStyles.close()
    return productStyles

def generatePrices():
    readProductPrices = open("txtFiles/costPrices.txt")
    costPrice = readProductPrices.read().split("\n")
    salePrice = []
    for i in costPrice:
        salePrice.append((int(i) * 2) - .05)

    readProductPrices.close()

    return [costPrice, salePrice]

def getDates(amountOfDates):
    readDates = open("txtFiles/dates.txt")
    dateList = list(readDates.read().split("\n"))
    readDates.close()
    return dateList


if __name__ == '__main__':
    prices = generatePrices()
    costPrice = prices[0]
    salePrice = prices[1]
    productNames = getProductNames()
    productStyles = getProductStyleNums()
    getProductIDS = createProductId(len(productNames))
    getDateList = getDates(len(productNames))


    print("INSERT INTO PRODUCTS VALUES")
    for i in range(len(productNames)):
        print(f" ('{getProductIDS[i]}', '{productNames[i]}','{productStyles[i]}', '{costPrice[i]}', '{salePrice[i]}', '{getDateList[random.randint(0, len(productNames) -1)]}')", end='')
        if i != (len(productNames)-1):
            print(',')

