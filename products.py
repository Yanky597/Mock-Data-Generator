
import random
import math

def getProductNames():
    readProductNames = open("productNames.txt")
    writeToProductSyle = open("productStyleNumbers", "w")
    listOfProductNames = readProductNames.read().split("\n")
    for i in range(len(listOfProductNames)):
        writeToProductSyle.write(f"PN-{str(listOfProductNames[i])[:2]}{math.floor(random.random()*100000)}\n")
    readProductNames.close()
    writeToProductSyle.close()

    return listOfProductNames

def getProductStyleNums():
    readProductStyles = open("productStyleNumbers")
    productStyles = readProductStyles.read().split("\n")
    readProductStyles.close()
    return productStyles

def generatePrices():
    readProductPrices = open("costPrices.txt")
    costPrice = readProductPrices.read().split("\n")
    salePrice = []
    for i in costPrice:
        salePrice.append((int(i) * 2) - .05)

    readProductPrices.close()

    return [costPrice, salePrice]



if __name__ == '__main__':
    prices = generatePrices()
    costPrice = prices[0]
    salePrice = prices[1]
    productNames = getProductNames()
    productStyles = getProductStyleNums()


    print("INSERT INTO PRODUCTS")
    for i in range(len(productNames)):
        print(f"VALUES ('{productNames[i]}','{productStyles[i]}', '{costPrice[i]}', '{salePrice[i]}')", end='')
        if i != (len(productNames)-1):
            print(',')

