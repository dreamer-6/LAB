# The "Bank Vault" - A dictionary to store all accounts
accounts = {}

# --- 1. The Bank Functions ---
def create_account(account_number, balance):
    accounts[account_number] = balance
    print("Account created successfully!")

def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number] += amount
        print("Deposit successful!")
    else:
        print("Error: Account not found.")

def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            print("Withdrawal successful!")
        else:
            print("Error: Insufficient funds.")
    else:
        print("Error: Account not found.")

def check_balance(account_number):
    if account_number in accounts:
        print(f"Account: {account_number} | Balance: ${accounts[account_number]}")
    else:
        print("Error: Account not found.")

# --- 2. The Interactive Menu ---
while True:
    print("\n--- Bank Menu ---")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Quit")
    
    choice = int(input("Enter choice (1-5): "))
    
    if choice == 5:
        print("Goodbye!")
        break
        
    # Ask for the account number for choices 1, 2, 3, and 4
    acc_num = input("Enter account number: ")
    
    if choice == 1:
        bal = float(input("Enter initial balance: "))
        create_account(acc_num, bal)
    elif choice == 2:
        amt = float(input("Enter amount to deposit: "))
        deposit(acc_num, amt)
    elif choice == 3:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(acc_num, amt)
    elif choice == 4:
        check_balance(acc_num)
    else:
        print("Invalid choice. Please try again.")