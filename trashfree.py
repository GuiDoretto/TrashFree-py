def coletar_dados_usuario():
    nome = input("Digite seu nome: ")
    endereco = input("Digite seu endereço: ")
    tipo_lixo = input("Digite o tipo de lixo: ")
    data = input("Digite a data de agendamento: ")

    # Aqui você pode adicionar validações e tratamento de erros, se necessário

    return nome, endereco, tipo_lixo, data


def verificar_disponibilidade_coleta(data):
    # Aqui daria para implementar a lógica para verificar a disponibilidade da coleta com base na data fornecida pelo usuário
    disponibilidade = True  # Exemplo de valor de retorno, você pode ajustar conforme necessário
    return disponibilidade


def calcular_melhor_rota(endereco):
    # Aqui teria que implementar a lógica para calcular a melhor rota com base no endereço fornecido pelo usuário
    rota = "Rua A -> Rua B -> Rua C"  # Exemplo de valor de retorno, você pode ajustar conforme necessário
    return rota


def exibir_resumo_operacao(nome, endereco, tipo_lixo, data, rota):
    print("--- Resumo da Operação ---")
    print("Nome: ", nome)
    print("Endereço: ", endereco)
    print("Tipo de lixo: ", tipo_lixo)
    print("Data de agendamento: ", data)
    print("Melhor rota: ", rota)


def exibir_coletas_agendadas(coletas):
    if len(coletas) == 0:
        print("Não há coletas agendadas.")
    else:
        print("--- Coletas Agendadas ---")
        for i, coleta in enumerate(coletas):
            print(f"Coleta {i+1}:")
            print("Nome: ", coleta["nome"])
            print("Endereço: ", coleta["endereco"])
            print("Tipo de lixo: ", coleta["tipo_lixo"])
            print("Data de agendamento: ", coleta["data"])
            print("Melhor rota: ", coleta["rota"])
            print("------------------------")


# Função principal
def main():
    coletas_agendadas = []  # Lista para armazenar as coletas agendadas

    while True:
        print("----- MENU -----")
        print("1. Agendar coleta")
        print("2. Verificar coletas agendadas")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome, endereco, tipo_lixo, data = coletar_dados_usuario()
            disponibilidade = verificar_disponibilidade_coleta(data)
            if disponibilidade:
                rota = calcular_melhor_rota(endereco)
                coleta = {
                    "nome": nome,
                    "endereco": endereco,
                    "tipo_lixo": tipo_lixo,
                    "data": data,
                    "rota": rota
                }
                coletas_agendadas.append(coleta)
                exibir_resumo_operacao(nome, endereco, tipo_lixo, data, rota)
            else:
                print("Desculpe, não há disponibilidade para a data selecionada.")
        elif opcao == "2":
            exibir_coletas_agendadas(coletas_agendadas)
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite um número válido.")


if __name__ == "__main__":
    main()