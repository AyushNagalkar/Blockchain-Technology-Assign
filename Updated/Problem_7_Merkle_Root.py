import hashlib


def sha256(data):
    """Generate SHA-256 hash of data"""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


def double_sha256(data):
    """Double SHA-256 hash (Bitcoin standard)"""
    if isinstance(data, str):
        data = data.encode()
    return sha256(sha256(data))


class Transaction:
    def __init__(self, tx_id, sender, receiver, amount):
        self.tx_id = tx_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.hash = double_sha256(f"{sender}->{receiver}:{amount}")
    
    def __repr__(self):
        return f"TX({self.sender[:4]}...→{self.receiver[:4]}...): {self.amount} BTC"


class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.tree_levels = []
        self.merkle_root = None
        self.compute_merkle_root()
    
    def compute_merkle_root(self):
        print("Computing Merkle Root...")
        print("-" * 70)

        hashes = [tx.hash for tx in self.transactions]
        print(f"\nLevel 0: Transaction Hashes ({len(hashes)} hashes)")
        for i, h in enumerate(hashes):
            print(f"  TX{i}: {h[:32]}...")
        
        self.tree_levels.append(hashes.copy())
        
        level = 1

        while len(hashes) > 1:
            new_level = []

            for i in range(0, len(hashes), 2):
                if i + 1 < len(hashes):
                    combined = hashes[i] + hashes[i + 1]
                else:
                    combined = hashes[i] + hashes[i]

                parent_hash = double_sha256(combined.encode())
                new_level.append(parent_hash)
            
            hashes = new_level
            
            print(f"\nLevel {level}: Parent Hashes ({len(hashes)} hashes)")
            for i, h in enumerate(hashes):
                print(f"  Hash{i}: {h[:32]}...")
            
            self.tree_levels.append(hashes.copy())
            level += 1
        
        self.merkle_root = hashes[0]
        
        print(f"\n{'=' * 70}")
        print(f"Merkle Root: {self.merkle_root}")
        print(f"{'=' * 70}\n")
    
    def verify_transaction(self, tx_index):
        if tx_index < 0 or tx_index >= len(self.transactions):
            return False

        tx_hash = self.transactions[tx_index].hash
        return tx_hash in self.tree_levels[0]
    
    def display_tree_structure(self):
        print("\n" + "=" * 70)
        print("MERKLE TREE STRUCTURE")
        print("=" * 70)
        
        for level_idx, level in enumerate(self.tree_levels):
            print(f"\nLevel {level_idx}: {len(level)} hash(es)")
            for i, h in enumerate(level):
                print(f"  [{i}] {h[:48]}...")
    
    def get_audit_path(self, tx_index):
        print(f"\nMerkle Proof for TX{tx_index}:")
        print("-" * 70)
        
        index = tx_index
        path = []
        
        for level_idx in range(len(self.tree_levels) - 1):
            level = self.tree_levels[level_idx]
            
            if index % 2 == 0:
                sibling_index = index + 1 if index + 1 < len(level) else index
            else:
                sibling_index = index - 1
            
            sibling_hash = level[sibling_index]
            path.append({
                'level': level_idx,
                'sibling_index': sibling_index,
                'sibling_hash': sibling_hash
            })
            
            print(f"  Level {level_idx}: Use sibling at index {sibling_index}")
            print(f"    {sibling_hash[:48]}...")
            
            index = index // 2
        
        return path


class BitcoinBlock:
    def __init__(self, block_number, transactions, previous_block_hash="0"):
        self.block_number = block_number
        self.transactions = transactions
        self.previous_block_hash = previous_block_hash
        self.timestamp = None
        self.nonce = 0
        
        self.merkle_tree = MerkleTree(transactions)
        self.merkle_root = self.merkle_tree.merkle_root
        self.block_hash = self.compute_block_hash()
    
    def compute_block_hash(self):
        block_header = f"{self.block_number}{self.previous_block_hash}{self.merkle_root}"
        return double_sha256(block_header)
    
    def display_block_info(self):
        print("\n" + "=" * 70)
        print(f"BITCOIN BLOCK #{self.block_number}")
        print("=" * 70)
        
        print(f"\nBlock Header:")
        print(f"  Block Number: {self.block_number}")
        print(f"  Previous Block Hash: {self.previous_block_hash[:32]}...")
        print(f"  Merkle Root: {self.merkle_root[:32]}...")
        print(f"  Block Hash: {self.block_hash[:32]}...")
        print(f"  Transaction Count: {len(self.transactions)}")
        
        print(f"\nTransactions:")
        for i, tx in enumerate(self.transactions):
            print(f"  {i}. {tx}")


# Main execution
if __name__ == "__main__":
    print("\nCreating sample transactions...")
    transactions = [
        Transaction("tx1", "Alice", "Bob", 10),
        Transaction("tx2", "Bob", "Charlie", 5),
        Transaction("tx3", "Charlie", "Dave", 2),
        Transaction("tx4", "Dave", "Eve", 1)
    ]
    
    block = BitcoinBlock(1, transactions, "0000abc123def456")
    block.display_block_info()
    block.merkle_tree.display_tree_structure()
    block.merkle_tree.get_audit_path(0)

    print("\n" + "=" * 70)
    print("TEST: ODD NUMBER OF TRANSACTIONS")
    print("=" * 70)
    
    odd_transactions = [
        Transaction("tx1", "Alice", "Bob", 10),
        Transaction("tx2", "Bob", "Charlie", 5),
        Transaction("tx3", "Charlie", "Dave", 2)
    ]
    
    block2 = BitcoinBlock(2, odd_transactions, block.block_hash)
    block2.display_block_info()
    block2.merkle_tree.display_tree_structure()


"""
Theory:
Bitcoin uses a Merkle tree to compress many transaction hashes into one root.
Each pair of hashes is combined until only one hash remains.
Changing one transaction changes the final root.
"""
