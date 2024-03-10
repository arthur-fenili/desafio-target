"""

5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""


def inverter(string_informada):
    string_final = ""
    for i in range(len(string_informada) - 1, -1, -1):
        string_final += string_informada[i]
    return string_final


string_informada = input("Digite a string para ser invertida: ")

print(f"Esta é a string invertida: {inverter(string_informada)}")
