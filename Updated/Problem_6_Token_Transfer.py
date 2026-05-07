from web3 import Web3


SIMPLETOKEN_SOLIDITY = '''
pragma solidity ^0.8.0;

contract SimpleToken {
    mapping(address => uint) public balances;
    uint public totalSupply;
    string public name = "Simple Token";
    string public symbol = "ST";
    uint8 public decimals = 18;

    constructor(uint initialSupply) {
        totalSupply = initialSupply * 10 ** uint256(decimals);
        balances[msg.sender] = totalSupply;
    }

    function transfer(address receiver, uint amount) public returns (bool) {
        require(amount > 0, "Amount must be positive");
        require(balances[msg.sender] >= amount, "Insufficient Balance");

        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        return true;
    }

    function getBalance(address account) public view returns (uint) {
        return balances[account];
    }

    function approve(address spender, uint amount) public returns (bool) {
        // Simplified approval (in real world, would use allowance mapping)
        return true;
    }

    function transferFrom(address sender, address receiver, uint amount) public returns (bool) {
        require(amount > 0, "Amount must be positive");
        require(balances[sender] >= amount, "Insufficient Balance");

        balances[sender] -= amount;
        balances[receiver] += amount;
        return true;
    }
}
'''


class TokenContract:
    def __init__(self, rpc_url, private_key, wallet_address):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.private_key = private_key
        self.wallet_address = wallet_address
        self.contract = None

    def connected(self):
        return self.w3.is_connected()

    def attach(self, contract_address, abi):
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def balance_of(self, address):
        return self.contract.functions.getBalance(address).call()


SIMPLETOKEN_ABI = [
    {"inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint", "name": "", "type": "uint"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "getBalance", "outputs": [{"internalType": "uint", "name": "", "type": "uint"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "receiver", "type": "address"}, {"internalType": "uint", "name": "amount", "type": "uint"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}
]


if __name__ == "__main__":
    print(SIMPLETOKEN_SOLIDITY)


"""
Theory:
The token contract stores balances in a mapping.
The transfer function moves tokens from one address to another.
Deploy in Remix, then connect to the contract address from Python.
"""
