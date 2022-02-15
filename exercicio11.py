'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

print('Aqui vamos ter algumas operações. Teremos 3 numeros e com eles:\n '
      '\no produto do dobro do primeiro com metade do segundo' 
      '\na soma do triplo do primeiro com o terceiro'
      '\no terceiro elevado ao cubo.\n')

n1 = int(input('Digite aqui o 1º numero: '))
n2 = int(input('Digite aqui o 2º numero: '))
n3 = int(input('Digite aqui o 3º numero: \n'))

a = (n1 * 2) * 2 + (n2 / 2)  #calculo a
print(f'{a} - é o produto do dobro do primeiro com metade do segundo\n ')

b = (n1 * 3) + n3  #calculo b
print(f'{b} - a soma do triplo do primeiro com o terceiro\n ')

c = (n3 ** 3)
print(f'{c} - o terceiro elevado ao cubo ')