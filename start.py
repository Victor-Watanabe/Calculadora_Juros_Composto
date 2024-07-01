import PySimpleGUI as sg
import Information_for_calculations

def first_face():
    sg.theme('reddit')

    window_size = (580, 220)  # Largura x Altura em pixels

    # Estilo do botão "Próximo"
    button_style = {'size': (12, 1), 'font': ('Times New Roman', 14, 'bold')}

    layout = [
        [sg.Text(
            "Calcule o Montante final de seu Investimento!", 
            justification='center', 
            size=(50, 1),
            font=('Times New Roman', 20, 'bold'),  
            text_color='black'
        )],
        [sg.Text("Para Calcular, Precisamos das Seguintes Informações:", text_color='black', size=(100, 1), font=('Times New Roman', 14), justification='left')],
        [sg.Text("* Capital Inicial;", text_color='black', size=(100, 1), font=('Times New Roman', 14), justification='left')],
        [sg.Text("* Taxa de Juros;", text_color='black', size=(100, 1), font=('Times New Roman', 14), justification='left')],
        [sg.Text("* Tempo Total de Investimento.", text_color='black', size=(100, 1), font=('Times New Roman', 14), justification='left')],
        [sg.Text("Clique em ''", text_color='black', font=('Times New Roman', 14), justification='left', pad=(0, 0)),
         sg.Text("Seguir", text_color='blue', font=('Times New Roman', 14), justification='left', pad=(0, 0)),
         sg.Text("'' Para Continuar.", text_color='black', font=('Times New Roman', 14), justification='left', pad=(0, 0)),
         sg.Button("Seguir", **button_style, pad=((190, 0), 0))],
        [sg.Text('', size=(20, 1))],  # Espaço vazio para separação
    ]

    # Calculando a posição para centralizar a janela
    screen_width, screen_height = sg.Window.get_screen_size()
    window_x = (screen_width - window_size[0]) // 2
    window_y = (screen_height - window_size[1]) // 2

    window = sg.Window('Calcule seu Juros Composto 📊', layout=layout, size=window_size, location=(window_x, window_y), return_keyboard_events=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event in ('Return', 'Return:36', 'Enter:13', '\r', 'Enter:108'):
            event == 'Seguir'
            window.close()
            Information_for_calculations.data_base() 
        elif event == 'Seguir':
            window.close()
            Information_for_calculations.data_base() 
        elif event == 'Escape:27':
            break

# Chamando a função principal
if __name__ == "__main__":
    first_face()
