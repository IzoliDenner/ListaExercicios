'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

salarioh = float(input('Quanto voce ganha por hora trabalhada? '))
horast = float(input('Quantas horas voce trabalha por mes? '))

salariob = salarioh * horast
ir = salariob * 0.11
inss = salariob * 0.08
sindicato = salariob * 0.05

sl = salariob - ir - inss - sindicato

print(f'Salário Bruto: R$ {salariob:.2f}')
print(f'Imposto de renda (11%): R$ {ir:.2f}')
print(f'Inss (8%): R$ {inss:.2f}')
print(f'Sindicado (5%): R$ {sindicato:.2f}')
print(f'Salario liquido: R$ {sl:.2f}')


