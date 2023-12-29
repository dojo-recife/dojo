def numeros_na_linha(text):
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
    numbers = digit_map.keys()
    value = ''
    find_numbers = []
    

    for c in text:
        if c.isdigit():
            find_numbers.append(int(c))
            value = ''
            continue

        value += c
        reverse = ''
        for x in range(len(value), 0, -1):
            reverse = value[x-1:]
            if reverse in numbers:
                find_numbers.append(reverse)
                value = ''
                break

        if value in numbers:
            find_numbers.append(value)
    
    find_numbers = [num.replace(num, str(digit_map[num])) 
                    if not str(num).isdigit() else str(num) 
                    for num in find_numbers]
    
    return str(find_numbers[0]) + str(find_numbers[-1])
    
    
    