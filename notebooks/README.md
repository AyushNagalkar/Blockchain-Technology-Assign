# Blockchain Technology - 8 Problems Python Implementation

This folder contains Python implementations of 8 blockchain technology problems, converted from Jupyter notebooks to standalone Python files for easy execution.

## Overview of Problems

### Problem 1: Simple Blockchain with Hashing & Linked Blocks
**File:** `Problem_1_Simple_Blockchain.py`

A basic blockchain implementation that demonstrates:
- SHA-256 hashing of blocks
- Linking blocks using previous hash
- Creating and managing a blockchain

**Run:** `python Problem_1_Simple_Blockchain.py`

**Output:**
```
Simple blockchain with 4 blocks (1 genesis + 3 transaction blocks)
Each block contains hash and reference to previous block
```

---

### Problem 2: Block Verification Function
**File:** `Problem_2_Block_Verification.py`

Implements verification functions to validate chain integrity:
- Verify individual block hashes
- Verify chain links (previous hash matching)
- Detect tampering with blocks
- Validate entire blockchain

**Run:** `python Problem_2_Block_Verification.py`

**Features:**
- Detects when blocks are tampered with
- Shows how tampering breaks the chain
- Validates blockchain integrity

---

### Problem 3: Digital Wallet with Public/Private Keys
**File:** `Problem_3_Digital_Wallet.py`

Creates digital wallets using RSA cryptography:
- Generate public-private key pairs
- Sign messages with private key
- Verify signatures with public key
- Demonstrate non-repudiation

**Run:** `python Problem_3_Digital_Wallet.py`

**Features:**
- 2048-bit RSA encryption
- Digital signatures using SHA-256
- Message authentication
- Tampering detection

---

### Problem 4: Double-Spending Prevention
**File:** `Problem_4_Double_Spending_Prevention.py`

Simulates transactions between wallets with double-spending prevention:
- Create wallets with initial balances
- Process transactions
- Validate sender balance before transaction
- Prevent double-spending

**Run:** `python Problem_4_Double_Spending_Prevention.py`

**Features:**
- Multiple wallet management
- Transaction history tracking
- Double-spending detection
- Balance validation

---

### Problem 5: HelloWorld Smart Contract Deployment
**File:** `Problem_5_HelloWorld_Deploy.py`
**Solidity File:** `HelloWorld_Remix.sol`

Deploy a HelloWorld smart contract on Ethereum test network (Sepolia):
- Contract compilation guide
- Deployment instructions using Remix IDE
- Python helper code to interact with deployed contract

**Setup Instructions:**
1. Get test ETH from Sepolia faucet
2. Open Remix IDE: https://remix.ethereum.org
3. Create file `HelloWorld.sol`
4. Copy code from `HelloWorld_Remix.sol`
5. Compile and deploy on Sepolia network
6. Run the Python script with contract address

**Python Usage:**
```python
deployer = HelloWorldDeployer(RPC_URL, PRIVATE_KEY, WALLET_ADDRESS)
deployer.check_connection()
deployer.interact_with_contract(CONTRACT_ADDRESS)
deployer.get_message()
deployer.set_message("New Message")
```

---

### Problem 6: Token Transfer Between Accounts
**File:** `Problem_6_Token_Transfer.py`
**Solidity File:** `SimpleToken_Remix.sol`

Create and manage a custom ERC20-like token:
- Deploy token contract on Ethereum test network
- Transfer tokens between accounts
- Check token balances
- Validate token transactions

**Setup Instructions:**
1. Get test ETH
2. Deploy `SimpleToken_Remix.sol` using Remix IDE
3. Set initial supply (e.g., 1000 tokens)
4. Use Python script to transfer tokens

**Python Usage:**
```python
token = TokenContract(RPC_URL, PRIVATE_KEY, WALLET_ADDRESS)
token.connect_to_contract(CONTRACT_ADDRESS)
token.get_token_info()
token.get_balance(WALLET_ADDRESS)
token.transfer_tokens(RECEIVER_ADDRESS, 100)
```

---

### Problem 7: Bitcoin Merkle Root Computation
**File:** `Problem_7_Merkle_Root.py`

Analyze Bitcoin block structure and compute Merkle root:
- Create transactions
- Build Merkle tree from transactions
- Compute Merkle root
- Verify transactions using Merkle proofs
- Handle odd number of transactions

**Run:** `python Problem_7_Merkle_Root.py`

**Features:**
- Transaction hashing with double SHA-256
- Binary tree construction
- Merkle proof generation
- Tree visualization
- Audit path calculation

---

### Problem 8: Proof-of-Work Mining
**File:** `Problem_8_Proof_of_Work.py`

Implement Proof-of-Work mining mechanism:
- Mine blocks by finding valid nonces
- Adjust difficulty level
- Verify proof-of-work
- Demonstrate difficulty effect on mining time

**Run:** `python Problem_8_Proof_of_Work.py`

**Features:**
- Configurable difficulty levels
- Mining time measurement
- Chain verification
- Difficulty analysis
- PoW statistics

---

## Installation Requirements

### For Local Python Files (Problems 1-4, 7-8):
```bash
# No external dependencies required for basic functionality
python -V  # Python 3.7 or higher
```

### For Solidity Contracts (Problems 5-6):
```bash
# For local testing/compilation:
pip install web3 py-solc-x

# For Ethereum network interaction:
pip install web3

# For PKI features (Problem 3):
pip install cryptography
```

### For Complete Setup with All Features:
```bash
pip install web3 py-solc-x cryptography
```

