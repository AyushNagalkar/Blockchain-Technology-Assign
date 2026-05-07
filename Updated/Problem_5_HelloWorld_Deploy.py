from web3 import Web3


HELLOWORLD_SOLIDITY = '''
pragma solidity ^0.8.0;

contract HelloWorld {
    string public message;

    constructor() {
        message = "Hello, Blockchain!";
    }

    function setMessage(string memory newMessage) public {
        message = newMessage;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }
}
'''


class HelloWorldDeployer:
    def __init__(self, rpc_url, private_key, wallet_address):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.private_key = private_key
        self.wallet_address = wallet_address
        self.contract = None

    def connected(self):
        return self.w3.is_connected()

    def attach(self, contract_address, abi):
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def read_message(self):
        return self.contract.functions.getMessage().call()


HELLOWORLD_ABI = [
    {"inputs": [], "name": "getMessage", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "string", "name": "newMessage", "type": "string"}], "name": "setMessage", "outputs": [], "stateMutability": "nonpayable", "type": "function"}
]


if __name__ == "__main__":
    print(HELLOWORLD_SOLIDITY)


"""
Theory:
The contract stores one message on chain.
Web3 connects to the deployed contract using its address and ABI.
Use Remix for deployment, then read or change the message from Python.
"""
