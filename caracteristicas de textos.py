import os

def inicio():
    os.system('cls')
    
    text = input("digite algo ~> ") #A função input só retorna str

    print("O tipo primitivo desse valor ", type(text))
    print("Só tem espaço? ", text.isspace())
    print("Só tem número? ", text.isnumeric())
    print("É alfabetico? ", text.isalpha())
    print("É alfanumerico? ", text.isalnum()) #se possuir letras ou números, retorna verdadeiro 
    print("Está em maiúculas? ", text.isupper())
    print("Está em minúsculas? ", text.islower())
    print("Está capitalizada? ", text.istitle()) #se tiver letras maiúsculas e minúsculas, retorna verdadeiro

def repitir(): #Validação e reinicialização
    try:
        if input("repitir? ~> ").lower() == 's':
            main()

    except:
         repitir()


def main():
    inicio()
    repitir()

if __name__ == "__main__":
    main()