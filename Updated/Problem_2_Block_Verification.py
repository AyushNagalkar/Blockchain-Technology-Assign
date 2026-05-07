import hashlib


def sha256(data):
    """Generate SHA-256 hash of data"""
    return hashlib.sha256(data.encode()).hexdigest()


class Block:
    """A block in the blockchain"""
    
    def __init__(self, index, previous_hash, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        """Compute the hash of the block"""
        block_data = f"{self.index}{self.previous_hash}{self.data}{self.nonce}"
        return sha256(block_data)
    
    def verify_block(self):
        """Verify if the block's hash is correctly computed"""
        calculated_hash = self.compute_hash()
        return calculated_hash == self.hash


class Blockchain:
    """A blockchain with verification capabilities"""
    
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Create the first block in the blockchain"""
        genesis_block = Block(0, "0", "Genesis Block")
        self.chain.append(genesis_block)
    
    def get_latest_block(self):
        """Get the last block in the chain"""
        return self.chain[-1]
    
    def add_block(self, data):
        """Add a new block to the blockchain"""
        previous_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            previous_hash=previous_block.hash,
            data=data
        )
        self.chain.append(new_block)
        return new_block
    
    def verify_block_hash(self, block_index):
        """Verify if a specific block's hash is valid"""
        if block_index < 0 or block_index >= len(self.chain):
            return False
        
        block = self.chain[block_index]
        return block.verify_block()
    
    def verify_chain_link(self, block_index):
        """Verify if a block's previous_hash matches the previous block's hash"""
        if block_index == 0:
            return self.chain[0].previous_hash == "0"
        
        if block_index < 0 or block_index >= len(self.chain):
            return False
        
        current_block = self.chain[block_index]
        previous_block = self.chain[block_index - 1]
        
        return current_block.previous_hash == previous_block.hash
    
    def verify_entire_chain(self):
        """Verify the integrity of the entire blockchain"""
        print("Verifying entire blockchain...")
        print("-" * 50)
        
        all_valid = True
        
        for i, block in enumerate(self.chain):
            hash_valid = self.verify_block_hash(i)
            link_valid = self.verify_chain_link(i)
            
            status = "✓ VALID" if (hash_valid and link_valid) else "✗ INVALID"
            print(f"Block #{i}: {status}")
            
            if not hash_valid:
                print(f"  - Hash verification failed!")
                all_valid = False
            
            if not link_valid:
                print(f"  - Chain link verification failed!")
                all_valid = False
        
        print("-" * 50)
        return all_valid
    
    def tamper_block(self, block_index, new_data):
        """Simulate tampering with a block"""
        if 0 <= block_index < len(self.chain):
            self.chain[block_index].data = new_data
            print(f"Block #{block_index} has been tampered with!")
    
    def display_chain(self):
        """Display all blocks in the chain"""
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash[:16]}...")
            print(f"  Hash: {block.hash[:16]}...")


# Main execution
if __name__ == "__main__":
    # Create blockchain
    blockchain = Blockchain()
    
    # Add some blocks
    blockchain.add_block("Alice transfers 10 BTC to Bob")
    blockchain.add_block("Bob transfers 5 BTC to Charlie")
    blockchain.add_block("Charlie transfers 2 BTC to David")
    
    print("=" * 50)
    print("BLOCKCHAIN WITH VERIFICATION")
    print("=" * 50)
    
    # Display the blockchain
    blockchain.display_chain()
    
    # Verify chain integrity - should be valid
    print("\n" + "=" * 50)
    print("VERIFICATION TEST 1: Valid Chain")
    print("=" * 50)
    is_valid = blockchain.verify_entire_chain()
    print(f"Chain Status: {'VALID ✓' if is_valid else 'INVALID ✗'}\n")
    
    # Tamper with a block
    print("=" * 50)
    print("TAMPERING WITH BLOCK #1")
    print("=" * 50)
    blockchain.tamper_block(1, "Hacker transfers 1000 BTC to Hacker")
    
    # Verify chain integrity - should be invalid
    print("\n" + "=" * 50)
    print("VERIFICATION TEST 2: Tampered Chain")
    print("=" * 50)
    is_valid = blockchain.verify_entire_chain()
    print(f"Chain Status: {'VALID ✓' if is_valid else 'INVALID ✗'}\n")
    
    # Display tampered chain
    blockchain.display_chain()
    
    print("\n" + "=" * 50)
    print("CONCLUSION")
    print("=" * 50)
    print("Any tampering with block data breaks the chain")
    print("The next block's hash won't match because the previous_hash changed")
    print("This ensures blockchain immutability and security!")


"""
Theory:
Verification checks two things.
First, a block hash must match its data.
Second, each block must point to the previous block correctly.
If either check fails, the chain is invalid.
"""
