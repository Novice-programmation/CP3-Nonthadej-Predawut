usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "Benutzername"  and passwordInput == "Passwort":
    userSelected = int(input("กด 1 สำหรับภาษาไทย\n"
                             "Press 2 for English."))
    if userSelected == 1:
        print("ยินดีต้อนรับสู่ร้านค้าแห่งหนึ่ง")
        print("--------------------")
        print("ยางลบ ก้อนละ ๕ บาท")
        print("ดินสอ แท่งละ ๑๐ บาท")
        print("กรุณาเลือกสินค้า:")
        จำนวนยางลบ = input("กรุณาใส่จำนวนยางลบ:")
        จำนวนดินสอ = input("กรุณาใส่จำนวนดินสอ:")
        ราคายางลบ = 5
        ราคาดินสอ = 10
        result = int(จำนวนยางลบ)*int(ราคายางลบ) + int(จำนวนดินสอ)*int(ราคาดินสอ)
        print("ราคาทั้งหมด:",result,"บาท")
    elif userSelected == 2:
        print("Welcome to a shop")
        print("--------------------")
        print("Eraser 6 THB each")
        print("Pencil 12 THB each")
        print("Please select merchandise:")
        nEraser = input("Please input amount of eraser:")
        nPencil = input("Please input amount of pencil:")
        priceeraser = 6
        pricepencil = 12
        result = int(nEraser) * int(priceeraser) + int(nPencil) * int(pricepencil)
        print("Total price:", result, "THB")
else:
    print("Login failed!")