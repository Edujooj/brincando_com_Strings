import os


def inicio():
    # strip() função responsavel por remover caracteres ou espaços
    texto = input("digite algo ~> ").strip()

    piramede_vertical(texto)


def piramede_vertical(texto):
    tex = ""
    for t in texto:
        tex += t
        print(f"{" "*(len(texto)-len(tex))}{tex}|{tex}")
    
    for i in range(len(texto) - 1, -1, -1): #começo, fim, acréscimo
        print(f"{" "*(len(texto)-i)}{texto[:i]}|{texto[:i]}")   #text[:4] pegue os 4 primeiros caracteres
                                                                #text[7:] pegue todos os caracteres apartir do index 7
def repitir():
    try:
        if input("repitir? ~> ").lower() == 's':
            __main__()
    except:
        repitir()


def __main__():
    os.system("cls")
    inicio()
    repitir()


if __name__ == "__main__":
    __main__()
