import random

def getProductIDS():
    readProductIds = open("txtFiles/ProductIDS.txt")
    productIdList = list(readProductIds.read().split("\n"))
    readProductIds.close()
    return productIdList

if __name__ == '__main__':
    PKS = getProductIDS()
    print("INSERT INTO INVENTORY VALUES")
    for i in range(len(PKS)):
        #PRO_ID, INV_QUANTITY, ISACTIVE, MIN_QUANTITY
        print(f"('{PKS[i]}', {random.randint(50, 1000)}, {10}, 1)", end ='')
        if(i != len(PKS) - 1 ):
            print(", ")

