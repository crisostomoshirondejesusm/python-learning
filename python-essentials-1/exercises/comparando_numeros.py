
''' Programa que faz a leitura de 3 numeros, compara-os e mostra o maior na tela '''

'''Primeiro, pedimos para que o usuario insira os numero, no nosso caso interos'''



# num1 = int(input('primeiro numero'))
# num2 = int(input('segundo numero'))
# num3 = int(input('terceiro numero'))



'''
Em seguida, para facilitar a comparacao, criamos uma variavel chamada maior_numero
e atribuimos a ela o valor de num1.
nesse caso, assumimos que num1 e o primeiro valor.
'''

# maior_numero = num1

''' Iniciamos a comparação e atualizamos o valor da variavel maior_numero'''

# if num2 > maior_numero:
    # maior_numero = num2
    
''' Comparamos o terceiro com o valor da variavel maior_numero atual 
e atualizamos novamente o seu valor se necessario'''


# if num3 > maior_numero:
    # maior_numero = num3
    
'''imprensao do mior_numero e dos numero introduzidos pelo usuario'''
    
# print(maior_numero)
# print(num1, num2, num3)





# podemos simplificar ainda mais esse codigo usando a função max() para o maior e min() para o minimo

# leitura dos numeros

num1 = int(input(f'{1}° numero'))
num2 = int(input(f'{2}° numero'))
num3 = int(input(f'{3}° nmero'))

# criar a variavel maior_numero para receber a função max() e determinar o maior numero

maior_numero = max(num1, num2, num3)
print(maior_numero)

# par achar o menor valor de todos é so trocar max() por min()