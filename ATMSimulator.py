import time
from datetime import datetime
import pickle as p

UserData ={}
def create_acc():
    UserName = input("Username: ")
    Password = input("Password: ")
    Money = float(input("Enter initial deposite amount (>10000): "))
    UserData["UserName"] = UserName
    UserData["Password"] = Password
    UserData["Money"] = Money
    with open("atmData.dat","ab") as file:
        p.dump(UserData,file)
    
    print("\nAccount Created Successful:")
    print("Saved Data", UserData, "\n")

def Withdraw():
    UserName = input("Enter Username: ")
    Password = input("Enter Password: ")
    WithdAmount = float(input("Withdrawal Amount: "))
    amount, trans_type = Banking(UserName, Password, WithdAmount, operation="withdraw")
    return UserName, amount, trans_type

def Deposit():
    UserName = input("Enter Username: ")
    Password = input("Enter Password: ")
    DepoAmount = float(input("Deposit amount: "))
    amount, trans_type = Banking(UserName, Password, DepoAmount, operation="deposit")
    return UserName, amount, trans_type

def loading(n,m=0.5):
    for i in range(n):
        print(".", end = "")
        time.sleep(m)
    print("Done")

new = 0
#Banking
def Banking(UserName, Password, Amount=0, operation="deposit"):
    for i in range(3):
        if UserName in UserData.values():
            for a in range(3):
                if Password == UserData["Password"]:
                    loading(3,0.3)
                    if operation == "withdraw":
                        if Amount <= UserData["Money"]:
                            UserData["Money"] -= Amount
                            print("Withdrawal successful.")
                            return Amount, "Withdrawal"
                        else:
                            print("No Sufficient Amount")
                            print("Balance is only: ", UserData["Money"])
                            return 0, "Failed"
                    elif operation == "deposit":
                        UserData["Money"] += Amount
                        print("Deposit successful.")
                        return Amount, "Deposit"
                    return 0, "Failed"
                else:
                    print("Passowrd is Incorrect")
                    if operation == "deposit":
                        Deposit()
                    elif operation == "withdraw":
                        Withdraw()
                    if i == 2:
                        print("ACCESS IS BLOCKED DUE TO MULITPLE INCORRECT PASSWORDS")
                        print("")
            break
        else:
            print("Invalid Account")
            print("Please try again")
            print()
            if operation == "deposit":
                Deposit()
            elif operation == "withdraw":
                Withdraw()
            if i == 2:
                print("ACCESS IS BLOCKED!")



print("\t\t HDFC Bank")
print("""
What would you like to perform?
    1. Deposit
    2. Withdraw
    3. Create Account
    4. Exit
""")

WorD = int(input("Choose 1/2/3/4: "))
time.sleep(1)
UserName = ""
amount = 0
trans_type = ""
if WorD == 1:
    UserName, amount, trans_type = Deposit()
elif WorD == 2:
    UserName, amount, trans_type = Withdraw()
elif WorD == 3:
    create_acc()
else:
    print("Thank You")

#Receipt
print("Processing the Receipt",end = "")
loading(5)
time.sleep(2)
print()
print("\t\t HDFC Bank")
print("\t\t","RECEIPT")
Dt = datetime.now()           # Current Date and Time
print("Date and Time: ",Dt)
print()
print("User Name: ", UserName)
print("Amount of Deposit or Withdrawal: ",new)
print()
print()
