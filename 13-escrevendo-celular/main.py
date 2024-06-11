def key_letter(letter):
    if letter == "a":
        return "2"
    elif letter == "b":
        return "22"
    elif letter == "c":
        return "222"
    elif letter == "d":
        return "3"
    elif letter == "e":
        return "33"
    elif letter == "f":
        return "333"
    elif letter == "g":
        return "4"
    elif letter == "h":
        return "44"
    elif letter == "i":
        return "444"
    elif letter == "j":
        return "5"
    elif letter == "k":
        return "55"
    elif letter == "l":
        return "555"
    elif letter == "m":
        return "6"
    elif letter == "n":
        return "66"
    elif letter == "o":
        return "666"
    elif letter == "p":
        return "7"
    elif letter == "q":
        return "77"
    elif letter == "r":
        return "777"
    elif letter == "s":
        return "7777"
    elif letter == "t":
        return "8"
    elif letter == "u":
        return "88"
    elif letter == "v":
        return "888"
    elif letter == "w":
        return "9"
    elif letter == "x":
        return "99"
    elif letter == "y":
        return "999"
    elif letter == "z":
        return "9999"
    
    elif letter == " ":
        return "0"
    elif letter == " ":
        return "0"

def generic_function(text):
    text = text.lower()
    output = ""

    for letter in text:
        code = key_letter(letter)
        if output != "" and output[-1] in code:

            output = output + "_"

        

        output = output + code
    return output
    
