import os

def inicio():
    os.system('cls')

    text = input("digite um texto\n~> ")
    textoFinal = []

    for letra in text:
        textoFinal.append(letra)

    print("texto 'empacotado': ")
    print(textoFinal, end="\n\n") # Por padrão, o end recebe "\n" (uma quebra de linha)

    print("texto 'desempacotado': ")
    print(*textoFinal, sep=" ", end="\n\n") # Por padrão, o sep recebe " " (um espaço)

    print("texto com sep alterado: ")
    print(*textoFinal, sep='\n')

def repitir():
    try:
        if input("Repitir? ~> ").lower() == 's':
            __main__()
    except:
        repitir()
        
def __main__():
    inicio()
    repitir()

if __name__ == "__main__":
    __main__()