---

## Directory Structure

```
Blockchain Technology/
├── Problem_1_Simple_Blockchain.py
├── Problem_2_Block_Verification.py
├── Problem_3_Digital_Wallet.py
├── Problem_4_Double_Spending_Prevention.py
├── Problem_5_HelloWorld_Deploy.py
├── Problem_6_Token_Transfer.py
├── Problem_7_Merkle_Root.py
├── Problem_8_Proof_of_Work.py
├── HelloWorld_Remix.sol
├── SimpleToken_Remix.sol
└── README.md
```

---

## Quick Start Guide

### Run All Basic Problems Locally:
```bash
# Problem 1: Blockchain creation
python Problem_1_Simple_Blockchain.py

# Problem 2: Block verification
python Problem_2_Block_Verification.py

# Problem 3: Digital wallets
python Problem_3_Digital_Wallet.py

# Problem 4: Double-spending prevention
python Problem_4_Double_Spending_Prevention.py

# Problem 7: Merkle root computation
python Problem_7_Merkle_Root.py

# Problem 8: Proof-of-Work mining
python Problem_8_Proof_of_Work.py
```

### Deploy Smart Contracts (Problems 5-6):
1. Visit Remix IDE: https://remix.ethereum.org
2. Create new files with Solidity code
3. Compile and deploy to Sepolia test network
4. Run Python interaction scripts with deployed contract addresses

---

## Key Concepts Covered

### Fundamental Blockchain Concepts:
- ✓ Hashing and hash chains
- ✓ Block structure and linking
- ✓ Chain verification and integrity
- ✓ Digital signatures and authentication
- ✓ Wallets and balance management

### Transaction Management:
- ✓ Transaction creation and validation
- ✓ Double-spending prevention
- ✓ Balance verification
- ✓ Transaction history

### Mining and Consensus:
- ✓ Proof-of-Work algorithm
- ✓ Difficulty adjustment
- ✓ Nonce computation
- ✓ Mining time analysis

### Merkle Trees:
- ✓ Transaction hashing
- ✓ Binary tree construction
- ✓ Merkle root computation
- ✓ Merkle proofs for verification

### Smart Contracts:
- ✓ Contract deployment
- ✓ State management
- ✓ Function calls and transactions
- ✓ Token transfer implementation

---

## Ethereum Test Network Setup

### For Sepolia Network:

1. **Get Test ETH:**
   - Visit: https://www.alchemy.com/faucets/sepolia
   - Enter your wallet address
   - Receive 0.5 test ETH

2. **Get RPC Endpoint:**
   - Infura: https://infura.io (free tier available)
   - Alchemy: https://alchemy.com
   - Ankr: https://ankr.com

3. **Set Up MetaMask:**
   - Install MetaMask extension
   - Add Sepolia network to wallet
   - Import or create wallet

4. **Configure Python Scripts:**
   ```python
   RPC_URL = "https://sepolia.infura.io/v3/YOUR_PROJECT_ID"
   PRIVATE_KEY = "your_private_key"  # Keep this secret!
   WALLET_ADDRESS = "0x..."
   CONTRACT_ADDRESS = "0x..."  # From Remix deployment
   ```

---

## Security Warnings

⚠️ **IMPORTANT:**
- **NEVER** commit private keys to version control
- Use environment variables for sensitive data
- Always test on testnet before mainnet
- Verify contract addresses carefully
- Use hardware wallets for real funds
- Keep private keys offline and secure

---

## Performance Notes

### Mining Difficulty vs. Time:
- Difficulty 1: < 1 second
- Difficulty 2: 1-5 seconds
- Difficulty 3: 5-30 seconds
- Difficulty 4: 30+ seconds

This demonstrates why Bitcoin adjusts difficulty to maintain ~10 minute block time.

---

## Troubleshooting

### Connection Issues:
```bash
# Test Python installation
python -c "from web3 import Web3; print('Web3 installed')"

# Test network connection
python -c "from web3 import Web3; w3 = Web3(); print(w3.is_connected())"
```

### Import Errors:
```bash
# Install missing packages
pip install --upgrade web3 py-solc-x cryptography

# Verify installation
pip list | grep -i web3
```

### Smart Contract Issues:
- Check contract address format (should start with 0x)
- Verify ABI matches deployed contract
- Ensure sufficient test ETH for gas fees
- Check network selection (Sepolia vs. others)

---

## Additional Resources

### Documentation:
- Web3.py: https://web3py.readthedocs.io
- Solidity: https://docs.soliditylang.org
- Ethereum: https://ethereum.org/developers
- Bitcoin: https://developer.bitcoin.org

### Tools:
- Remix IDE: https://remix.ethereum.org
- Etherscan: https://sepolia.etherscan.io (Sepolia explorer)
- MetaMask: https://metamask.io

### Learning Resources:
- Ethereum Development Documentation
- Bitcoin Whitepaper
- Blockchain Security Best Practices

---

## License

This code is provided for educational purposes. Use freely but ensure you understand the blockchain concepts before using in production.

---

## Summary

All 8 problems have been converted from Jupyter notebooks to clean, standalone Python files:
- ✓ Problem 1-4, 7-8: Ready to run locally
- ✓ Problem 5-6: Ready for Remix IDE deployment + Python interaction
- ✓ Complete with documentation and examples
- ✓ Beginner-friendly with detailed comments
- ✓ Security best practices included

Start with Problem 1 and work your way through to understand blockchain technology fundamentals!
