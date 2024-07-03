import PySimpleGUI as sg
from decimal import Decimal, getcontext
import result_interface

# Aumenta a precisão para lidar com números grandes
getcontext().prec = 100  # Ajuste a precisão conforme necessário

def equation_interest(number_float, percentage_float, months):
    # Converte os valores para Decimal para maior precisão
    number = Decimal(number_float)
    percentage = Decimal(percentage_float) / 100
    months = Decimal(months)

    # Cálculo de Equação Juros Composto com acréscimo mensal do capital inicial
    montante = Decimal(0)
    capital_acrescentado = Decimal(number_float)

    for month in range(1, int(months) + 1):
        montante += capital_acrescentado
        montante *= (1 + percentage)

    # Criando a devida nomenclatura
    total_invested = number * month

    # Descobrindo o Valor de Juros.
    fees = montante - total_invested

    # Tratamento de dados para incluir 02 dígitos após a vírgula
    montante = round(montante, 2)
    fees = round(fees, 2)
    total_invested = round(total_invested, 2)

    # Ajustando para contabilizar o primeiro mês de cálculo
    montante = montante + number
    total_invested = total_invested + number


    # Realizando o tratamento de dados para o valor aparecer em contábil
    montante = "{:,.2f}".format(montante).replace(",", "X").replace(".", ",").replace("X", ".")
    fees = "{:,.2f}".format(fees).replace(",", "X").replace(".", ",").replace("X", ".")
    total_invested = "{:,.2f}".format(total_invested).replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"{montante}\n {fees} \n {total_invested}")
    return result_interface.presenting_results(montante, fees, total_invested)
