texto = input()
maiuscula = 0
minuscula = 0
numero = 0
invalido = 0
contador = 0
sequencia = 0

while contador < len(texto):
    if ord(texto[contador]) > 64 and ord(texto[contador]) <91:
        maiuscula += 1
    if ord(texto[contador]) < 123 and ord(texto[contador]) > 90:
        minuscula += 1
    if texto[contador].isnumeric():
        numero += 1
    if (ord(texto[contador]) < 64 or ord(texto[contador])>122) and not texto[contador].isnumeric():
        invalido += 1
    if contador+1 < len(texto):
        if ord(texto[contador])+1 == ord(texto[contador+1]):
            sequencia += 1
    
    contador += 1

if len(texto) > 5 and len(texto) < 16:
    if maiuscula != 0 and minuscula != 0 and numero != 0 and invalido == 0 and sequencia == 0:
        print("senha ok")
    else:
        print("senha invalida")
else:
        print("senha invalida")

