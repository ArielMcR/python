import json, os
from abc import ABC, abstractmethod
from typing import List
from models.membro import Membro


class PersistenciaStrategy(ABC):
    """Interface Strategy para persistência. Aplicação de OCP e DIP."""
    @abstractmethod
    def carregar(self) -> List[Membro]: pass
    @abstractmethod
    def salvar(self, membros: List[Membro]) -> None: pass


class JsonPersistencia(PersistenciaStrategy):
    """Implementação concreta: persiste dados em arquivo JSON."""
    def __init__(self, caminho: str = "membros.json"):
        self._caminho = caminho

    def carregar(self) -> List[Membro]:
        if not os.path.exists(self._caminho):
            return []
        with open(self._caminho, "r", encoding="utf-8") as f:
            return [Membro.from_dict(d) for d in json.load(f)]

    def salvar(self, membros: List[Membro]) -> None:
        with open(self._caminho, "w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in membros], f, ensure_ascii=False, indent=2)
