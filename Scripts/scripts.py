#WHILE
x=1

while x < 10:
    print(x)
    x += 1 #x = x + 1

#FOR
lista1 = [1,2,3,4,5]
lista2 = ["Olá","Mundo","!"]
lista3 = [0,"Olá","Biscoito","Bolacha",9.99,True]

for i in lista3:
    print(i)

#FOR-RANGE
for i in range(10,20,2):
    print(i)

#STRINGS
a = "Diogenes"
b = "Matheus"

concatenar = a + " " + b

tamanho = len(concatenar)
print (concatenar)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

c = "Marcos"
d = "Vinicius"

concatenar = c + " " + d
print(concatenar[0:4])

e = "Guilherme"
f = "Henrique"

concatenar = e + " " + f
print(concatenar)
concatenar = concatenar.upper()
print(concatenar)

concatenar = e + " " + f + "\n"
print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split("r")
print(minha_lista)

busca = minha_string.find("rainha")
print(busca)

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)
