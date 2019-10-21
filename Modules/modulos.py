from os import path
import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd, Tk
import operator


def choose_file():
    file = fd.askopenfilename(initialdir=path.expanduser("~/Desktop"))
    return file

def show_choosen_file(file):
    if file.endswith('xlsx'):
        table = pd.read_excel(file)
    elif file.endswith('csv'):
        table = pd.read_csv(file,sep=';')
    try:
        return table
    except:
        print('Não foi possivel abri o arquivo selecionado')

def filter_list(dataframe):
    return list(dataframe)

def filtrar(table, f1, f2):
    a = table[f1] == f2
    return a