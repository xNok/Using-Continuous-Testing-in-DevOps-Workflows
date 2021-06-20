from abc import ABC, abstractmethod

class RepoBase(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def list(self):
        pass