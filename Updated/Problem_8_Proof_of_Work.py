import hashlib
import time


def sha256(data):
    """Generate SHA-256 hash of data"""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


class Block:
    def __init__(self, index, previous_hash, data, difficulty=1):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = None
        self.timestamp = time.time()
        self.mining_time = 0
    
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.nonce}{self.timestamp}"
        return sha256(block_string)
    
    def mine_block(self):
        print(f"\nMining Block #{self.index}...")
        print(f"Difficulty: {self.difficulty} (require {self.difficulty} leading zeros)")
        print("-" * 70)
        
        target = "0" * self.difficulty
        start_time = time.time()
        attempts = 0
        
        while True:
            self.hash = self.calculate_hash()
            attempts += 1

            if self.hash.startswith(target):
                self.mining_time = time.time() - start_time
                print(f"\n✓ Block Mined Successfully!")
                print(f"  Nonce: {self.nonce}")
                print(f"  Hash: {self.hash}")
                print(f"  Attempts: {attempts:,}")
                print(f"  Time taken: {self.mining_time:.2f} seconds")
                return True
            
            self.nonce += 1

            if attempts % 10000 == 0:
                print(f"  Attempts: {attempts:,} | Current Hash: {self.hash[:16]}...")
    
    def verify_block(self):
        target = "0" * self.difficulty
        calculated_hash = self.calculate_hash()
        
        if calculated_hash != self.hash:
            return False, "Hash mismatch"
        
        if not self.hash.startswith(target):
            return False, f"Hash does not meet difficulty requirement"
        
        return True, "Block is valid"
    
    def __repr__(self):
        return f"Block(#{self.index}, Hash: {self.hash[:16]}..., Nonce: {self.nonce})"


class ProofOfWorkBlockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()
    
    def create_genesis_block(self):
        print("Creating Genesis Block...")
        genesis_block = Block(0, "0", "Genesis Block", self.difficulty)
        genesis_block.mine_block()
        self.chain.append(genesis_block)
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            previous_hash=previous_block.hash,
            data=data,
            difficulty=self.difficulty
        )
        
        new_block.mine_block()
        self.chain.append(new_block)
        return new_block
    
    def verify_chain(self):
        print("\n" + "=" * 70)
        print("VERIFYING BLOCKCHAIN")
        print("=" * 70)
        
        for i, block in enumerate(self.chain):
            is_valid, message = block.verify_block()
            
            if not is_valid:
                print(f"✗ Block #{i} is INVALID: {message}")
                return False
            
            if i > 0:
                if block.previous_hash != self.chain[i-1].hash:
                    print(f"✗ Block #{i} chain link is broken!")
                    return False
            
            print(f"✓ Block #{i} is valid (PoW: {block.hash[:16]}...)")
        
        print("✓ Entire blockchain is valid!")
        return True
    
    def display_chain(self):
        print("\n" + "=" * 70)
        print("BLOCKCHAIN")
        print("=" * 70)
        
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash[:16]}...")
            print(f"  Hash: {block.hash}")
            print(f"  Nonce: {block.nonce}")
            print(f"  Difficulty: {block.difficulty}")
            print(f"  Mining Time: {block.mining_time:.2f}s")


def demonstrate_difficulty_effect():
    print("\n" + "=" * 70)
    print("DIFFICULTY EFFECT ON MINING TIME")
    print("=" * 70)
    
    data = "Test Transaction"
    
    for difficulty in range(1, 6):
        print(f"\n{'─' * 70}")
        print(f"Difficulty: {difficulty}")
        print(f"{'─' * 70}")
        
        block = Block(0, "0", data, difficulty)
        block.mine_block()
    
    print("\n" + "=" * 70)
    print("KEY OBSERVATION:")
    print("═" * 70)
    print("""
Higher difficulty = More leading zeros required
More zeros required = Fewer valid hashes
Fewer valid hashes = More attempts needed
More attempts = More time to mine

This is the basis of Proof-of-Work:
- Miners must spend computational resources
- The difficulty can be adjusted to maintain consistent block time
- It's computationally expensive to attack (create false blocks)
- But easy to verify (just check the leading zeros)
    """)


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("PROOF-OF-WORK BLOCKCHAIN MINING")
    print("=" * 70)
    
    print("\nCreating blockchain with difficulty level 2...")
    blockchain = ProofOfWorkBlockchain(difficulty=2)
    
    print("\n" + "=" * 70)
    print("ADDING BLOCKS TO BLOCKCHAIN")
    print("=" * 70)
    
    blockchain.add_block("Alice transfers 50 BTC to Bob")
    blockchain.add_block("Bob transfers 30 BTC to Charlie")
    blockchain.add_block("Charlie transfers 20 BTC to Dave")
    
    blockchain.display_chain()
    blockchain.verify_chain()

    print("\n" + "=" * 70)
    print("BLOCKCHAIN STATISTICS")
    print("=" * 70)
    
    total_mining_time = sum(block.mining_time for block in blockchain.chain)
    avg_mining_time = total_mining_time / len(blockchain.chain)
    
    print(f"Total Blocks: {len(blockchain.chain)}")
    print(f"Total Mining Time: {total_mining_time:.2f} seconds")
    print(f"Average Mining Time: {avg_mining_time:.2f} seconds")
    print(f"Difficulty Level: {blockchain.difficulty}")
    
    demonstrate_difficulty_effect()

    print("\n" + "=" * 70)
    print("PROOF-OF-WORK EXPLANATION")
    print("=" * 70)
    print("""
🔍 What is Proof-of-Work?

A consensus mechanism where miners solve computational puzzles to:
1. Validate transactions
2. Create new blocks
3. Secure the network

🔒 How Does It Work?

1. PUZZLE: Find a nonce that produces a hash starting with N zeros
2. EFFORT: Requires many attempts (computational work)
3. VERIFICATION: Easy to verify (just check the leading zeros)
4. REWARD: Miner who finds it first gets rewards

⚙️ Key Properties:

- Difficult to compute (work required)
- Easy to verify (just check hash format)
- Adjustable difficulty (maintain 10-min block time)
- Prevents double-spending and spam
- Makes blockchain immutable

🌍 Used By:
- Bitcoin: ~10 minute average block time
- Ethereum (pre-merge): Similar PoW system
- Many other cryptocurrencies

⚠️  Challenges:
- High energy consumption
- Expensive mining hardware
- Centralization risk (large mining pools)
- Environmental concerns

This is why newer systems use alternatives like:
- Proof of Stake (PoS) - less energy intensive
- Proof of Authority (PoA) - more centralized but efficient
    """)


"""
Theory:
Proof-of-Work means trying nonces until the hash matches the difficulty.
More difficulty means more attempts.
Verification is easy once the hash is found.
"""
