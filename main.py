import os
import pandas as pd
from Modules import modulos
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import operator

def run():
    while True:
        print('-=' * 60)
        resposta = str(input('1 - IMPORTAR UMA NOVA PLANILHA\n2 - EXIBIR ARQUIVO\n3 - Filtrar por coluna\n* - SAIR DO PROGRAMA\n|' ))
        print('-=' * 60)
        if resposta == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            x = modulos.choose_file()
        elif resposta == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                print(modulos.display_choosen_file(x))
                
            except:
                return print('Você não selecionou nenhum arquivo!')
        elif resposta == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            # c = modulos.filter_list(dataframe=modulos.display_choosen_file(x))
            # for i in c:
            #     print(f'{c.index(i)} - {i}')
            #     adnetrindade @ hotmail.com
            # reposta2 = input()
            # opt = int(input('Digite o numero da coluna a ser filtrada: '))
            # a = list(modulos.display_choosen_file(x)[c[opt]])
            # os.system('cls' if os.name == 'nt' else 'clear')
            # for i in a:
            #     print(f'{a.index(i)} - {i}')
            # opt2 = int(input('Digite o valor da linha a ser filtrada: '))

            # os.system('cls' if os.name == 'nt' else 'clear')
            # a = modulos.display_choosen_file(x)[c[opt]] == a[opt2]
            # print(modulos.display_choosen_file(x)[a])
        elif resposta =='*':
            break
            
run()
print('-= VOLTE SEMPRE =-')


# operator_dict = {
#     '+' : operator.add,
#     '==': operator.eq,
#     '>' : operator.gt,
#     '<' : operator.lt,
# }

# num1 = int(input("Enter a number 1: "))
# oper = input("Choose a math operation (+, ==, >,<): ")
# num2 = int(input("Enter a number 2: "))

# print(operator_dict[oper](num1, num2))

# print(read_file())
