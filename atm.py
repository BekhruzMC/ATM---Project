class ATM:
    def __init__(self, balance, password):
        self.balance = balance
        self.password = password
    
    def check_balance(self):
        password = int(input("Please enter your password : "))
        if password == self.password:
            print(f"Your current balance as follows : {self.balance} $")
        else:
            print("Password is incorrect. Please try again!")
    
    def deposit(self):
        password = int(input("Please enter your password : "))
        if password == self.password:
            amount = float(input("Enter the amount of your deposit please : "))
            self.balance += amount
            print(f"You have deposited {amount} $. Balance updated, your balance is {self.balance} $")
        else:
            print("Password is incorrect. Please try again!")
        
    def withdraw(self):
        password = int(input("Please enter your password : "))
        if password == self.password:
            amount = float(input("Enter the amount of your withdraw please : "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have withdrawn {amount} $. Balance updated, your balance is {self.balance} $")
            else:
                print("Insufficient funds!")
        else:
            print("Password is incorrect. Please  try again!")
    
    def exit(self):
        print("Thank you for using our Bank services. Have a great day!")

bank = ATM(1000, 1234)

while True:
    print("Welcome to the Bank service!")
    print("Please select one of the sections!")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice please (1-4) : "))

    if choice == 1:
        bank.check_balance()
    elif choice == 2:
        bank.deposit()
    elif choice == 3:
        bank.withdraw()
    elif choice == 4:
        bank.exit()
        break
    else:
        print("Invalid choice. Please enter the valid choice!")
