class TestCase():
    def __init__(self, name):
        self.was_run = None
        self.name = name
        self.was_set_up = False

    def run(self):
        self.set_up()
        exec(f"self.{self.name}()")
        print(f"{self.name} is working")

    # colocar abstract?
    def set_up(self):
        pass

class WasRun(TestCase):
    def test_method(self):
        self.was_run = True

    def set_up(self):
        self.was_set_up = True
