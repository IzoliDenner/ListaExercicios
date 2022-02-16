'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''


print('Ola, Este é o sistema ARCO IRIS TINTAS ')

m2 = float(input('Qual a medida em M2 que serão pintados? '))

cobertura = 6
lata = 18
valor = 80.00
galao = 3.6
valorg = 25.00

print(f'Serão necessários {m2 / cobertura:.2f} lts de tinta.')
print(f'Em latas de 18lts precisará de: {(m2 / cobertura) / lata:.2f}latas, que custarão: R$ {(m2 / cobertura) / lata * valor:.2f}')
print(f'Em latas de 3,6ls precisa de: {(m2 / cobertura) / galao:.2f}latas, que custarão: R$ {(m2 / cobertura) / galao * valorg:.2f}')