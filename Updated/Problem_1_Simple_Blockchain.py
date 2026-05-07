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
    
    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash[:8]}..., data={self.data})"


class Blockchain:
    """A simple blockchain implementation"""
    
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
    
    def display_chain(self):
        """Display all blocks in the chain"""
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash[:8]}...")
            print(f"  Hash: {block.hash[:8]}...")


# Main execution
if __name__ == "__main__":
    # Create blockchain
    blockchain = Blockchain()
    
    # Add some blocks
    blockchain.add_block("Alice transfers 10 BTC to Bob")
    blockchain.add_block("Bob transfers 5 BTC to Charlie")
    blockchain.add_block("Charlie transfers 2 BTC to David")
    
    # Display the blockchain
    print("=" * 50)
    print("SIMPLE BLOCKCHAIN")
    print("=" * 50)
    blockchain.display_chain()
    
    # Verify integrity
    print("\n" + "=" * 50)
    print("BLOCKCHAIN INTEGRITY")
    print("=" * 50)
    print(f"Total blocks: {len(blockchain.chain)}")
    print(f"Genesis block hash: {blockchain.chain[0].hash[:16]}...")
    print(f"Latest block hash: {blockchain.get_latest_block().hash[:16]}...")


"""
Theory:
A blockchain stores blocks in order.
Each block keeps its own hash and the previous block's hash.
If any block changes, the chain link breaks.
"""
