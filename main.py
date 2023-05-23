import numpy as np

def euklid(a, b):
    if b == 0:
        return a
    print(f"{a} = {np.floor(b)} * {b} + {a % b}")
    return euklid(b, a % b)

def find_st(a, b):
    s = 0
    old_s = 1
    r = b
    old_r = a
    while r != 0:
        quotient = np.floor(old_r / r)
        oldest_r = old_r
        old_r = r
        r = oldest_r - quotient * r
        oldest_s = old_s
        old_s = s
        s = oldest_s - quotient * s
    if b != 0:
        bez_t = np.floor((old_r - old_s * a) / b)
    else:
        bez_t = 0
    return [old_s, bez_t]

def diofant(a, b, c, s, t):
    D = euklid(a, b)
    if D % c == 0:
        return "Kan ikke løses"
    a_maerke = a / D
    b_maerke = b / D
    c_maerke = c / D
    return f"(x, y) = ({c_maerke * s} - {b_maerke}k; {c_maerke * t} + {a_maerke}k)"

def loes_diofant(a,b,c):
    print("Finder største fælles divisor vha. Euklids algoritme med følgende ligninger:\n")
    print(f"største fælles divisor: {euklid(a,b)}\n\n")
    print(f"Finder s og t:")
    st = find_st(a,b)
    print(f"s = {st[0]} og t = {st[1]}\n\n")
    print("Løser diofantisk ligning med formen ax + by = c:")
    print(diofant(a, b, c, st[0], st[1]))

def loes_euklid(a,b):
    print("Finder største fælles divisor vha. Euklids algoritme med følgende ligninger:\n")
    print(f"største fælles divisor: {euklid(a, b)}\n\n")
    print(f"Finder s og t:")
    st = find_st(a, b)
    print(f"s = {st[0]} og t = {st[1]}\n\n")

print("For at finde sfd/gcd samt s-, og t-værdier skriv \"euk,a,b\"")
print("For at løse en diofantisk ligning skriv \"dio,a,b,c\"")
input = input().split(",")
if input[0] == "euk":
    loes_euklid(int(input[1]), int(input[2]))
elif input[0] == "dio":
    loes_diofant(int(input[1]), int(input[2]), int(input[3]))
else:
    "Prøv igen, programmet forstod dig ikke."