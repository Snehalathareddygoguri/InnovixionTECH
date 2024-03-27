class BankAccountManagement:
    #Initializatons for our bank account management
    def __init__(self, bankacc_holder, init_balance=0):
        self.bankacc_holder=bankacc_holder
        self.bal_amnt=init_balance
    #Displays the balance in our account
    def show_balance(self):
        print(f"Account Balance for {self.bankacc_holder}: ${self.bal_amnt:.2f}")
    #Function for depositing the amount in bank account
    def deposit_money(self, amount):
        if amount>0:
            self.bal_amnt+=amount
            print(f"Deposited Amount:${amount:.2f} into {self.bankacc_holder}'s account.")
            self.show_balance()
        else:
            print("Invalid deposit amount!! Please enter a correct value!!")
    #Function for money withdrawal from bank account
    def withdraw_amount(self, amount):
        if 0<amount<=self.bal_amnt:
            self.bal_amnt-=amount
            print(f"Withdraw Amount:${amount:.2f} from {self.bankacc_holder}'s accouunt.")
            self.show_balance()
        else:
            print("Invalid withdrawl amount !!Check Balance and try again!!")
#Main function which takes the user inputs..and calls the function for our selected inputs
if __name__=="__main__":
    bankacc_holder=input("Enter account holder's name: ")
    init_balance=float(input("Enter initial amount available in bank account: "))
    account=BankAccountManagement(bankacc_holder, init_balance)
    while True:
        print("\nOptions:")
        print("1. Check Account Balance:")
        print("2. Deposit:")
        print("3. Withdrawl:")
        print("4.Exit")
        option=input("Enter your option(1-4): ")
        #Nested if loop for checking input options and calls functions according to our option
        if option == '1':
            account.show_balance()
        elif option == '2':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit_money(amount)
        elif option == '3':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw_amount(amount)
        elif option == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose correct option..!!")