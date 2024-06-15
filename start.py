import PySimpleGUI as sg
import Information_for_calculations

def first_face():
    sg.theme('reddit')

    window_size = (550, 120)  # Largura x Altura em pixels

    # Estilo do botão "Próximo"
    button_style = {'size': (10, 1), 'font': ('Times New Roman', 12, 'bold')}

    layout = [
        [sg.Text(
            "Itens Calculáveis:", 
            justification='center', 
            size=(50, 1),
            font=('Times New Roman', 14, 'bold'),  # Alterando a fonte para Times New Roman
            text_color='black',  # Cor do texto preto
        )],
        [sg.Text("Podemos Calcular os Seguintes Itens: Montante, Capital Inicial, Valor de Juros e Tempo.\nClique em 'Seguir' Para Continuar.")],
        [sg.Text('', size=(50,1)), sg.Button("Seguir", **button_style), sg.Text('')]  
    ]

    # Calculando a posição para centralizar a janela
    screen_width, screen_height = sg.Window.get_screen_size()
    window_x = (screen_width - window_size[0]) // 2
    window_y = (screen_height - window_size[1]) // 2

    window = sg.Window('Calcule seu Juros Composto 📊', layout=layout, size=window_size, location=(window_x, window_y))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Seguir':
            window.close()
            Information_for_calculations.data_base() 
         
# Chamando a função principal
if __name__ == "__main__":
    first_face()
