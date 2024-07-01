import PySimpleGUI as sg
import Information_for_calculations

def identify_formula():
    sg.theme('reddit')

    # Estilo dos botões
    button_style = {'size': (8, 1), 'font': ('Times New Roman', 12, 'bold'), 'border_width': 1}

    layout = [
        [sg.Text(
            'O Valor do Capital Inicial Será Acrescentado Em Todos Os Meses Subsequentes?', 
            justification='center', 
            size=(40, 2),
            font=('Times New Roman', 14, 'bold'),  # Embelezando a fonte do texto
            text_color='black'  # Cor do texto preto
        )],
        [sg.Column(
            [[sg.Button("SIM", **button_style), sg.Button('NÃO', **button_style)]], 
            justification='center'
        )]
    ]

    window = sg.Window('Identificando Qual a Fórmula Aplicada📊', layout=layout, return_keyboard_events=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'SIM':
            print("Usuário clicou SIM")
        elif event == 'NÃO':
            print("Usuário clicou NÃO")
        elif event == 'Escape:27':
            window.close()
            Information_for_calculations.data_base()
            break

    window.close()

# Chamando a função principal
if __name__ == "__main__":
    identify_formula()

