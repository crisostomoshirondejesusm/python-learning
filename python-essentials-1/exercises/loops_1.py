


'''objetivo: criar um programa que compara 3, 100mil ou ate mais de 1M de numeros fornecidos pelo usuario.
para esse caso precisamos de um loop, no caso usaremos o loop while '''


maior_numero = None # o None, informa que ainda nao sei qual e o maior valor.

#( None e um valor especial que indiga que uma dada variavel ou funcao ainda nao tem nenhum valor fisico, porem, None != 0)

while True: # enquanto for verdade, executa o loop do bloco que vem asseguir

    num = int(input('insira os numeros que pretende comparar e ( -1 para encerar)')) # recebe dados do usuario

    if num == -1: # condicao de parada do loop
        break # impede que torne-se um loop infinito encerrando eessa parte do programa
    # porem permitindo com que a parte por baixo dessa linha comesse a ser executada

    if maior_numero is None or num > maior_numero:
        maior_numero = num

    # esta parte faz a comparacao dos dados inseridos e atualiza o valor da variavel maior_numero

if maior_numero is None:
    print(' nenhum numero foi digitado')

else:
    print(f' o maior numero e : {maior_numero}')

# essa ultima parte do codigo, pega as condicoes geradas no bloco 'while True' as executa e mostra os devidos resultados na tela

print('='*40, 'FIM DO PROGRAMA', '='*40)


'''NOTA: neste programa , alem do loop while, fizemos tambem o uso de alguns operadores logicos 'is' e 'or' '''

# Resolução do problema gerado pelo programa acima

''' Esse programa da erro do tipo ValueError quando o usuario preciona a tecla Enter sem introduzir nenhum numero
logo no inicio por conta da entrada int(input()) quando o input nao recebe nada, ele retorna uma string vazia (''),
e o int() tenta converter uma string inválida para inteiro e gera ValueError”.
para que o programa nao quebre nessa situacao, primeiro lemos o numero, so depois convertemos. entretanto, pode se dar o caso de
o usuario digitar letras.
para esse problema, usamos 'if not .isdigit()', também usamos o continue para retornar ao inicio do loop, caso um desses erros ocorra.'''




maior_numero = None

while True:  # inicia o loop. enquanto for verdade, toda parte do codigo endentada sera executada em loop.
    
    entrada = input('digite um numero, e digite -1 para encerar') # recebendo dados do usuario que pode ser string vazia ou letra
    
    if entrada == '-1':  #condicao para encerar o loop
        break
        
    if entrada == '':       # tratando a entrada vazia. quando o usuario preciona Enter sem inserir nehum dado
        print('entrada invalida, por favor digite um numero')
        continue     # retorna para o inicio do loop

    # tratando do erro gerado quando o usuario digita letras ao invez de numeros
    if not entrada.isdigit(): # equivalente a 
        print('entrada invalida. digite apenas numeros')
        continue
    # se a entrada nao for composta só de numeros (inteiros), diga invalido e continue
    # Exemplo: 
    # entrada = 123, entrada.isdigit() = True mas o if not entrada.isdigit() converte isso para False
    # entrada = abc, entrada.isdigit() = False, mas o if not entrada.isdigit() converte isso em True
    # entrada = 12.23, entrada.isdigit() = False, mas o if not entrada.isdigit() converte isso em TRUE
        
    num = int(entrada) # converter a entra em um numero inteiro
    
    if maior_numero is None or num > maior_numero:
        maior_numero = num
        print(maior_numero)
    
        
if maior_numero is None:
    print('Nenhum número foi digitado')
else:
    print(f'O maior número é: {maior_numero}')



'''esse codigo também tem situações que podem o fazer travar, por exemplo se o usuario usar -1, 12.3, 
o .isdigit() só aceita números inteiro, .isdigit() é útil em casos simples, mas não é recomendado para validação numérica geral.
'123'.isdigit() True
'abc'.isdigit() False.
para solucionar esse problema, usamos o try/except'''


# Comparador de numeros mais seguro para interação com o usuario 

maior_numero = None

while True:
    entrada = input('Digite um número (-1 para encerrar): ')

    if entrada == '':
        print('Entrada vazia. Digite um número.')
        continue
# Conversão segura com try
    try:
        num = int(entrada)

# O try: Tenta converter a string em inteiro

# Se for "10" → funciona

# Se for "abc" → gera erro mas esse erro e capturado pelo except na linha asseguir

# Tratamento do erro

    except ValueError:
        print('Entrada inválida. Digite apenas números inteiros.')
        continue

# Captura somente o erro de conversão

# Evita que o programa pare

# Volta para pedir outro número
    
    if num == -1:
        break

    if maior_numero is None or num > maior_numero:
        maior_numero = num
        print('Maior até agora:', maior_numero)

if maior_numero is None:
    print('Nenhum número foi digitado')
else:
    print(f'O maior número é: {maior_numero}')


'''Nota:
esse ultimo codigo, so difere dos outros apenas pela presenca do try que e usado quando suspeita-se que uma determinada parte 
do godigo pode gerar erro e quebrar o programa, e o except que trata do erro gerado.
try deve ter um except no fim.'''