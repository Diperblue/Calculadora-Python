#variaveis-soma
soma = 1
multiplicação = 2
divisão = 3
esponenciação = 4
raizquadrada = 5
#variaveis-soma

#print-calculos

print('-'*50)
print('[ 1 ] Somar')
print('[ 2 ] Multiplicação')
print('[ 3 ] Divisão')
print('[ 4 ] Esponenciação')
print('[ 5 ] Raiz Quadrada')
print('-'*50)

#print-calculos

#pergunta
r1 = int(input(print('Qual conta você quer fazer?: ')))
#pergunta

#soma-2num
if r1 == 1:
    r1r1 = int(input(print('Qual a quantidade de numeros: ')))
    if r1r1 == 2:
        num21s = int(input(print('Qual o primeiro numero: ')))
        num22s = int(input(print('Qual o segundo numero: ')))
        soma21 = num21s + num22s
        print(f'A soma entre {num21s} e {num22s} e {soma21}')
#soma-2num