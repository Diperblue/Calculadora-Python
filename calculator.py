#imports
import time
import math
#imports

#progress_bar
def progress_bar(done):
    print("\rCarregando: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.009)
#progress_bar

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
sr1 = int(input(print('Qual conta você quer fazer?: ')))
#pergunta

#soma-2num
if sr1 == 1:
    sr2 = int(input(print('Qual a quantidade de numeros: ')))
    if sr2 == 2:
        num21s = int(input(print('Qual o primeiro numero: ')))
        num22s = int(input(print('Qual o segundo numero: ')))
        soma21 = num21s + num22s
        test()
        print(f'\nA soma entre {num21s} e {num22s} e {soma21}')
#soma-2num