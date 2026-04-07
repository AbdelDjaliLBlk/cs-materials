# TP n°3 — Exercice 2
def power_mod(base, exp, n):
    result = 1
    base = base % n
    while exp > 0:
        if exp % 2 == 1:        # si bit = 1
            result = (result * base) % n
        exp = exp // 2          
        base = (base * base) % n
    return result


# (gcd, x, y) tel que : a*x + b*y = gcd
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1

def mod_inverse(e, phi):
    _, x, _ = extended_gcd(e, phi)
    return x % phi


def chiffrer(message, e, n):
    chiffre = []
    for i in range(len(message)):
        M = ord(message[i])   
        C = power_mod(M, e, n)          
        chiffre.append(C)
    return chiffre

def trouver_cle_privee(e, phi):
    return mod_inverse(e, phi)


def dechiffrer(chiffre, d, n):
    message = ""
    for i in range(len(chiffre)):
        M = power_mod(chiffre[i], d, n)  
        message += chr(M)                
    return message


if __name__ == "__main__":
    n   = 187
    e   = 3
    phi = 160   # phi(n) = (p-1)*(q-1) = 10*16
    message = "BOB"

    print("=" * 40)
    chiffre = chiffrer(message, e, n)
    print(f"*    Message chiffré   : {chiffre}")

    d = trouver_cle_privee(e, phi)
    print(f"**   Clé privée D :{d}")

    dechiffre = dechiffrer(chiffre, d, n)
    print(f"***  Message déchiffré : {dechiffre}")
    print(f"**** Identique a l'originale : {message == dechiffre}")
    print("=" * 40)