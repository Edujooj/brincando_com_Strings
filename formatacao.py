import os

while True:
    os.system('cls')

    num = int(input("digite um numero ~> "))
    print("você digitou {}, o seu antecessor é {} e seu sucessor é {}\nA raiz quadrada é {:.2f}".format(num, num-1, num+1, num**(1/2)))

    if input("repitir? ~> ") != 's':
        break