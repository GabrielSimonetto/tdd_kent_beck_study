from abc import ABC, abstractmethod

class TestCase(ABC):
    def __init__(self, name):
        self.was_run = None
        self.name = name
        self.was_set_up = False
        self.log = ""

    def run(self):
        self.set_up()
        exec(f"self.{self.name}()")
        print(f"{self.name} is working")
        self.teardown()

    # @abstractmethod
    # ainda nao funciona, WasRun eh muito diferente de TestCaseTest
    def set_up(self):
        pass

    # @abstractmethod
    def teardown(self):
        pass


class WasRun(TestCase):

    def set_up(self):
        self.was_run = False
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "
    
    def teardown(self):
        self.log += "teardown "
