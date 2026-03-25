# ============================================================
# BANK ACCOUNT EXERCISE
# Topics: Inheritance, Classes, Exception Handling
# ============================================================

# ============================================================
# PART I: BankAccount Class
# ============================================================

class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False
    
    def authenticate(self, username, password):
        """Verify credentials and set authenticated flag"""
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False
    
    def deposit(self, amount):
        """Add money to account"""
        if not self.authenticated:
            raise Exception("You must be logged in to deposit!")
        
        if amount <= 0:
            raise Exception("Deposit amount must be positive!")
        
        self.balance += amount
        print(f"✅ Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Remove money from account"""
        if not self.authenticated:
            raise Exception("You must be logged in to withdraw!")
        
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive!")
        
        if amount > self.balance:
            raise Exception("Insufficient funds!")
        
        self.balance -= amount
        print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        """Return current balance"""
        if not self.authenticated:
            raise Exception("You must be logged in to check balance!")
        return self.balance


# ============================================================
# PART II: MinimumBalanceAccount (Inherits from BankAccount)
# ============================================================

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        """Override withdraw to check minimum balance"""
        if not self.authenticated:
            raise Exception("You must be logged in to withdraw!")
        
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive!")
        
        # Check if balance would go below minimum
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw! Balance must stay above ${self.minimum_balance}")
        
        self.balance -= amount
        print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")


# ============================================================
# PART IV: ATM Class
# ============================================================

class ATM:
    def __init__(self, account_list, try_limit):
        # Validate account_list
        if not isinstance(account_list, list):
            raise Exception("account_list must be a list!")
        
        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise Exception("All accounts must be BankAccount or MinimumBalanceAccount instances!")
        
        # Validate try_limit
        if not isinstance(try_limit, (int, float)) or try_limit <= 0:
            print("⚠️ Invalid try_limit! Setting to default: 2")
            try_limit = 2
        
        self.account_list = account_list
        self.try_limit = int(try_limit)
        self.current_tries = 0
        
        # Start the ATM
        self.show_main_menu()
    
    def show_main_menu(self):
        """Display main menu for login or exit"""
        while True:
            print("\n" + "=" * 40)
            print("🏧 ATM MAIN MENU")
            print("=" * 40)
            print("1. Log in")
            print("2. Exit")
            
            choice = input("Select option (1-2): ").strip()
            
            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                self.log_in(username, password)
            elif choice == "2":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid option!")
    
    def log_in(self, username, password):
        """Authenticate user and show account menu"""
        # Try to find matching account
        for account in self.account_list:
            if account.authenticate(username, password):
                print(f"\n✅ Welcome, {username}!")
                self.current_tries = 0  # Reset tries on success
                self.show_account_menu(account)
                return
        
        # No match found
        self.current_tries += 1
        remaining = self.try_limit - self.current_tries
        
        if self.current_tries >= self.try_limit:
            print(f"\n🚫 Maximum tries ({self.try_limit}) reached! Shutting down.")
            exit()
        else:
            print(f"\n❌ Invalid credentials! Tries remaining: {remaining}")
    
    def show_account_menu(self, account):
        """Show account operations after login"""
        while True:
            print("\n" + "=" * 40)
            print(f"💰 ACCOUNT MENU - {account.username}")
            print("=" * 40)
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Log out")
            
            # Show account type
            if isinstance(account, MinimumBalanceAccount):
                print(f"   [Min Balance Account - Min: ${account.minimum_balance}]")
            
            choice = input("Select option (1-4): ").strip()
            
            try:
                if choice == "1":
                    amount = float(input("Enter deposit amount: $"))
                    account.deposit(amount)
                
                elif choice == "2":
                    amount = float(input("Enter withdrawal amount: $"))
                    account.withdraw(amount)
                
                elif choice == "3":
                    balance = account.get_balance()
                    print(f"💵 Current balance: ${balance}")
                
                elif choice == "4":
                    account.authenticated = False  # Log out
                    print("👋 Logged out successfully!")
                    break
                
                else:
                    print("❌ Invalid option!")
            
            except Exception as e:
                print(f"❌ Error: {e}")


# ============================================================
# TESTING THE CODE
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🏦 BANK ACCOUNT SYSTEM - TESTING")
    print("=" * 60)
    
    # Create test accounts
    account1 = BankAccount("alice", "1234", 1000)
    account2 = MinimumBalanceAccount("bob", "5678", 500, minimum_balance=100)
    account3 = BankAccount("charlie", "9999", 200)
    
    # Start ATM
    atm = ATM([account1, account2, account3], try_limit=3)