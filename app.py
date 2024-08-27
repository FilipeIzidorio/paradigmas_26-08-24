numero = int(input("digite um numero inteiro: "))

"""
for i in range(1, numero + 1):
    print("*" * i)

print("\n")
print("outra forma\n")


for i in range(numero,0,-1):
    print("*" * i)
"""


for i in range(1,numero+1):
    for j in range(i):
        print("*",end="")
    print()

print("\n")

for i in range(numero,0,-1):
    for j in range(i):
        print("*",end="")
    print()