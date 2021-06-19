def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Base+Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>>"))
    return userSelected
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login()==True:
    showMenu()
    userSelected=menuSelect()
    if userSelected==1:
        totalPrice = int(input("Base price (THB) : "))
        print('Total price including VAT =',vatCalculator(totalPrice))
    elif userSelected==2:
        print('Total price of the 2 items including VAT =',priceCalculator())
    else:
        print('end')
else:
    exit()