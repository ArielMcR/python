from typing import List, Optional
from models.membro import Membro
from strategies.persistencia import PersistenciaStrategy


class MembroService:
    """
    Regras de negócio para membros.
    SRP: apenas lógica de negócio.
    DIP: depende da abstração PersistenciaStrategy.
    """
    def __init__(self, persistencia: PersistenciaStrategy):
        self._persistencia = persistencia
        self._membros: List[Membro] = persistencia.carregar()
        self._proximo_id = max((m.id for m in self._membros), default=0) + 1

    def _salvar(self): self._persistencia.salvar(self._membros)

    def cadastrar(self, nome: str, cpf: str, email: str, telefone: str) -> Membro:
        if self.buscar_por_cpf(cpf):
            raise ValueError(f"CPF {cpf} já cadastrado.")
        membro = Membro(nome=nome, cpf=cpf, email=email, telefone=telefone, id=self._proximo_id)
        self._proximo_id += 1
        self._membros.append(membro)
        self._salvar()
        return membro

    def listar(self) -> List[Membro]:
        return self._membros.copy()

    def buscar_por_cpf(self, cpf: str) -> Optional[Membro]:
        cpf_limpo = cpf.replace(".", "").replace("-", "")
        for m in self._membros:
            if m.cpf.replace(".", "").replace("-", "") == cpf_limpo:
                return m
        return None

    def buscar_por_id(self, id: int) -> Optional[Membro]:
        return next((m for m in self._membros if m.id == id), None)

    def editar(self, id: int, nome: str, email: str, telefone: str) -> Membro:
        membro = self.buscar_por_id(id)
        if not membro:
            raise ValueError(f"Membro ID {id} não encontrado.")
        membro.nome = nome; membro.email = email; membro.telefone = telefone
        self._salvar()
        return membro

    def excluir(self, id: int) -> None:
        membro = self.buscar_por_id(id)
        if not membro:
            raise ValueError(f"Membro ID {id} não encontrado.")
        self._membros.remove(membro)
        self._salvar()
