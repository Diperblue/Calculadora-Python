#imports
import time
#imports

#defs
    #loading
def progress_bar(done):
    print("\rCarregando: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def loading():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.001)
    #loading
#defs

#print-calculos
print('-'*50)
print('[ 1 ] Somar')
print('[ 2 ] Multiplicação')
print('[ 3 ] Divisão')
print('[ 0 ] Sair do menu')
print('-'*50)
#print-calculos

#pergunta
while True:
    r1 = int(input('Digite o numero do calculo que você vai querer fazer: '))
    if r1 != int:
        r1 = int(input('Digite um numero valido dependendo do calculo que você vai querer executar: '))
    else:
        break
#pergunta

#soma
if r1 == 1:
    num1s = float(input('Qual o primeiro numero: '))
    num2s = float(input('Qual o segundo numero: '))
    soma1 = num1s + num2s
    loading()
    print(f'\nA soma entre {num1s} e {num2s} e {soma1}')
#soma

#multiplicação
    #num2
if r1 == 2:
    r1r2 = int(input('Quantos numeros para a multiplicação: '))
    if r1r2 == 2:
        num1m = float(input('Qual o primeiro numero: '))
        num2m = float(input('Qual o segundo numero: '))
        mult1 = num1m * num2m
        loading()
        print(f'\nA multiplicação entre {num1m} e {num2m} e {mult1}')
    #num2

    #num3
    if r1r2 == 3:
        num1m = float(input('Qual o primeiro numero: '))
        num2m = float(input('Qual o segundo numero: '))
        num3m = float(input('Qual o terceiro numero: '))
        mult1 = num1m * num2m * num3m
        loading()
        print(f'\nA multiplicação da {mult1}')
    #num3

#mulplicação

#divisão
if r1 == 3:
    r1r3 = int(input('Com quantos numeros você vai querer fazer a divisão?: '))
    #num2
    if r1r3 == 2:
        num1d = float(input('Qual o primeiro numero: '))
        num2d = float(input('Qual o segundo numero: '))
        divisao = num1d/num2d
        loading()
        print(f'\nA multiplicação da {divisao}')
    #num2

    #num3
    if r1r3 == 3:
        num1d = float(input('Qual o primeiro numero: '))
        num2d = float(input('Qual o segundo numero: '))
        num3d = float(input('Qual o terceiro numero: '))
        divisao = num1d/num2d/num3d
        loading()
        print(f'\nA multiplicação da {divisao}')
    #num3
#divisão

if r1 == 0:
    pass
#multiplicação