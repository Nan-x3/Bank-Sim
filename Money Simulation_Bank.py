# Project

# Importing

import pickle

# Main Code


def CreateNewAcc():
    try:
        f = open("Bank", "ab+")
        if f.tell() > 0:
            f.seek(0)
            Rec = pickle.load()
            

        else:
            Rec = []

        while True:
            AccNo = int(input("\nEnter Account Number: "))
            for i in range(len(Rec)):
                if Rec[i][0] == AccNo:
                    print("Account already exists.")
                    continue
            Name = input("\nPlease enter your name: ")
            Dep = float(
                input("\nPlease enter the amount you want to deposit: "))
            MobileNo = int(input("\nPlease enter your mobile number: "))
            Email = input("\nPlease enter your email address: ")
            Rec1 = [AccNo, Name, Dep, MobileNo, Email]
            Rec.append(Rec1)
            print("\n", Rec1)
            print("\n", Rec)
            f = open("Bank", 'wb+')
            pickle.dump(Rec, f)
            f.close()

            Continue = input(
                "\nDo you want to enter more records? (yes/no) : ").lower()
            if Continue in ['yes', 'y']:
                continue
            elif Continue in ['no', 'n']:
                break

    except ValueError:
        print("\nInvalid Values Entered.")


def Credit():
    try:
        with open("Bank", 'rb+') as f:
            Rec = pickle.load(f)
            acc = int(
                input("\nEnter the account number from which the money is to be credited: "))
            for i in range(0, len(Rec)):
                if Rec[i][0] == acc:
                    Deposit = float(input("\nEnter amount to be added: "))
                    Rec[i][2] += Deposit
                    print("\nAmount Deposited - ", Deposit)
                    break
                else:
                    print("\nRecord not found.")
            f.seek(0)
            pickle.dump(Rec, f)
        f.close()

    except FileNotFoundError:
        print("\nBank File doesn't exist.")


def Balance():
    try:
        f = open("Bank", "rb")
        Bal = pickle.load(f)
        AccNo = int(
            input("\nEnter the account number of which you want to check the balance: "))
        for i in range(0, len(Bal)):
            if Bal[i][0] == AccNo:
                print("\nBalance Amount  - ", Bal[i][2])
                break
            else:
                print("\nRecord not found.")

    except FileNotFoundError:
        print("\nBank File doesn't exist.")


def Withdraw():
    try:
        f = open("Bank", 'rb+')
        Rec = pickle.load(f)
        acc = int(
            input("\nEnter the account number from which the money is to be withdrawn: "))
        for i in range(0, len(Rec)):
            if Rec[i][0] == acc:
                Withdraw = float(input("\nEnter amount to be withdrawn: "))
                Rec[i][2] -= Withdraw
                print("\nAmount Withdrawn - ", Withdraw)
                print("\nYou have", Rec[i][2])
                break
            else:
                print("\nRecord not found.")
        f.seek(0)
        pickle.dump(Rec, f)
        f.close()

    except FileNotFoundError:
        print("\nBank File doesn't exist.")


def AllAcc():
    f = open("Bank", "rb")
    Rec = pickle.load(f)
    for i in range(0, len(Rec)):
        print(Rec[i][1])


def Delete():
    try:
        f = open("Bank", "rb+")
        Rec = pickle.load(f)
        AccNo = int(input(
            "\nPlease enter the Account number of the Account which you want to delete: "))

        for i in range(len(Rec)):
            if Rec[i][0] == AccNo:
                Rec.pop(i)
                print(Rec)
                break
            else:
                print("\nPlease choose an existing account.")

        f.seek(0)
        pickle.dump(Rec, f)
        f.close()

    except FileNotFoundError:
        print("\nFile Doesn't Exist.")


def Update():
    try:
        f = open("Bank", "rb+")
        Rec = pickle.load(f)
        AccNo = int(input(
            "\nPlease enter the Account number of the Account of which you want to update: "))

        for i in range(len(Rec)):
            if Rec[i][0] == AccNo:
                choice = input(
                    "\nDo you want to update this Account. Type 'YES' or 'NO': ")

                if choice == 'YES' or choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'Y':
                    while True:
                        print("\nTo Change: ")
                        print("\n1. Name")
                        print("\n2. Mobile Number")
                        print("\n3. Email")
                        print("\n4. EXIT")
                        print("\nSelect Your Option (1-4) ")
                        ch = input("Enter your choice: ")

                        if ch == '1':
                            Rec[i][1] == input("Enter the new Name: ")
                        elif ch == '2':
                            Rec[i][3] == input("Enter the new Mobile Number: ")
                        elif ch == '3':
                            Rec[i][4] == input("Enter the new Email: ")
                        elif ch == '4':
                            print("\nYour account has been updated.")
                            break
                        else:
                            print("Invalid choice")

                elif choice == 'NO' or choice == 'No' or choice == 'N' or choice == 'n' or choice == 'no':
                    break

    except FileNotFoundError:
        print("\nFile doesn't exist")

# Intro


print('''Welcome to GMN bank
_____________________________
''')

while True:
    print("\nMAIN MENU")
    print("\n1. NEW ACCOUNT")
    print("\n2. DEPOSIT AMOUNT")
    print("\n3. WITHDRAW AMOUNT")
    print("\n4. BALANCE ENQUIRY")
    print("\n5. ALL ACCOUNT HOLDER LIST")
    print("\n6. CLOSE AN ACCOUNT")
    print("\n7. MODIFY AN ACCOUNT")
    print("\n8. EXIT")
    print("\nSelect Your Option (1-8) ")
    ch = input("\nEnter your choice : ")

    if ch == '1':
        CreateNewAcc()
    elif ch == '2':
        Credit()
    elif ch == '3':
        Withdraw()
    elif ch == '4':
        Balance()
    elif ch == '5':
        AllAcc()
    elif ch == '6':
        Delete()
    elif ch == '7':
        Update()
    elif ch == '8':
        print("\nThanks for using bank managemnt system")
        break
    else:
        print("\nInvalid choice")
