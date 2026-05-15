form abc import ABC,abstracthod
class Absclass(ABC):
    def print(self,x):
        print("passed value:",x)

    @Abstractmethod
    def task(self):
        print("we are inside Absclass task")
class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")
obj = test_class()
obj.task()
obj.print(100)
