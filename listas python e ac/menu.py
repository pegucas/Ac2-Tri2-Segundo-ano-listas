def Menu():
    print("Escolha uma opção abaixo:")
    print("1 - Cadastrar um novo jogador")
    print("2 - Mostrar jogadores cadastrados")
    print("3 - Mostrar relatorio")
    print("4 - Pesquisar jogador")
    print("5 - Alterar uma informação")
    print("6 - Remover um jogador")
    print("7 - Mostrar estatisticas gerais")
    print("8 - Encerrar programa")

def Ifs():
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