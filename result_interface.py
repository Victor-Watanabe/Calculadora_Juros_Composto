import PySimpleGUI as sg
import Information_for_calculations

def presenting_results(montante, fees, total_invested):
    sg.theme('reddit')

    # Definindo o tamanho da janela
    window_size = (580, 260)

    # Estilo dos botões
    button_style = {'size': (60, 1), 'font': ('Times New Roman', 15, 'bold')}

    # Layout da interface
    layout = [
        [sg.Text(
            'Resultado Final do Cálculo', 
            justification='center', 
            size=(60, 1),  
            font=('Times New Roman', 24, 'bold'),
            text_color='black',
            pad=((0, 0), (1, 26))  
        )],
        [sg.Text('Valor Final:', justification='left', size=(10, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
         sg.Text(f'R${montante}', size=(45, 1), justification='right', font=('Times New Roman', 16), key='montante_value')],
        [sg.Text('Rendimento:', justification='left', size=(10, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
         sg.Text(f'R${fees}', size=(45, 1), justification='right', font=('Times New Roman', 16), key='fees_value')],
        [sg.Text('Total Investido:', justification='left', size=(10, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
         sg.Text(f"R${total_invested}", size=(45, 1), justification='right', font=('Times New Roman', 16), key='total_invested_value')],
        [sg.Text('', size=(54, 1)), sg.Button("Voltar", **button_style), sg.Text('')]
    ]
    
    # Criando a janela
    window = sg.Window('Resultado do Cálculo 📊', layout=layout, size=window_size)

    while True:
        event, values = window.read()
        
        # Verificando se a janela foi fechada
        if event == sg.WINDOW_CLOSED:
            break
        
        # Voltando para a tela anterior ao clicar em "Voltar"
        if event == "Voltar":
            window.close()
            Information_for_calculations.data_base()

    window.close()