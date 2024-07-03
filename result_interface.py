import PySimpleGUI as sg
import Information_for_calculations

def presenting_results(montante, fees, total_invested):
    sg.theme('GreenTan')  # Escolhendo o tema GreenTan

    # Definindo o tamanho da janela
    window_size = (600, 280)

    # Estilo dos botões
    button_style = {'size': (10, 1), 'font': ('Arial', 14)}

    # Layout da interface
    layout = [
        [sg.Text(
            'Resultado Final do Cálculo', 
            justification='center', 
            size=(30, 1),  
            font=('Helvetica', 24, 'bold'),
            text_color='white',
            background_color='#333333',
            pad=((0, 0), (10, 20))  
        )],
        [sg.Text('Valor Final:', justification='left', size=(10, 1), font=('Arial', 18, 'bold'), pad=((10, 10), (10, 10))), 
         sg.Text(f'R${montante}', size=(55, 1), justification='right', font=('Arial', 16, 'bold'), key='montante_value')],
        [sg.Text('Rendimento:', justification='left', size=(10, 1), font=('Arial', 18, 'bold'), pad=((10, 10), (10, 10))), 
         sg.Text(f'R${fees}', size=(55, 1), justification='right', font=('Arial', 16, 'bold'), key='fees_value')],
        [sg.Text('Total Investido:', justification='left', size=(15, 1), font=('Arial', 18, 'bold'), pad=((10, 10), (10, 10))), 
         sg.Text(f"R${total_invested}", size=(55, 1), justification='right', font=('Arial', 16, 'bold'), key='total_invested_value')],
        [sg.Button("Voltar", **button_style)]
    ]
    
    # Criando a janela
    window = sg.Window('Resultado do Cálculo 📊', layout=layout, size=window_size)

    while True:
        event, values = window.read()
        
        # Verificando se a janela foi fechada
        if event == sg.WINDOW_CLOSED:
            break
                
        # Voltando para a tela anterior ao clicar em "Voltar" ou pressionar Esc
        elif event == "Voltar" or event == 'Escape:27':
            window.close()
            Information_for_calculations.data_base()

    window.close()
