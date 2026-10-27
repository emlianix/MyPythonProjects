n = int(input())

binary = bin(n)
octal = oct(n)
hexadec = hex(n)

print(binary[2:])
print(octal[2:])
print(hexadec[2:].upper())