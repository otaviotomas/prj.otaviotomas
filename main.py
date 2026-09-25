# Lista que armazenará os ativos em memória
ativos = []


def cadastrar_ativo():
    print("\n--- CADASTRO DE ATIVO ---")

    # Validação do ID
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo: "))
            break
        except ValueError:
            print("Erro: o ID deve ser um número inteiro.")

    # Validação do nome
    while True:
        nome = input("Digite o nome do equipamento: ").strip()
        if nome:
            break
        print("Erro: o nome não pode ficar vazio.")

    # Validação do responsável
    while True:
        responsavel = input("Digite o responsável: ").strip()
        if responsavel:
            break
        print("Erro: o responsável não pode ficar vazio.")

    # Cria o dicionário do ativo
    ativo = {
        "id": id_ativo,
        "nome": nome,
        "responsavel": responsavel
    }

    # Adiciona na lista
    ativos.append(ativo)

    print("\nAtivo cadastrado com sucesso!")


def listar_ativos():
    print("\n--- LISTA DE ATIVOS ---")

    if len(ativos) == 0:
        print("Não há ativos cadastrados.")
        return

    for ativo in ativos:
        print("\n-------------------------")
        print(f"ID: {ativo['id']}")
        print(f"Nome: {ativo['nome']}")
        print(f"Responsável: {ativo['responsavel']}")


def exibir_menu():
    while True:
        print("\n" + "=" * 40)
        print("SISTEMA DE CADASTRO DE ATIVOS DE TI")
        print("=" * 40)
        print("1 - Cadastrar ativo")
        print("2 - Listar ativos")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_ativo()

        elif opcao == "2":
            listar_ativos()

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    exibir_menu()