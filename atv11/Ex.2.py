#Escreva um algoritmo que leia um vetor de 15 elementos
#inteiros. Encontre e imprima na tela o menor elemento,
#assim como sua posição no vetor.

lista = []

num = int(input('Digite o tamanho da lista: '))

while num !=0:
    x = int(input('Digite um número: '))
    if x in lista:
        print('Tente outro número')
    else:
        lista.append(x)
        num -= 1
    
y = min(lista)
elemento = lista.index(y)

print(lista)
print('O menor elemento da lista é: ', y)
print('E o elemento está na posição: ', elemento)