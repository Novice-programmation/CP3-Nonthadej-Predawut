usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "Benutzername"  and passwordInput == "Passwort":
    print("ยินดีต้อนรับสู่ร้านค้าแห่งหนึ่ง")
    print("--------------------")
    print("กรุณาเลือกสินค้า")
    print("ยางลบ ก้อนละ ๕ บาท")
    print("ดินสอ แท่งละ ๘ บาท")
    print("ปากกา ด้ามละ ๑๐ บาท")
    userSelected = int(input("กด 1 ยางลบ\n"
                             "กด 2 ดินสอ\n"
                             "กด 3 ปากกา\n"
                             "กด 4 ทำรายการเสร็จสิ้น"))
    ราคายางลบ = 5
    ราคาดินสอ = 8
    ราคาปากกา = 10
    จำนวนยางลบ = 0
    จำนวนดินสอ = 0
    จำนวนปากกา = 0
    while userSelected==1 or 2 or 3 or 4:
        if userSelected == 1:
            จำนวนยางลบ = input("กรุณาใส่จำนวนยางลบ:")
            subtotaleraser=int(จำนวนยางลบ) * int(ราคายางลบ)
            print("Subtotal ยางลบ",subtotaleraser,"บาท")
            print("กรุณาเลือกสินค้า")
            userSelected = int(input("กด 1 ยางลบ\n"
                                     "กด 2 ดินสอ\n"
                                     "กด 3 ปากกา\n"
                                     "กด 4 ทำรายการเสร็จสิ้น"))
        elif userSelected == 2:
            จำนวนดินสอ = input("กรุณาใส่จำนวนดินสอ:")
            subtotalpencil = int(จำนวนดินสอ) * int(ราคาดินสอ)
            print("Subtotal ดินสอ",subtotalpencil,"บาท")
            print("กรุณาเลือกสินค้า")
            userSelected = int(input("กด 1 ยางลบ\n"
                                     "กด 2 ดินสอ\n"
                                     "กด 3 ปากกา\n"
                                     "กด 4 ทำรายการเสร็จสิ้น"))
        elif userSelected == 3:
            จำนวนปากกา = input("กรุณาใส่จำนวนปากกา:")
            subtotalpen = int(จำนวนปากกา) * int(ราคาปากกา)
            print("Subtotal ปากกา",subtotalpen,"บาท")
            print("กรุณาเลือกสินค้า")
            userSelected = int(input("กด 1 ยางลบ\n"
                                     "กด 2 ดินสอ\n"
                                     "กด 3 ปากกา\n"
                                     "กด 4 ทำรายการเสร็จสิ้น"))
        elif userSelected == 4:
            result = int(จำนวนยางลบ) * int(ราคายางลบ) + int(จำนวนดินสอ) * int(ราคาดินสอ)+ int(จำนวนปากกา) * int(ราคาปากกา)
            print("ราคาทั้งหมด",result,"บาท")
            print("กรุณาชำระเงินที่cashier")
            print("ขอบคุณครับ")
            break
        else:
            print("Error! Please select only 1-4")
            userSelected = int(input("กด 1 ยางลบ\n"
                                 "กด 2 ดินสอ\n"
                                 "กด 3 ปากกา\n"
                                 "กด 4 ทำรายการเสร็จสิ้น"))
else:
    print("Login failed!")