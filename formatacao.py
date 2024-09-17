import os

def inicio():
    os.system('cls')

    num = int(input("digite um numero ~> "))
    print("você digitou {}, o seu antecessor é {} e seu sucessor é {}\nA raiz quadrada é {:.2f}".format(num, num-1, num+1, num**(1/2)))

def repitir():
    try:
        if input("repitir? ~> ").lower() == 's':
            __main__()
    except:
        repitir()
    
def __main__():
    inicio()
    repitir()

if __name__ == "__main__":
    __main__()