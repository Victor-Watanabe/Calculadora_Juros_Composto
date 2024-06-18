
def format_percentage(value):
    value_float = ''.join(filter(str.isdigit, str(value)))  # Remove todos os caracteres não numéricos

    value_string = str(value)
    
    # Verifica se o valor já tem um ponto decimal na posição correta
    if "," or "%" or "." in value_string:
        value_string = value_string.replace(",","").replace("%","").replace(".","")

    else:
        pass

    if len(value_string) == 0:
        percentage_formatted = "0.00%"
        percentage_float = 0.00
    elif len(value_string) == 1:
        percentage_formatted = f"{value_string}"
        percentage_float = float(f"0.0{value_float}")
        if "0" in percentage_formatted[:-2]:
            percentage_formatted.replace(percentage_formatted[:-2],"")
    else:
        integer_part = value_string[:-2]
        decimal_part = value_string[-2:]
        integer_float = value_float[:-2]
        decimal_float = value_float[-2:]
        percentage_formatted = integer_part + "," + decimal_part + "%"
        percentage_float = float(f"{integer_float}.{decimal_float}")
        
    return percentage_formatted, percentage_float