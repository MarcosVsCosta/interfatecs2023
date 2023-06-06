contador = 0
texto = input()
numero = 0
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','e','d','t','u','v','w','x','y','z']

if texto[1].isnumeric():
    numero = texto[0]+texto[1]
    numero = int(numero)
else:
    numero = texto[0]
    numero = int(numero)

while contador < numero:
    print('*'*(25-contador), end="")
    aux = 0
    if 'n' in texto:
        while aux <= contador:
            print(alfabeto[aux], end="")
            aux += 1
    else:
        while aux <= contador:
            print(alfabeto[aux].upper(), end="")
            aux += 1
    contador += 1
    print()
