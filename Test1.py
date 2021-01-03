import time

users = [{'name': 'Omar', 'balance': 2200, 'pinCode': 2707},
         {'name': 'Abdo', 'balance': 3000, 'pinCode': 1352},
         {'name': 'Rawda', 'balance': 1000, 'pinCode': 2298},
         {'name': 'Mohamed', 'balance': 5000, 'pinCode': 1964},
         {'name': 'Gege', 'balance': 2500, 'pinCode': 1974},
         {'name': 'Esawy', 'balance': 500, 'pinCode': 6896},
         {'name': 'Saif', 'balance': 1000, 'pinCode': 9106},
         {'name': 'Ali', 'balance': 2000, 'pinCode': 2256},
         {'name': 'Hadeer', 'balance': 10000, 'pinCode': 0000},
         {'name': 'Mika', 'balance': 1000, 'pinCode': 1111}]



currentUser = {}
currentPinCode = 0

def loading(t):
    for i in range(1,t):
        print("\rLoading" + "."*i, end="")
        time.sleep(1)

def initialScreen():
    global currentUser
    global currentPinCode
    found = False
    loading(3)
    print("\r#####################################################")
    print("#               Welcome To Omar's ATM                 #")
    print("                 Please! Enter Your 4-Digits pin code# ")
    currentPinCode = int(input("Your 4-digits pin code   "))
    print("#                                                     #")
    print("#                                                     #")
    print("#                                                     #")
    print("#######################################################")
    for user in users:
        if user['pinCode'] == currentPinCode:
            currentUser = user
            found = True
    if found:
        selectScreen()
    else:
        errorScreen()
    return





def errorScreen():
    print("\r#####################################################")
    print("#                                                     #")
    print("#               Welcome To Omar's ATM                 #")
    print("#                     ERROR                           #")
    print("#               Your pin code dosn't match            #")
    print("#                                                     #")
    print("#                                                     #")
    print("#                                                     #")
    print("#######################################################")
    loading(5)
    initialScreen()
    return


def selectScreen():
    print("\r#####################################################")
    print("#                                                     #")
    print("#               Welcome To Omar's ATM                 #")
    print("#            WELCOME", currentUser["name"],"          #")
    print("#            Please Select the required operation     #")
    print("#  1- Cash Withdrawal                                 #")
    print("#  2- Balance inquiry                                 #")
    print("#  3- Transfer                                        #")
    print("#  4- Bill payment                                    #")
    print("#  5- Settings                                        #")
    print("#  6- Donate                                          #")
    operation = int(input())
    print("#######################################################")
    if operation == 1:
        cashWithDrawal()
    elif operation == 2:
        balanceInquiry()
    elif operation == 3:
        transfare()
    elif operation == 4:
        pillPayment()
    elif operation == 5:
        Settings()
    elif operation== 6:
        donate()
    else:
        errorScreen()
    loading(5)


    return

def cashWithDrawal():
    global currentUser
    print("\r#####################################################")
    print("#                                                     #")
    print("#               Welcome To ATM                        #")
    print("#               Please insert the required amount     #")
    print("#                                                     #")
    amount = int(input())
    print("#                                                     #")
    print("#                                                     #")
    print("#######################################################")
    if amount <= currentUser['balance']:
        currentUser['balance'] = currentUser['balance'] - amount
        print("Your transaction is being processed ....")
        balanceInquiry()
    else:
        print("Your balance is not enough")



    return

def balanceInquiry():
    loading(5)
    print("\r#####################################################")
    print("#                                                     #")
    print("#               Welcome To Omar's ATM                 #")
    print("#       Your balance is : ",currentUser['balance'],  "#")
    print("#                                                     #")
    print("#                                                     #")
    print("#                                                     #")
    print("#                                                     #")
    print("#######################################################")
    print("Do you want to do another operation ? PLEASE select YES   or    NO")
    operation2 = input()
    if operation2 == "YES":
        selectScreen()
    if operation2 == "NO":
        print("Thank you and good bye")
    loading(3)
    return

def transfare():
    global currentUser
    print("\r#####################################################")
    print("#                                                     #")
    print("#               Welcome To ATM                        #")
    print("#               Please insert the required amount     #")
    print("#                                                     #")
    amount = int(input())
    name = input("Enter the name ")
    print("#                                                     #")
    print("#                                                     #")
    print("#######################################################")
    if amount <= currentUser['balance']:
        for user in users:
            if name == user['name']:
                user['balance'] = user['balance'] + amount
                currentUser['balance'] = currentUser['balance'] - amount
                print('Your transaction is being processed')
        balanceInquiry()



def pillPayment():
    return

def Settings():
    return

def donate():
    return


initialScreen()
