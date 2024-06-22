
def format_percentage(value):
    value_float = ''.join(filter(str.isdigit, str(value)))  # Remove todos os caracteres não numéricos

    value_string = ''.join(filter(str.isdigit, str(value)))
    
    # Verifica se o valor já tem um ponto decimal na posição correta
    if "," or "%" or "." in value_string:
        value_string = value_string.replace(",","").replace("%","").replace(".","")

    else:
        pass

    if len(value_string) == 0:
        percentage_formatted = "0.00%"
        percentage_float = 0.00

    elif len(value_string) == 1:
        percentage_formatted = f"0,0{value_string}%"
        percentage_float = float(f"0.0{value_float}")
    
    elif len(value_string) == 4 and "0" in value_string[:-2]:
            if value_string[1] != "0":
                integer_part = value_string[:-2]
                decimal_part = value_string[-2:]
                integer_float = value_float[:-2]
                decimal_float = value_float[-2:]
                if "0" in integer_part[0]:
                    integer_part = integer_part.replace(integer_part[0],"") 
                percentage_formatted = integer_part + "," + decimal_part + "%"
                percentage_float = float(f"{integer_float}.{decimal_float}")
                
                                
                return percentage_formatted, percentage_float
            
            else:
                if value_string[0] != "0":
                    value_string = value_string.replace(value_string[-2:],"")
                    value_float = value_float.replace(value_float[-2:],"")
                    percentage_formatted = f"{value_string},00%"
                    percentage_float = float(f"{value_float}.00")



                else:
                    value_string = value_string.replace(value_string[:-2],"")
                    value_float = value_float.replace(value_float[:-2],"")
                    percentage_formatted = f"0,{value_string}%"
                    percentage_float = float(f"0.{value_float}")

    else:
        integer_part = value_string[:-2]
        decimal_part = value_string[-2:]
        integer_float = value_float[:-2]
        decimal_float = value_float[-2:]
        percentage_formatted = integer_part + "," + decimal_part + "%"
        percentage_float = float(f"{integer_float}.{decimal_float}")
        try:
            if "0" in percentage_formatted[0]:
                percentage_formatted = percentage_formatted.replace(percentage_formatted[0], "")

        except: pass
        if percentage_formatted[0] == ",":
            percentage_formatted = "0" + percentage_formatted
        
    return percentage_formatted, percentage_float