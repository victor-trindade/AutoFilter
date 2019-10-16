import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd, Tk
import operator

Tk().withdraw() 

def choose_file():
    file = fd.askopenfilename()
    return str(file)

def show_choosen_file(file):
    table = pd.read_excel(file)
    return(table)