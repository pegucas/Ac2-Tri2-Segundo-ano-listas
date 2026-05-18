from menu import Menu, Ifs
EscolhaMenu = 0

while EscolhaMenu != 8:
    Menu()

    EscolhaMenu = int(input("Qual sera a opção?: "))

    if EscolhaMenu == 1:
        print("OK")
    elif EscolhaMenu == 2:
        print("Beleza")
    elif EscolhaMenu == 3:
        print("joia")
    elif EscolhaMenu == 4:
        print("Ta")
    elif EscolhaMenu == 5:
        print("Kay")
    elif EscolhaMenu == 6:
        print("Ta bom")
    elif EscolhaMenu == 7:
        print("Sim")
    else:
        print("Vazando daqui...")