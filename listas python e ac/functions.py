Nomes = []
Partidas = []
Gols = []
Media = []

def Cadastro():

    nome = input("Diga o nome do Jogdor: ").upper()
    QuantPart = int(input("Quantas partidas ele jogou: "))
    QuantGols = int(input("Diga a quantidade de gols: "))
    media = QuantGols / QuantPart

    Nomes.append(nome)
    Partidas.append(QuantPart)
    Gols.append(QuantGols)
    Media.append(media)

def Cadastrados():

    if len(Nomes) == 0:
        print("Não esxiste jogadores cadastrados")
    else:
        print("Aqui todos os jogadores cadastrados:")
        print(Nomes)
        print(f"Existem {len(Nomes)} no total")

def relatorioCompleto():
    print("Relatorio de todos os cadastrados (Para informações de um especifico digitar 4):")

    for i in range(len(Nomes)):
        print(f"Nome: {Nomes[i]} || Partidas: {Partidas[i]} || Gols: {Gols[i]}")

def PesquisaJogador():

    if len(Nomes) == 0:
        print("Nada aqui no momento")
    else:
        Pesquisa = input("Digite o nome do Jogador: ").upper()

        if Pesquisa in Nomes:
            pos = Nomes.index(Pesquisa)

            print("Jogador:", {Nomes[pos]})

            print("Partidas:", {Partidas[pos]})

            print("Gols:", {Gols[pos]})

            print(f"Média do jogador: {Media[pos]:.2f} em porcentagem numeral")

            if Media[pos] <= 0.35:
                print("O jogador PRECISA MELHORAR")

            elif Media[pos] <= 0.67:
                print("Com base nisso o jogador é BOM")

            elif Media[pos] <= 0.87:
                print("Com base nisso o jogador é EXCELENTE")

            elif Media[pos] <= 1:
                print("Com base nisso o jogador é LENDARIO")

            else:
                print("O jogador é pessimo e precisa MELHORAR MUITO MESMO")
        else:
            print("Não foi encontrado")

def AlterarInfo():
    if len(Nomes) == 0:
        print("Nenhum jogador para alterar")

    else:
        jog = input("Digite o nome do jogador: ").upper()

        if jog in Nomes:
            print("-" * 45)
            print("Oque voce gostaria de modificar")
            print("1 - Nome")
            print("2 - Partidas")
            print("3 - Gols")
            print("4 - Terminar")
            print("-" * 45)

            Selection = 0

            while Selection !=4: 
                Selection = int(input("Selecione uma opção: "))

                if Selection == 1:
                    pos = Nomes.index(jog)

                    Novo_nome = input("Que seria o novo nome?: ").upper()
                    Nomes[pos] = Novo_nome
                    jog = Novo_nome

                    print(f"Nome mudado para {Nomes[pos]}")

                elif Selection == 2:
                    pos = Nomes.index(jog)

                    Novos_jogos = int(input("Qual sera a nova quantidade de partidas?: "))
                    Partidas[pos] = Novos_jogos

                    QuantGols = 0
                    QuantGols = Gols[pos]

                    Novamedia = QuantGols / Novos_jogos

                    Media[pos] = Novamedia

                    print(f"Quantidade substituida para {Partidas[pos]}")

                elif Selection == 3:
                    pos = Nomes.index(jog)

                    Novos_gols = int(input("Qual sera a nova quantidade de gols?: "))
                    Gols[pos] = Novos_gols

                    QuantPart = 0
                    QuantPart = Partidas[pos]

                    Novamedia = Novos_gols / QuantPart

                    Media[pos] = Novamedia

                    print(f"Quantidade substituida para {Gols[pos]}")

                else:
                    print("Terminando... ")
        else:
            print("Erro 404: Não encontrado")

def Remover():
    if len(Nomes) == 0:
        print("Não tem jogadores cadastrados")
    
    else:
        Removido = input("Coloque o nome do jogador: ").upper()
        if Removido in Nomes:

            Certeza = int(input("Voce tem certeza mesmo? (1 - Sim || 2 - Não): "))

            if Certeza == 1:
                Nomes.remove(Removido)
                Partidas.remove(Removido)
                Gols.remove(Removido)
                Media.remove(Removido)

                print("Jogador removido")

            else:
                print("Cancelando operação...")

        else:
            print("Não foi encontrado")

def Estatisticas():
    if len(Nomes) == 0:
        print("Não tem ninguem registrado")

    else:
        print(f"Existem {len(Nomes)} jogadores cadastrados.")
        print(f"A melhor média foi: {max(Media)}")
        print(f"E a pior média foi: {min(Media)}")

        mediaDeTodos = sum(Gols) / sum(Partidas)
        print(f"A média geral contando todo mundo foi: {mediaDeTodos:.2f}")

        pos = max(Media)
        melhor = Media.index(pos)
        melhor = Nomes[melhor]

        print(f"A melhor média e portanto desempenho foi do {melhor}")

        print("Outros jogadores notaveis foram:")

        for i in range(len(Nomes)):
            if Media[i] >= 0.87:
                print(f"{Nomes[i]}: {Media[i]:.2f}")

        print("E outros que não são tão notaveis assim... (Se tiver ninguem UaU todos são uteis o suficiente):")

        for i in range(len(Nomes)):
            if Media[i] <= 0.30:
                print(f"{Nomes[i]}: {Media[i]:.2f}")
        
        print("E apenas isso obrigado")
