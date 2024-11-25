class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit Successful! New Balance: ${self.balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal Successful! Remaining Balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive value.")

    def view_account_details(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}\n")


def bank_management_system():
    print("Welcome to the Bank Management System!\n")
    accounts = {}

    while True:
        print("Options:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        print("")

        if choice == "1":
            account_number = input("Enter Account Number: ").strip()
            if account_number in accounts:
                print("An account with this number already exists.\n")
                continue
            account_holder = input("Enter Account Holder's Name: ").strip()
            initial_deposit = float(input("Enter Initial Deposit Amount: "))
            accounts[account_number] = BankAccount(account_number, account_holder, initial_deposit)
            print(f"Account Created Successfully for {account_holder}!\n")

        elif choice == "2":
            account_number = input("Enter Account Number: ").strip()
            if account_number in accounts:
                amount = float(input("Enter Amount to Deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.\n")

        elif choice == "3":
            account_number = input("Enter Account Number: ").strip()
            if account_number in accounts:
                amount = float(input("Enter Amount to Withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.\n")

        elif choice == "4":
            account_number = input("Enter Account Number: ").strip()
            if account_number in accounts:
                accounts[account_number].view_account_details()
            else:
                print("Account not found.\n")

        elif choice == "5":
            print("Thank you for using the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


# Run the Bank Management System
bank_management_system()
