'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

print('Este é  o Sistema TINTAS ARCO-IRIS: ')

m2 = float(input('Digite aqui Quantos metros quadrados serão Pintados: '))

litro = 1
cobertura = 3
lata = 18
valor = 80.00

print(f'Para esta metragem Quadrada são necessários: {m2 / cobertura:.2f} lts')
print(f'Serão necessárias: {(m2 / cobertura) / lata:.2f} latas. ')
print(f'Que custarão: R$ {(m2 / cobertura) / lata  * valor:.2f}')