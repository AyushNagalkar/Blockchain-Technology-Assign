import hashlib


class DigitalWallet:
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.key = hashlib.sha256(name.encode()).hexdigest()

    def sign(self, message):
        return hashlib.sha256((message + self.key).encode()).hexdigest()

    def verify(self, message, signature):
        return signature == self.sign(message)


if __name__ == "__main__":
    alice = DigitalWallet("Alice")
    bob = DigitalWallet("Bob")

    message = "send 10 btc"
    signature = alice.sign(message)

    print("Alice key:", alice.key[:16] + "...")
    print("Signature valid for Alice:", alice.verify(message, signature))
    print("Signature valid for Bob:", bob.verify(message, signature))


"""
Theory:
This is a simple wallet simulation.
A message is signed with a hash based key.
The same message and key produce the same signature, so tampering is easy to detect.
"""
