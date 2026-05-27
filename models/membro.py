from dataclasses import dataclass, field
from datetime import date


@dataclass
class Membro:
    """Entidade Membro da associação aeronáutica."""
    nome: str
    cpf: str
    email: str
    telefone: str
    data_ingresso: str = field(default_factory=lambda: date.today().isoformat())
    id: int = 0

    def to_dict(self) -> dict:
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf,
                "email": self.email, "telefone": self.telefone, "data_ingresso": self.data_ingresso}

    @staticmethod
    def from_dict(data: dict) -> "Membro":
        return Membro(id=data["id"], nome=data["nome"], cpf=data["cpf"],
                      email=data["email"], telefone=data["telefone"], data_ingresso=data["data_ingresso"])
