
def format_currency(value):
    value_float = ''.join(filter(str.isdigit, str(value)))  # Remove todos os caracteres não numéricos

    value_string = str(value)
    
    # Verifica se o valor já tem um ponto decimal na posição correta
    if "," or "R$" or "." in value_string:
        value_string = value_string.replace(",","").replace("R$","").replace(".","")

    else:
        pass

    if len(value_string) == 0:
        value_formatted = f"0.0{value_string}"
        number_float = 0,{value_float}
    elif len(value_string) == 1:
        value_formatted = f"{value_string}"
        number_float = float(f"0.0{value_float}")
        if "0" in value_formatted[:-2]:
            value_formatted.replace(value_formatted[:-2],"")
    else:
        integer_part = value_string[:-2]
        decimal_part = value_string[-2:]
        integer_float = value_float[:-2]
        decimal_float = value_float[-2:]
        value_formatted = "R$" + integer_part + "," + decimal_part
        number_float = float(f"{integer_float}.{decimal_float}")

    return value_formatted, number_float