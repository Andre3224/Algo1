#Escreva um algoritmo que leia um vetor inteiro de 20
#posições (vetor 1). Verifique os valores do vetor 1 e
#modifique um segundo vetor (vetor 2), atribuindo o valor “1”
#ao vetor 2 quando houver um valor nulo no primeiro vetor.
#Ao fim, imprima os dois vetores

Vetor1 = []
Vetor2 = []
num = 20

while num !=0:
    x = int(input('Digite um número: '))
    if x in Vetor1:
        print('Tente outro número')
    else:
        Vetor1.append(x)
        num -= 1
        
if 0 in Vetor1:
    Vetor2 = 1
    print('Tem 0 no vetor 1')

else:
    Vetor2 = Vetor1

print('O vetor 1 é: ', Vetor1)
print('o vetor 2 é: ', Vetor2)