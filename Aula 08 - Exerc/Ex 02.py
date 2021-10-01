# 2. Crie um programa que lê três números do usuário, e utiliza duas funções diferentes para
#determinar o maior e o menor número. Imprima o maior e menor valor na tela

print('Qual o maior e qual o menor dos números?')
num1 = float(input('Digite o número 01: '))
num2 = float(input('Digite o número 02: '))
num3 = float(input('Digite o número 03: '))

if num1 > num2 and num1 > num2:
    if num2 > num3:
        print('O maior número é, ', num1)
        print('O menor número é, ', num3)
    else:
        print('O maior número é, ', num1)
        print('O menor número é, ', num2)
        
if num2 > num1 and num1 > num2:
    if num1 > num3:
        print('O maior número é, ', num2)
        print('O menor número é, ', num3)
    else:
        print('O maior número é, ', num2)
        print('O menor número é, ', num1)
        
if num3 > num1 and num3 > num2:
    if num2 > num1:
        print('O maior número é, ', num3)
        print('O menor número é, ', num1)
    else:
        print('O maior número é, ', num3)
        print('O menor número é, ', num2)