numero = 0
print (f"\033[3mNúmeros PARES entre 1 y 10000: {numero}\033[0m")

print("="*30)
for i in range(2, 11,2):
    numero = i
    print (f"\033[1mNúmero: {numero}\033[0m")

print("="*30)