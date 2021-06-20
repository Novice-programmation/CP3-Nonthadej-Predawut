menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    print('Total:',sum(priceList))

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()