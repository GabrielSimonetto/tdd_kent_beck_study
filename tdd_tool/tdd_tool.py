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
        try:
            exec(f"self.{self.name}()")
        except:
            result.test_failed()
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
        self.error_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self):
        return f"{self.run_count} run, {self.error_count} failed"


class WasRun(TestCase):

    def set_up(self):
        self.was_run = False
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def test_broken_method(self):
        raise Exception

    def teardown(self):
        self.log += "teardown "
