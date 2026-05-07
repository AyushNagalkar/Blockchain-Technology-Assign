import hashlib


def sha256(data):
    """Generate SHA-256 hash of data"""
    return hashlib.sha256(data.encode()).hexdigest()


class Wallet:
    """A simple wallet with balance tracking"""
    
    def __init__(self, name, initial_balance=100):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []
    
    def add_transaction(self, transaction_info):
        """Record a transaction in history"""
        self.transaction_history.append(transaction_info)
    
    def __repr__(self):
        return f"{self.name} | Balance: {self.balance} BTC"


class Transaction:
    """A blockchain transaction"""
    
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = self.sign_transaction()
        self.timestamp = None
    
    def sign_transaction(self):
        """Create a simple hash signature for the transaction"""
        data = f"{self.sender.name}{self.receiver.name}{self.amount}"
        return sha256(data)
    
    def __repr__(self):
        return f"{self.sender.name} -> {self.receiver.name}: {self.amount} BTC"


class SimpleBlockchain:
    """A blockchain that validates transactions and prevents double-spending"""
    
    def __init__(self):
        self.transactions = []
        self.failed_transactions = []
    
    def validate_transaction(self, transaction):
        """
        Validate a transaction:
        1. Check if sender has sufficient balance
        2. Check if amount is positive
        3. Prevent double-spending
        """
        # Check positive amount
        if transaction.amount <= 0:
            return False, "Amount must be positive"
        
        # Check sufficient balance
        if transaction.sender.balance < transaction.amount:
            return False, "Insufficient balance (Double-spending prevented!)"
        
        return True, "Valid transaction"
    
    def add_transaction(self, transaction):
        """
        Add a transaction to the blockchain if it's valid
        Updates wallet balances if transaction is successful
        """
        is_valid, message = self.validate_transaction(transaction)
        
        if is_valid:
            # Process the transaction
            transaction.sender.balance -= transaction.amount
            transaction.receiver.balance += transaction.amount
            
            # Record in history
            transaction.sender.add_transaction(f"Sent {transaction.amount} BTC to {transaction.receiver.name}")
            transaction.receiver.add_transaction(f"Received {transaction.amount} BTC from {transaction.sender.name}")
            
            # Add to blockchain
            self.transactions.append(transaction)
            
            print(f"✓ Transaction Successful: {transaction}")
            return True
        else:
            # Record failed transaction
            self.failed_transactions.append((transaction, message))
            print(f"✗ Transaction Failed: {transaction}")
            print(f"  Reason: {message}")
            return False
    
    def get_balance(self, wallet):
        """Get current balance of a wallet"""
        return wallet.balance
    
    def display_transactions(self):
        """Display all successful transactions"""
        print("\n" + "=" * 60)
        print("TRANSACTION HISTORY (Successful)")
        print("=" * 60)
        for i, tx in enumerate(self.transactions, 1):
            print(f"{i}. {tx}")
            print(f"   Signature: {tx.signature[:16]}...")
    
    def display_failed_transactions(self):
        """Display all failed transactions"""
        if not self.failed_transactions:
            return
        
        print("\n" + "=" * 60)
        print("FAILED TRANSACTIONS")
        print("=" * 60)
        for i, (tx, reason) in enumerate(self.failed_transactions, 1):
            print(f"{i}. {tx}")
            print(f"   Reason: {reason}")


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("TRANSACTION SYSTEM WITH DOUBLE-SPENDING PREVENTION")
    print("=" * 60)
    
    # Create wallets
    print("\n" + "=" * 60)
    print("STEP 1: CREATE WALLETS")
    print("=" * 60)
    
    alice = Wallet("Alice", 100)
    bob = Wallet("Bob", 100)
    charlie = Wallet("Charlie", 100)
    
    print(f"{alice}")
    print(f"{bob}")
    print(f"{charlie}")
    
    # Create blockchain
    blockchain = SimpleBlockchain()
    
    # Test 1: Valid transaction
    print("\n" + "=" * 60)
    print("TEST 1: VALID TRANSACTION")
    print("=" * 60)
    
    tx1 = Transaction(alice, bob, 50)
    blockchain.add_transaction(tx1)
    
    print(f"\nWallet Status After Transaction:")
    print(f"{alice}")
    print(f"{bob}")
    
    # Test 2: Valid transaction from Bob
    print("\n" + "=" * 60)
    print("TEST 2: ANOTHER VALID TRANSACTION")
    print("=" * 60)
    
    tx2 = Transaction(bob, charlie, 30)
    blockchain.add_transaction(tx2)
    
    print(f"\nWallet Status After Transaction:")
    print(f"{alice}")
    print(f"{bob}")
    print(f"{charlie}")
    
    # Test 3: Double-spending attempt (Alice only has 50 left)
    print("\n" + "=" * 60)
    print("TEST 3: DOUBLE-SPENDING ATTEMPT")
    print("=" * 60)
    print("Alice tries to send 70 BTC to Charlie but only has 50 BTC")
    
    tx3 = Transaction(alice, charlie, 70)
    blockchain.add_transaction(tx3)
    
    print(f"\nWallet Status (Unchanged):")
    print(f"{alice}")
    print(f"{bob}")
    print(f"{charlie}")
    
    # Test 4: Negative amount (invalid)
    print("\n" + "=" * 60)
    print("TEST 4: INVALID TRANSACTION (Negative Amount)")
    print("=" * 60)
    
    tx4 = Transaction(bob, alice, -10)
    blockchain.add_transaction(tx4)
    
    # Test 5: Another double-spending attempt
    print("\n" + "=" * 60)
    print("TEST 5: ANOTHER DOUBLE-SPENDING ATTEMPT")
    print("=" * 60)
    print("Bob tries to send 100 BTC to Alice but only has 70 BTC")
    
    tx5 = Transaction(bob, alice, 100)
    blockchain.add_transaction(tx5)
    
    # Display results
    blockchain.display_transactions()
    blockchain.display_failed_transactions()
    
    # Summary
    print("\n" + "=" * 60)
    print("FINAL WALLET BALANCES")
    print("=" * 60)
    print(f"{alice}")
    print(f"{bob}")
    print(f"{charlie}")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"""
✓ Total Successful Transactions: {len(blockchain.transactions)}
✓ Failed Transactions: {len(blockchain.failed_transactions)}
✓ Double-spending attempts were prevented!

Key Features:
1. Each wallet maintains a balance
2. Transactions are validated before processing
3. Insufficient balance automatically rejects the transaction
4. Double-spending is impossible in this system
5. Transaction history is maintained for both sender and receiver

This is the fundamental security mechanism of blockchain systems!
    """)


"""
Theory:
A wallet must spend only what it has.
Before a transaction is accepted, the sender balance is checked.
This prevents the same funds from being used twice.
"""
