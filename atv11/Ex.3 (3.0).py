#Escreva um algoritmo que leia um vetor inteiro de 20
#posições (vetor 1). Verifique os valores do vetor 1 e
#modifique um segundo vetor (vetor 2), atribuindo o valor “1”
#ao vetor 2 quando houver um valor nulo no primeiro vetor.
#Ao fim, imprima os dois vetores

Vetor1 = []
Vetor2 = []
num = 5

while num !=0:
    x = int(input('Digite um número: '))
    if x == 0:
        Vetor1.append(x)
        Vetor2.append(1)
        num -= 1 
    else:
        Vetor1.append(x)
        Vetor2.append(x)
        num -= 1 #(num = num - 1)
        
#print('O vetor 1 é: ', Vetor1)
#print('o vetor 2 é: ', Vetor2)

matrix2 = [[Vetor1[i], Vetor2[i]] for i in range(len(Vetor1))]
print(matrix2)