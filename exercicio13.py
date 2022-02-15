'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

print('Aqui vamos calcular seu peso ideal levando em conta também o tipo do Sexo.\n ')
sexo = (input('Voce se considera "Homem" ou "Mulher" \n'))
h = float(input('Qual a sua altura: \n'))

alturah = (72.7 * h) - 58
alturam = (62.1 * h) - 44.7

if sexo == "Homem":
    print(f' considerando-se homem e sua altura o seu peso ideal é de: {alturah:.2f} ')

else:
    sexo == "Mulher"
    print(f' Considerando-se mulher e sua altura o seu peso ideal é de: {alturam:.2f}')
