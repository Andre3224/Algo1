#3. Crie um programa que lê um número não-negativo (> 0) do usuário, e calcula a operação fatorial
#para aquele número.
#- Com estruturas de repetição (PARA, ENQUANTO...)
#- Com chamadas recursivas
#- OBS: Fatorial de 5 -> 5! = 5 * 4 * 3 * ... * 2 * 1

num = float(input('Digite um número: '))
fatori = 1
while(num > 0):
    fatori = fatori * num
    num = num - 1
    
print('O valor fatorial é de: ', fatori)