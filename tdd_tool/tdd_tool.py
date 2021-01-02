from abc import ABC, abstractmethod

class TestCase(ABC):
    def __init__(self, name):
        self.was_run = None
        self.name = name
        self.was_set_up = False
        self.log = ""

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        exec(f"self.{self.name}()")
        print(f"{self.name} is working")
        self.teardown()
        return result

    # @abstractmethod
    # ainda nao funciona, WasRun eh muito diferente de TestCaseTest
    def set_up(self):
        pass

    # @abstractmethod
    def teardown(self):
        pass


class TestResult():
    def __init__(self):
        self.run_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return f"{self.run_count} run, 0 failed"


class WasRun(TestCase):

    def set_up(self):
        self.was_run = False
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    # we aren't catching this exception!
    # this makes it so our tests halt instead of carrying on.
    def test_broken_method(self):
        raise Exception

    def teardown(self):
        self.log += "teardown "
