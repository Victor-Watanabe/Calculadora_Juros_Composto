def format_month(value):
    value_float = ''.join(filter(str.isdigit, str(value)))  # Remove todos os caracteres não numéricos

    value_string = ''.join(filter(str.isdigit, str(value)))
    
    # Verifica se o valor já tem um ponto decimal na posição correta
    if "Meses" in value_string:
        value_string = value_string.replace("Meses","")

    elif "Mês" in value_string:
        value_string = value_string.replace("Mês","")

    elif len(value_string) == "0":
        month_formatted = "0 Meses"
        month = 0
        return month_formatted, month
    
    elif value_string == "1":
        month_formatted = f"{value_string} Mês"
        month = int(value_float)
        if "0" in month_formatted[0] and len(month_formatted) > 1:
            month_formatted = month_formatted.replace(month_formatted[0],"")
        return month_formatted, month

    elif len(value_string) > 1 and value_string[0] == "0":
        month_formatted = value_string.replace(value_string[0],"")
        month_formatted = month_formatted + "Meses"
        month = int(value_float)
        
        if month_formatted == "1Meses":
            month_formatted = f"{value_string[1]} Mês"

        return month_formatted, month
        
    else:
        try:
            month_formatted = f"{value_string} Meses"
            month = int(value_float)

        except: 
            month_formatted = "0 Meses"
            month = 0
            
        return month_formatted, month

