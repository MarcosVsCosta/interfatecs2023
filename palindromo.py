from unicodedata import normalize

texto = input()
texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
lista = []
comprimento = 0
contador = 0
palindromo = 0

for i in texto:
    if i != " ":
        lista.append(i)

if texto[len(texto)-1] == '.':
    lista.pop()

if len(lista) % 2 == 1:
    comprimento = int((len(lista)-1) / 2)
else:
    comprimento = int((len(lista)) / 2)

while contador < comprimento:
    #print(lista[contador] , lista[(len(lista)-1)-contador])
    if lista[contador].lower() != lista[(len(lista)-1)-contador].lower():
        palindromo = 1
    contador += 1

if palindromo == 0:
    print("palindromo")
else:
    print("não é palindromo")
