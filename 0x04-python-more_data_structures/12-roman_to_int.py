#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    suma = 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for rec in range(0, len(roman_string)):
        if rec == len(roman_string) - 1:
            suma += conv[roman_string[rec]]
        elif conv[roman_string[rec]] >= conv[roman_string[rec + 1]]:
            suma += conv[roman_string[rec]]
        elif conv[roman_string[rec]] < conv[roman_string[rec + 1]]:
            suma -= 10**(len(str(conv[roman_string[rec]])) - 1)
    return (suma)
