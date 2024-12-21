from abc import ABC, abstractmethod

class InterfaceConta(ABC):
    @abstractmethod
    def depositar(self, valor):
        pass