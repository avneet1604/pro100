class Atm:
    def __init__(self,cardNum,pin):
        self.cardNum = cardNum
        self.pin = pin
    
    def checkBalance(self):
        print("YOUR BALANCE IS 100000")

    def withdraw(self,amount):
        newAmount = 100000 - amount
        print("YOU HAVE WITHDRAWN "+str(amount)+". CURRENT BALANCE IS "+str(newAmount))

def main():
    card_Num = input("Enter your Card number: ")
    pin_num = input("Enter your Pin number: ")
    newUser = Atm(card_Num,pin_num)
    print("Choose your activity:")
    print("1. Balance Enquiry  2. Withdrawl Amount")
    activity = int(input("Enter activity number:"))
    
    if(activity == 1):
        newUser.checkBalance()
    elif(activity == 2):
        amount = int(input("Enter Withdrawl amount: "))
        newUser.withdraw(amount)
    else:
        print("Enter a valid activity number: ")

if __name__ == "__main__":
    main()
