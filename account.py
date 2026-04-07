accounts ={}

def create_account(account_number,balance):
    accounts[account_number] = balance
    print("account created succesfully")

def deposit(account_number,amount):
    if account_number in accounts:
        accounts[account_number] =+ amount
        print("Deposited successfully")
    else:
        print("Error: Account not found")

def withdraw(account_number,amount):
    if account_number in accounts:
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            print("Withdrawal Successful")

        else:
            print("Error: Insufficent fund")
    else:
        print("Error: Account not found")

def check_balance(account_number):
    if account_number in accounts:
        print(f"Account number: {account_number} | Balance: ${accounts[account_number]}")
    else:
        print("Error: Account not found!")


while True:
    print("Bank Operations")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter Your choice: "))

    if choice == 5:
        print("Goodbye!")
        break

    account_no = int(input("Enter account number"))
    
    if choice == 1:
        bal = int(input("Initial Balance: "))
        create_account(account_no,bal)
    elif choice == 2:
        amt = int(input("Enter Amount to deposit: "))
        deposit(account_no,amt)
    elif choice == 3:
        amt = int(input("Enter Amount to withdraw: "))
        withdraw(account_no,amt)
    elif choice == 4:
        check_balance(account_no)

    else:
        print("Invalid Choice")
    
        