import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from services.membro_service import MembroService
from strategies.persistencia import JsonPersistencia
from utils.formatador import formatar_membro


def menu():
    print("\n=== Associação Aeronáutica — Membros ===")
    print("1 - Cadastrar membro")
    print("2 - Listar membros")
    print("3 - Buscar por CPF")
    print("4 - Editar membro")
    print("5 - Excluir membro")
    print("0 - Sair")


def main():
    # Injeção de dependência: troque JsonPersistencia por outra estratégia sem alterar o serviço
    service = MembroService(JsonPersistencia("membros.json"))

    while True:
        menu()
        opcao = input("Opção: ").strip()

        if opcao == "1":
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                m = service.cadastrar(nome, cpf, email, telefone)
                print(f"\nMembro cadastrado!\n{formatar_membro(m)}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            membros = service.listar()
            if not membros:
                print("Nenhum membro cadastrado.")
            else:
                print(f"\n{len(membros)} membro(s) encontrado(s):")
                for m in membros:
                    print(f"\n{formatar_membro(m)}\n  {'─'*30}")

        elif opcao == "3":
            cpf = input("CPF: ")
            m = service.buscar_por_cpf(cpf)
            if m:
                print(f"\n{formatar_membro(m)}")
            else:
                print("Membro não encontrado.")

        elif opcao == "4":
            try:
                id = int(input("ID do membro: "))
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                telefone = input("Novo telefone: ")
                m = service.editar(id, nome, email, telefone)
                print(f"Membro atualizado!\n{formatar_membro(m)}")
            except (ValueError, TypeError) as e:
                print(f"Erro: {e}")

        elif opcao == "5":
            try:
                id = int(input("ID do membro: "))
                service.excluir(id)
                print("Membro excluído com sucesso.")
            except (ValueError, TypeError) as e:
                print(f"Erro: {e}")

        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
