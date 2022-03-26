import random

def generate_private_key(n, g):
    # Random number fro Alice where x<n-1
    x = random.randint(1, n)
    # Random number fro Bob where x<n-1
    y = random.randint(1, n)
    # Calculate g^x mod n which is Alice's key
    k1 = pow(g, x, n)
    # Calculate g^y mod n which is Bob's key
    k2 = pow(g, y, n)

    # If an attacker wants to get x and y (private keys) 
    # Which is the discrete logarithm problem it is an exponentially slow process 
    print("Alice's private key %s" % (pow(k2, x, n)))
    print("Bob's private key %s" % (pow(k1, y, n)))


if __name__ == '__main__':
    # It should be a huge prime number of course
    n = 37
    # g is the primitive root of n
    g = 13
    # Using Diffie-Hellman cryptosystem for generating private key (for DES and AES)
    generate_private_key(n, g)
