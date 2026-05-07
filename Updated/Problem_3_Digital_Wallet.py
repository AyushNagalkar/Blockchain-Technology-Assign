import hashlib
import random


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(n**0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def gen_prime(start=100, end=300):
    while True:
        p = random.randrange(start, end)
        if is_prime(p):
            return p


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    return x % m


class RSAKeyPair:
    def __init__(self):
        # small primes for demonstration only
        p = gen_prime(100, 300)
        q = gen_prime(100, 300)
        while q == p:
            q = gen_prime(100, 300)

        self.n = p * q
        phi = (p - 1) * (q - 1)

        # choose e coprime with phi
        e = 3
        while egcd(e, phi)[0] != 1:
            e += 2

        d = modinv(e, phi)

        self.e = e
        self.d = d

    def sign(self, message: str) -> int:
        # sign by hashing message to int then raising to d
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        sig = pow(h, self.d, self.n)
        return sig

    def verify(self, message: str, signature: int) -> bool:
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        recovered = pow(signature, self.e, self.n)
        return recovered == (h % self.n)


if __name__ == "__main__":
    # create two wallets (each wallet holds an RSA keypair and a balance)
    alice = RSAKeyPair()
    bob = RSAKeyPair()

    message = "send 10 btc"
    signature = alice.sign(message)

    print("Alice public key (n,e):", alice.n, alice.e)
    print("Signature valid for Alice:", alice.verify(message, signature))
    print("Signature valid for Bob (should be False):", bob.verify(message, signature))


"""
Theory:
This file implements a minimal RSA keypair (educational only).
Signing: hash the message to an integer and compute sig = hash^d mod n.
Verification: compute sig^e mod n and compare to the message hash (mod n).
Do NOT use this small-PRIME RSA for real security.
"""
