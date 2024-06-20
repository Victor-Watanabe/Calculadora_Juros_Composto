def format_month(value):
    value_float = ''.join(filter(str.isdigit, str(value)))  # Remove todos os caracteres não numéricos

    value_string = ''.join(filter(str.isdigit, str(value)))
    
    # Verifica se o valor já tem um ponto decimal na posição correta
    if "Meses" in value_string:
        value_string = value_string.replace("Meses","")

    if value_string == "1":
        month_formatted = f"{value_string} Mês"
        month = int(value_float)


    else:
        month_formatted = f"{value_string} Meses"
        month = int(value_float)

    return month_formatted, month