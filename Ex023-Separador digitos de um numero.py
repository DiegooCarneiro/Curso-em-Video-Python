'''
Exercício Python 023: Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.
'''

#Pegando pela posição

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(100000 + n))
print('{} milhares.'.format(n2[2]))
print('{} centenas. '.format(n2[3]))
print('{} dezenas. '.format(n2[4]))
print('{} unidades.'.format(n2[5]))

#--------------------------------------------

#usando a matemática

'''
n = str(input('Digite um numero de 0 a 9999: '))

print(f'Unidade: {n[-1 : ]} ') #usando o f'' no lugar do .format
print('Dezena:  {} \nCentena: {}'.format(n[-2 : -1], n[-3 : -2]))
print('Milhar:  {}'.format(n[-4 : -3]))


#usando a matemática

n2 = int(input('Digite um valor: '))

u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10

print('Unidade: {} '.format(u))
print('Dezena:  {} '.format(d))
print('Centeza: {} '.format(c))
print('Milhar:  {} '.format(m))
'''

