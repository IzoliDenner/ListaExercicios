#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


salario_hora = float(input('''Vamos calcular o seu salário mensal !!!
                   \nDigite aqui quanto voce ganha por hora:'''))

horas_trabalhadas = int(input('Agora digite quantas horas voce trabalhou no mes: '))

print(f'O Seu Salário mensal é de: {salario_hora * horas_trabalhadas} por mes, ')