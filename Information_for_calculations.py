import PySimpleGUI as sg
import formula
import format_capital
        
def data_base():
    sg.theme('reddit')

    window_size = (430, 230)  # Largura x Altura em pixels

    button_style = {'size': (10, 1), 'font': ('Times New Roman', 12, 'bold')}

    layout = [
        [sg.Text(
            'Dados Cadastrais Para Cálculo', 
            justification='center', 
            size=(60, 2),
            font=('Times New Roman', 14, 'bold'),
            text_color='black'
        )],
        [sg.Text('Capital Inicial', justification='left', size=(30, 1)), sg.Input(key='starting_capital', size=(15, 1), enable_events=True, justification='right', font=('Times New Roman', 12), text_color='black', tooltip='Informe o capital inicial')],
        [sg.Text('Porcentagem de Juros ao Mês:', justification='left', size=(30, 1)), sg.Input(key='fees', size=(15, 1), enable_events=True, justification='right', font=('Times New Roman', 12), text_color='black', tooltip='Informe os juros ao mês (Ex: 10%)')],
        [sg.Text('Tempo de investimento', justification='left', size=(30, 1)), sg.Input(key='time', size=(15, 1), enable_events=True, justification='right', font=('Times New Roman', 12), text_color='black')],
        [sg.Text('Nota: Todos os valores devem ser compatíveis com informações ao mês.\nSe os valores fornecidos estiverem em outra medida de tempo, apresentará um erro!', text_color='red', size=(60, 2), font=('Times New Roman', 9))],
        [sg.Text('', size=(36, 1)), sg.Button("Calcular", **button_style), sg.Text('')]
    ]

    window = sg.Window('Calcule seu Juros Composto 📊.', layout=layout, size=window_size)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Calcular':
            starting_capital_formatted = format_capital.format_currency(values['starting_capital'])
            fees = values['fees']
            time = values['time']

            if not starting_capital_formatted or not fees or not time: 
                print("Faltou Preencher Campo!")
            else:
                # Fechar a janela antes de chamar a função de cálculo
                window.close()
                # Chamar a função para calcular usando os valores formatados
                formula.identify_formula()

        elif event == 'starting_capital':  # Evento para formatar o valor assim que o usuário terminar de inserir
            valor_digitado = values['starting_capital']
            valor_formatado, number_float = format_capital.format_currency(valor_digitado)
            window['starting_capital'].update(valor_formatado)  # Atualiza o campo com o valor formatado
            print(valor_formatado)
            print(number_float)
    window.close()

# Chamando a função principal
if __name__ == "__main__":
    data_base()
