import random
import math

def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data

def getIDSAndPrices(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    # data.split("|")
    file.close()
    return data

def generatePrices():
    readProductPrices = open("txtFiles/costPrices.txt")
    costPrice = readProductPrices.read().split("\n")
    salePrice = []
    for i in costPrice:
        salePrice.append((int(i) * 2) - .05)

    readProductPrices.close()

    return [costPrice, salePrice]


if __name__ == '__main__':
    productIDS = getIDSAndPrices("txtFiles/ProductPluseCostPrice.txt")
    # for i in productIDS:
    #     print(i.split("|")[1])

    #InvoiceIDS = getValuesFromFile("txtFiles/InvoiceIDS.txt")[:100]
    # current amount of invoices is 100
    print("INSERT INTO INVOICE_ROW VALUES")
    rows = 100
    for i in range(rows):
        amountOfItems = random.randint(1, len(productIDS) - 1)
        checkList = []
        for j in range(amountOfItems):
            num = random.randint(0, len(productIDS) - 1)
            if(num in checkList):
                while (num in checkList):
                    num = random.randint(0, len(productIDS) - 1)


            checkList.append(num)

            ID = productIDS[num].split('|')[0]
            price = (int(productIDS[num].split('|')[1]) * 2 - .05)
            quantity = random.randint(1, 30)
            discount = .90 if quantity > 10 else 0
            finalPrice = (price * quantity) * discount if discount != 0 else (price * quantity)
            print(f"('{i}', '{ID}', "
                  f"{price}, {quantity}, {discount}, {round(finalPrice, 2)})", end="")
            if (i != rows - 1):
                print(",")



