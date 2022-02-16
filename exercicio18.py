'''
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = float(input('Digite o tamanho do arquivo para download: '))
velocidade = float(input('Digite a velocidade da internet: '))

tempo = tamanho / velocidade
minutos = tempo / 60

print(f'O arquivo levará: {tempo} para ficar pronto')
print(f'O arquivo levara: {minutos} para ser baixado')