def menu_principal():
    print(
        """Loja de Jogos
          Escolha uma opção:
          1 - Gerenciar Clientes
          2 -  Gerenciar Jogos
          3 -  Gerenciar Vendas
          4 - Sair"""
    )


def menu_cliente():
    print(
        """Loja de Jogos
          Escolha uma opção:
          1 - Cadastrar Cliente
          2 - Listar Clientes
          3 - Buscar Cliente
          4 - Atualizar Cliente
          5 - Excluir Cliente
          6 - Sair"""
    )


def menu_jogo():
    print(
        """Loja de Jogos
          Escolha uma opção:
          1 - Cadastrar Jogo
          2 - Listar Jogos
          3 - Buscar Jogo
          4 - Atualizar Jogo
          5 - Excluir Jogo
          6 - Sair"""
    )


def menu_venda():
    print(
        """Loja de Jogos
          Escolha uma opção:
          1 - Vender Jogo
          2 - Listar Vendas
          3 - Sair"""
    )


def cadastrar_cliente(clientes):
    identificador = input("Digite o ID do cliente: ")
    nome = input("Digite o nome do cliente: ")
    while True:
        try:
            idade = int(input("Digite a idade do cliente: "))
            break
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")
    clientes.append((identificador, nome, idade))
    print("Cliente cadastrado com sucesso!")


def listar_clientes(clientes):
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            identificador, nome, idade = cliente
            print(f"ID: {identificador}, Nome: {nome}, Idade: {idade}")


def buscar_cliente(clientes):
    id_desejado = input("Digite o ID do cliente que deseja buscar: ")
    for cliente in clientes:
        identificador, nome, idade = cliente
        if identificador == id_desejado:
            print(f"ID: {identificador}, Nome: {nome}, Idade: {idade}")
            break
    else:
        print("Cliente não encontrado.")


def atualizar_cliente(clientes):
    id_desejado = input("Digite o ID do cliente que deseja atualizar: ")
    for i, cliente in enumerate(clientes):
        identificador, nome, idade = cliente
        if identificador == id_desejado:
            novo_nome = input("Digite o novo nome do cliente: ")
            while True:
                try:
                    nova_idade = int(input("Digite a nova idade do cliente: "))
                    break
                except ValueError:
                    print("Idade inválida. Digite um número inteiro.")
            confirmar = input(
                f"Você tem certeza que deseja atualizar o cliente {nome} (s/n)? "
            )
            confirmar = confirmar.lower()
            if confirmar == "s":
                clientes[i] = (identificador, novo_nome, nova_idade)
                print("Cliente atualizado com sucesso!")
            break
    else:
        print("Cliente não encontrado.")


def excluir_cliente(clientes):
    id_desejado = input("Digite o ID do cliente que deseja excluir: ")
    for i, cliente in enumerate(clientes):
        identificador, nome, idade = cliente
        if identificador == id_desejado:
            confirmar = input(
                f"Você tem certeza que deseja excluir o cliente {nome} (s/n)? "
            )
            confirmar = confirmar.lower()
            if confirmar == "s":
                del clientes[i]
                print("Cliente excluído com sucesso!")
            break
    else:
        print("Cliente não encontrado.")


def cadastrar_jogo(jogos):
    identificador = input("Digite o ID do jogo: ")
    nome = input("Digite o nome do jogo: ")
    preco = input("Digite o preço do jogo: ")
    preco = preco.replace(",", ".")
    preco = float(preco)
    jogos.append((identificador, nome, preco))
    print("Jogo cadastrado com sucesso!")


def listar_jogos(jogos):
    if len(jogos) == 0:
        print("Nenhum jogo cadastrado.")
    else:
        for jogo in jogos:
            identificador, nome, preco = jogo
            print(f"ID: {identificador}, Nome: {nome}, Preço: {preco}")


def buscar_jogo(jogos):
    id_desejado = input("Digite o ID do jogo que deseja buscar: ")
    for jogo in jogos:
        identificador, nome, preco = jogo
        if identificador == id_desejado:
            print(f"ID: {identificador}, Nome: {nome}, Preço: {preco}")
            break
    else:
        print("Jogo não encontrado.")


