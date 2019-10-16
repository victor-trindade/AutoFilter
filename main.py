import os
import pandas as pd
from Modules import modulos


def run():
    while True:
        print('-=' * 60)
        resposta = str(input('1 - IMPORTAR UMA NOVA PLANILHA\n2 - EXIBIR ARQUIVO\n* - SAIR DO PROGRAMA\n|' ))
        print('-=' * 60)
        if resposta == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            x = modulos.choose_file()
        elif resposta == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                table = modulos.show_choosen_file(x)
                print(table)
            except:
                return print('Você não selecionou nenhum arquivo!')

        elif resposta =='*':
            break
            
run()
print('-= VOLTE SEMPRE =-')
# def read_file():
#     y = str(open_file())
#     if y.endswith('xlsx'):
#         table = pd.read_excel(y)
#     elif y.endswith('csv'):
#         table = pd.read_csv(y)
#     try:
#         return table
#     except:
#         print('Não foi possivel ler o arquivo')


# while True:
#     print('Read = Ler arquivo\nQuit = Sair do programa')
#     resposta = str(input('').lower())

#     if resposta == 'read':
#         print(read_file())
#     if resposta == 'quit':
#         break

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
# # def filter_by_column_name(name, value):
# #     filtered = read_file()[name] == value 
# #     return(read_file()[filtered])

