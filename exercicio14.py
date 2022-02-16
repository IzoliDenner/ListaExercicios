'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

kilos = float(input('Digite aqui a quantidade de Kilos que trouxe hoje: '))
kilosp = 50
multa = 4.00


if kilos == 50:
    print('Este é o limite permitido, não haverá multa')
elif kilos >= 51:
    print(f'{kilos}Kg, Voce Ultrapassou o limite permitido em: {kilos - kilosp}Kg '
          f'\ne devera pagar uma multa de: R$ {(kilos - kilosp) * multa}')

