from models.membro import Membro

def formatar_membro(m: Membro) -> str:
    return (f"  ID: {m.id} | Nome: {m.nome}\n"
            f"  CPF: {m.cpf} | Tel: {m.telefone}\n"
            f"  Email: {m.email} | Ingresso: {m.data_ingresso}")
