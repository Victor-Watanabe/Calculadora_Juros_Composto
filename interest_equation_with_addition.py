import PySimpleGUI as sg
import formula

def equation_interest_addition(number_float,percentage_float,month):
    
    montante = number_float*1+percentage_float**month 

    print(montante)