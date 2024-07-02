import PySimpleGUI as sg
import formula

def equation_interest(number_float,percentage_float,month):
    montante = number_float * (1 + percentage_float / 100) ** month
    montante = round(montante,2)
    total_invested = number_float
    fees = montante - number_float
    fees = round(fees,2)
    number_float = round(number_float,2)

    print(f"O resultado de investimento após {month} meses: \n O total de Juros foi de {fees}; \n O total arrecadado foi de {montante};\n Com o valor de Capital Inicial de {number_float}.")