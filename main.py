import os
import pandas as pd
from Modules import modulos

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
                print(modulos.show_choosen_file(x))
                
            except:
                return print('Você não selecionou nenhum arquivo!')
        elif resposta == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            c = modulos.filter_list(dataframe=modulos.show_choosen_file(x).columns)
            for i in c:
                print(f'{c.index(i)} - {i}')
            opt = int(input('Digite o numero da coluna a ser filtrada: '))
            print(modulos.show_choosen_file(x)[c[opt]])

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
