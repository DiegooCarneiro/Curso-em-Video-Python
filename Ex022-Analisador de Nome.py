'''
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras tem ao total sem considerar espaços.
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()
substituidor = nome.replace(' ', '')

print('Seu nome em maiúscula é: {} '.format(nome.upper()))
print('Seu nome em minúscula é: {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(substituidor)))
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) Do professor: contar quantas letras sem os espaços

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

'''separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))''' # Do professor: quantidade de letra do 1º nomeem {len(tamanho[0])} letras')