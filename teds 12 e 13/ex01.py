print('*********************************************************')
print('**************ALGORITMO GLOSSÁRIO PYTHON*****************')
print('*********************************************************')

from time import sleep

glossário_py={'Python:':'uma linguagem de programação de fácil aprendizagem.','Variável:':'um endereço que armazena um conteúdo na memória de um computador.','Indentação:':'um recurso fundamental para escrever o código do programa de forma hierárquica.','Lista:':'uma estrutura de dados.','print:':'uma função que serve para imprimir os argumentos passados a ela no terminal.'}

for i in glossário_py:
    sleep(1)
    print('\n')
    print(f'{i} é {glossário_py[i]}')
print('\n')
print(':) Que tal ampliar os seus conhecimentos de Python incrementando mais palavras ao glossário?')
print('\n')