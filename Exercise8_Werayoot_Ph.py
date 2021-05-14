usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "virus" and passwordInput == "covid19" :
    print("Login Success")
    if True :
        print("You're welcome")
        print("-----------------------------")
        print("Product List :")
        print("1. Pfizer price : 500 (THB)")
        print("2. Moderna : 450 (THB)")
        print("3. Sinovac : 550 (THB)")
        print("4. AstraZeneca : 400 (THB)")
        userSelected = int(input(">>>"))
        Pf = 500
        Mo = 450
        Si = 550
        As = 400
        if userSelected == 1 :
           amount = int(input("Amount (Dose) :"))
           print("Total (THB) : ",amount*Pf)
        elif userSelected == 2 :
           amount = int(input("Amount (Dose) :"))
           print("Total (THB) : ",amount*Mo)
        elif userSelected == 3 :
           amount = int(input("Amount (Dose) :"))
           print("Total (THB) : ",amount*Si)
        elif userSelected == 4 :
           amount = int(input("Amount (Dose) :"))
           print("Total (THB) : ",amount*As)
        else :
           print("!!!!!Please Select type of Vaccine !!!!!")
else :
    print("Login Failed !!!!")
