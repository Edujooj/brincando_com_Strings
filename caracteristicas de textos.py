import os

while True:
    os.system('cls')

    text = input("digite algo ~> ") #A função input só retorna str

    print("O tipo primitivo desse valor ", type(text))
    print("Só tem espaço? ", text.isspace())
    print("Só tem número? ", text.isnumeric())
    print("É alfabetico? ", text.isalpha())
    print("É alfanumerico? ", text.isalnum())
    print("Está em maiúculas? ", text.isupper())
    print("Está em minúsculas? ", text.islower())
    print("Está capitalizada? ", text.istitle())

    if input("repitir? ~> ") != 's':
        break