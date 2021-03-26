"""
Sources:

https://www.youtube.com/watch?v=QaOdwYVp2ik


Description:

The singleton pattern makes sure that a class has only one instaciation.

It is often used when you don't wnat to repeat the instanciation of an
object several times on runtime since this might create issues (efficientcy,
availability, etc)

Participants:
- Singleton: Defines an inner static instance that is shared even if the
             constructor is called several times in runtime.
"""


from time import sleep
from typing import Optional
from datetime import datetime

class SingletonMeta(type):
    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class TimeSingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.now_cls = datetime.utcnow()

    def now_method(self):
        return datetime.utcnow()


if __name__ == '__main__':
    s1 = TimeSingleton()
    print(s1.now_cls)
    print(s1.now_method())

    print("Esperando 3 segundos...   \n")
    sleep(3)

    s2 = TimeSingleton()
    print(s2.now_cls)
    print(s2.now_method())