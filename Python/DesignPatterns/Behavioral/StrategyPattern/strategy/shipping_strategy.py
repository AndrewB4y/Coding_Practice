from abc import ABCMeta, abstractmethod

class AbsStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, orderd):
        """ Calculate shipping cost """