def atualizar_jogo(jogos):
    id_desejado = input("Digite o ID do jogo que deseja atualizar: ")
    for i, jogo in enumerate(jogos):
        identificador, nome, preco = jogo
        if identificador == id_desejado:
            novo_nome = input("Digite o novo nome do jogo: ")
            novo_preco = input("Digite o novo preço do jogo: ")
            novo_preco = novo_preco.replace(",", ".")
            novo_preco = float(novo_preco)
            confirmar = input(
                f"Você tem certeza que deseja atualizar o jogo {nome} (s/n)? "
            )
            confirmar = confirmar.lower()
            if confirmar == "s":
                jogos[i] = (identificador, novo_nome, novo_preco)
                print("Jogo atualizado com sucesso!")
            break
    else:
        print("Jogo não encontrado.")


def excluir_jogo(jogos):
    id_desejado = input("Digite o ID do jogo que deseja excluir: ")
    for i, jogo in enumerate(jogos):
        identificador, nome, preco = jogo
        if identificador == id_desejado:
            confirmar = input(
                f"Você tem certeza que deseja excluir o jogo {nome} (s/n)? "
            )
            confirmar = confirmar.lower()
            if confirmar == "s":
                del jogos[i]
                print("Jogo excluído com sucesso!")
            break
    else:
        print("Jogo não encontrado.")


def vender_jogo(jogos, clientes, vendas):
    id_jogo = input("Digite o ID do jogo que deseja vender: ")
    id_cliente = input("Digite o ID do cliente que deseja comprar: ")
    for jogo in jogos:
        identificador_jogo, nome_jogo, preco_jogo = jogo
        if identificador_jogo == id_jogo:
            for cliente in clientes:
                identificador_cliente, nome_cliente, idade_cliente = cliente
                if identificador_cliente == id_cliente:
                    vendas.append((id_jogo, id_cliente))
                    print(
                        f"Venda realizada com sucesso! Jogo: {nome_jogo}, Cliente: {nome_cliente}"
                    )
                    break
            else:
                print("Cliente não encontrado.")
            break
    else:
        print("Jogo não encontrado.")


def listar_vendas(vendas, jogos, clientes):
    if len(vendas) == 0:
        print("Nenhuma venda realizada.")
    else:
        for venda in vendas:
            id_jogo, id_cliente = venda
            for jogo in jogos:
                identificador_jogo, nome_jogo, preco_jogo = jogo
                if identificador_jogo == id_jogo:
                    for cliente in clientes:
                        identificador_cliente, nome_cliente, idade_cliente = cliente
                        if identificador_cliente == id_cliente:
                            print(
                                f"Jogo: {nome_jogo}, Cliente: {nome_cliente}, Preço: {preco_jogo}"
                            )
                            break
                    break


def main():
    clientes = []
    jogos = []
    vendas = []

    while True:
        menu_principal()
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            while True:
                menu_cliente()
                opcao_cliente = input("Digite a opção desejada: ")
                if opcao_cliente == "1":
                    cadastrar_cliente(clientes)
                elif opcao_cliente == "2":
                    listar_clientes(clientes)
                elif opcao_cliente == "3":
                    buscar_cliente(clientes)
                elif opcao_cliente == "4":
                    atualizar_cliente(clientes)
                elif opcao_cliente == "5":
                    excluir_cliente(clientes)
                elif opcao_cliente == "6":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "2":
            while True:
                menu_jogo()
                opcao_jogo = input("Digite a opção desejada: ")
                if opcao_jogo == "1":
                    cadastrar_jogo(jogos)
                elif opcao_jogo == "2":
                    listar_jogos(jogos)
                elif opcao_jogo == "3":
                    buscar_jogo(jogos)
                elif opcao_jogo == "4":
                    atualizar_jogo(jogos)
                elif opcao_jogo == "5":
                    excluir_jogo(jogos)
                elif opcao_jogo == "6":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "3":
            while True:
                menu_venda()
                opcao_venda = input("Digite a opção desejada: ")
                if opcao_venda == "1":
                    vender_jogo(jogos, clientes, vendas)
                elif opcao_venda == "2":
                    listar_vendas(vendas, jogos, clientes)
                elif opcao_venda == "3":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
