# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

grausf = float(input('Aqui vamos transformar Graus F em Graus Celsius'
                     '\nDigite aqui os graus F: '))

print(f'{grausf} graus F são equivalentes a {(grausf - 32) / 1.8} Graus Celsius')