def numeros_na_linha(linha: str):
    digit_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    str_number = {digit:linha.index(digit) for digit in digit_map if digit in linha}
    print(str_number)
    first_position_digit = ""
    for digit in digit_map:
        if digit in linha:
            index = linha.index(digit)
            # linha = linha.replace(digit, str(digit_map[digit]))
            min_value = min(str_number.values())
            max_value = max(str_number.values())
            
            linha = linha.replace(digit, str(digit_map[digit]))
    
    digits = [number for number in linha if number.isdigit()]

    return f"{digits[0]}{digits[-1]}"
