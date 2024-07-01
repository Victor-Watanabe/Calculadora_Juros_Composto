import PySimpleGUI as sg
import formula
import format_capital
import format_percentage   
import format_month

def data_base():
    sg.theme('reddit')

    # Largura x Altura em pixels
    window_size = (660, 330)  

    # Personalizando os Estilos de botões
    button_style = {'size': (60, 1), 'font': ('Times New Roman', 15, 'bold')}

    # Criando o Layout da Interface
    layout = [
    [sg.Text(
        'Dados Para Base de Cálculos', 
        justification='center', 
        size=(60, 1),  
        font=('Times New Roman', 24, 'bold'),
        text_color='black',
        pad=((0, 0), (1, 26))  
    )],
    [sg.Text('Capital Inicial:', justification='left', size=(25, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
     sg.Input(key='starting_capital', size=(45, 1), enable_events=True, justification='right', font=('Times New Roman', 16), text_color='black', tooltip='Informe o capital inicial', pad=((0, 0), (5, 10)))],
    [sg.Text('Porcentagem de Juros ao Mês:', justification='left', size=(25, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
     sg.Input(key='percentage_fees', size=(45, 1), enable_events=True, justification='right', font=('Times New Roman', 16), text_color='black', tooltip='Informe os juros ao mês (Ex: 10%)', pad=((0, 0), (5, 10)))],
    [sg.Text('Tempo de Investimento:', justification='left', size=(25, 1), font=('Times New Roman', 18), pad=((0, 10), (5, 10))), 
     sg.Input(key='time_in_mounths', size=(45, 1), enable_events=True, justification='right', font=('Times New Roman', 16), text_color='black', tooltip='Informe o Tempo Total de Investimento', pad=((0, 0), (5, 10)))],
    [sg.Text('Nota: Todos os valores devem ser compatíveis com informações ao mês. Se os \nvalores fornecidos estiverem em outra medida de tempo, Comprometerá o Cálculo!', 
             text_color='red', size=(70, 2), font=('Times New Roman', 13, 'bold'), pad=((0, 0), (10, 10)))],
    [sg.Text('', size=(54, 1)), sg.Button("Calcular", **button_style), sg.Text('')]
    ]
    
    # Apresentando a interface
    window = sg.Window('Calcule seu Juros Composto 📊.', layout=layout, size=window_size, return_keyboard_events=True, use_default_focus=False)

    while True:
        event, values = window.read()
        
        # Configurando o Botão de Close.
        if event == sg.WINDOW_CLOSED:
            break

        # Se o Evento CALCULAR for acionado.
        elif event in ('Calcular', 'Return', 'Return:36', 'Enter:13', '\r', 'Enter:108'):
            starting_capital_formatted = format_capital.format_currency(values['starting_capital'])
            percentage_fees = format_percentage.format_percentage(values['percentage_fees'])
            time_in_mounths = values['time_in_mounths']

            # Se Faltar Preencher algum campo!
            if not starting_capital_formatted or not percentage_fees or not time_in_mounths: 
                print("Faltou Preencher Campo!")

            else:
                # Fechar a janela antes de chamar a função de cálculo
                window.close()
                
                # Chamar a função para calcular usando os valores formatados
                formula.identify_formula()

            # Evento para formatar o valor assim que o usuário terminar de inserir
        elif event == 'starting_capital':  
            value_typed = values['starting_capital']
            value_formatted, number_float = format_capital.format_currency(value_typed)
            
            # Atualiza o campo com o valor formatado
            window['starting_capital'].update(value_formatted)  
        
        # Evento para formatar o valor assim que o usuário terminar de inserir
        elif event == 'percentage_fees':  
            percentage_typed = values['percentage_fees']
            percentage_formatted, percentage_float = format_percentage.format_percentage(percentage_typed)
            
            # Atualiza o campo com o valor formatado
            window['percentage_fees'].update(percentage_formatted)  

        # Configurando se Caso o usuário pressionar o botão BackSpace
        elif event == 'BackSpace:8' and window.find_element_with_focus() == window['percentage_fees'] or event == "Delete:46" and window.find_element_with_focus() == window['percentage_fees']:
            try: 
                index = percentage_formatted.index(",")
                percentage_formatted = percentage_formatted[:-2] + percentage_formatted[-1]
                percentage_formatted = percentage_formatted.replace(percentage_formatted[index],"")
                
                if len(percentage_formatted) == 4:
                    percentage_formatted = (f"0{percentage_formatted[0]},{percentage_formatted[-3:]}")

                elif len(percentage_formatted) == 3:
                    percentage_formatted = (f"0,{percentage_formatted}")

                elif len(percentage_formatted) > 4:
                    percentage_formatted = percentage_formatted[:-3] + "," + percentage_formatted[-3:]
                    
                else: 
                    percentage_formatted = "0,00%"

                # Atualiza o campo com o valor formatado
                window['percentage_fees'].update(percentage_formatted)  
                
                percentage_float = percentage_formatted
                percentage_float = percentage_float.replace("%", "").replace(",",".")
                percentage_float = float(percentage_float)

            except: 
                percentage_float = 0.0
                percentage_formatted = "0,0%"

        # Evento para formatar o valor assim que o usuário terminar de inserir
        elif event == 'time_in_mounths':  
            mounth_typed = values['time_in_mounths']
            month_formatted, month = format_month.format_month(mounth_typed)
            window["time_in_mounths"].update(month_formatted)
               

        elif event == 'BackSpace:8' and window.find_element_with_focus() == window['time_in_mounths'] or event == "Delete:46" and window.find_element_with_focus() == window['time_in_mounths']:
            if month_formatted[0] == "1" and month_formatted[1] == " ":
                month_formatted = "0 Meses"
                month = 0 
                window["time_in_mounths"].update(month_formatted)
                
            else:
                month_string = month_formatted[-6:]
                number_strings_month = month_formatted[:-7]
                month_formatted= number_strings_month + month_string
                window["time_in_mounths"].update(month_formatted)     
                try:
                    month = int(number_strings_month)     

                except:
                    month = 0
                
        elif event.startswith('Escape:27'):
            break
    
    window.close()

# Chamando a função principal
if __name__ == "__main__":
    data_base()

# Verificar, Pois está dando erro quando efetuado o número depois de acrescer o
# Variaveis que serão Utilizadas para equação: Percentage_Float e number_float.
# Arrumar o arquivo Fomrat_months seguindo os demais arquivos.