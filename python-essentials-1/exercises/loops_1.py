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
    print('nenhum numero foi digitado')

else:
    print(f' o maior numero e : {maior_numero}')

# essa ultima parte do codigo, pega as condicoes geradas no bloco 'while True' as executa e mostra os devidos resultados na tela

print('='*40, 'FIM DO PROGRAMA', '='*40)


'''NOTA: neste programa , alem do loop while, fizemos tambem o uso de alguns operadores logicos 'is' e 'or' '''