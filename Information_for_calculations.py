import PySimpleGUI as sg
import formula
import format_capital
import format_percentage   
import format_month

def data_base():
    sg.theme('reddit')

    window_size = (660, 330)  # Largura x Altura em pixels

    button_style = {'size': (60, 1), 'font': ('Times New Roman', 15, 'bold')}

    layout = [
    [sg.Text(
        'Dados Para Base de Cálculos', 
        justification='center', 
        size=(60, 1),  # Diminuir o tamanho vertical
        font=('Times New Roman', 24, 'bold'),
        text_color='black',
        pad=((0, 0), (1, 26))  # Aumentar o espaçamento inferior comparado ao ajuste anterior
    )],
    [sg.Text('Capital Inicial:', justification='left', size=(25, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
     sg.Input(key='starting_capital', size=(45, 1), enable_events=True, justification='right', font=('Times New Roman', 16), text_color='black', tooltip='Informe o capital inicial', pad=((0, 0), (5, 10)))],
    [sg.Text('Porcentagem de Juros ao Mês:', justification='left', size=(25, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
     sg.Input(key='percentage_fees', size=(45, 1), enable_events=True, justification='right', font=('Times New Roman', 16), text_color='black', tooltip='Informe os juros ao mês (Ex: 10%)', pad=((0, 0), (5, 10)))],
    [sg.Text('Tempo de Investimento (Meses):', justification='left', size=(25, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
     sg.Input(key='time_in_mounths', size=(45, 1), enable_events=True, justification='right', font=('Times New Roman', 16), text_color='black', tooltip='Informe o Tempo Total de Investimento', pad=((0, 0), (5, 10)))],
    [sg.Text('Nota: Todos os valores devem ser compatíveis com informações ao mês. Se os \nvalores fornecidos estiverem em outra medida de tempo, Comprometerá o Cálculo!', 
             text_color='red', size=(70, 2), font=('Times New Roman', 13, 'bold'), pad=((0, 0), (10, 10)))],
    [sg.Text('', size=(54, 1)), sg.Button("Calcular", **button_style), sg.Text('')]
    ]
 
    window = sg.Window('Calcule seu Juros Composto 📊.', layout=layout, size=window_size)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Calcular':
            starting_capital_formatted = format_capital.format_currency(values['starting_capital'])
            percentage_fees = format_percentage.format_percentage(values['percentage_fees'])
            time_in_mounths = values['time_in_mounths']

            if not starting_capital_formatted or not percentage_fees or not time_in_mounths: 
                print("Faltou Preencher Campo!")
            else:
                # Fechar a janela antes de chamar a função de cálculo
                window.close()
                # Chamar a função para calcular usando os valores formatados
                formula.identify_formula()

        elif event == 'starting_capital':  # Evento para formatar o valor assim que o usuário terminar de inserir
            value_typed = values['starting_capital']
            value_formatted, number_float = format_capital.format_currency(value_typed)
            window['starting_capital'].update(value_formatted)  # Atualiza o campo com o valor formatado
            print(value_formatted)
            print(number_float)


        elif event == 'percentage_fees':  # Evento para formatar o valor assim que o usuário terminar de inserir
            percentage_typed = values['percentage_fees']
            percentage_formatted, percentage_float = format_percentage.format_percentage(percentage_typed)
            window['percentage_fees'].update(percentage_formatted)  # Atualiza o campo com o valor formatado
            print(percentage_formatted)
            print(percentage_float)
            print(len(percentage_formatted))

        elif event == 'time_in_mounths':  # Evento para formatar o valor assim que o usuário terminar de inserir
            mounth_typed = values['time_in_mounths']
            month_formatted, month = format_month.format_month(mounth_typed)
            window["time_in_mounths"].update(month_formatted)
            print(month_formatted)
            print(month)

        

    window.close()

# Chamando a função principal
if __name__ == "__main__":
    data_base()

# Variaveis que serão Utilizadas para equação: Percentage_Float e number_float.
# Arrumar o arquivo Fomrat_months seguindo os demais arquivos.