import PySimpleGUI as sg
from decimal import Decimal, getcontext
import result_interface

# Aumenta a precisão para lidar com números grandes
getcontext().prec = 100  # Ajuste a precisão conforme necessário

def equation_interest(number_float, percentage_float, month):
    # Converte os valores para Decimal para maior precisão
    number = Decimal(number_float)
    percentage = Decimal(percentage_float) / 100
    months = Decimal(month)

    # Cálculo de Equação Juros Composto SEM acréscimo
    montante = number * (1 + percentage) ** months

    # Descobrindo o Valor de Juros.
    fees = montante - number

    # Criando a Devida nomenclatura
    total_invested = number

    # Tratamento de dados para incluir 02 dígitos após vírgula
    try:
        montante = round(montante, 2)
        fees = round(fees, 2)
        total_invested = round(total_invested, 2)
    
    except: 
        print("Valor Limite atingido, Preencha com valores menores!")

    # Realizando o tratamento de dados para o valor aparecer em contábil
    montante = "{:,.2f}".format(montante).replace(",", "X").replace(".", ",").replace("X", ".")
    fees = "{:,.2f}".format(fees).replace(",", "X").replace(".", ",").replace("X", ".")
    total_invested = "{:,.2f}".format(total_invested).replace(",", "X").replace(".", ",").replace("X", ".")

    return result_interface.presenting_results(montante, fees, total_invested)
