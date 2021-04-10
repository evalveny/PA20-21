import abc

class Figura(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
      raise NotImplementedError()
    
    @abc.abstractmethod
    def perimetre(self):
      raise NotImplementedError()
    
    @abc.abstractmethod
    def llegeix(self):
      raise NotImplementedError()

    @abc.abstractmethod
    def __str__(self):
      raise NotImplementedError()
