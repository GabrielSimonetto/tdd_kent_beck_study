class TestCase():
    def __init__(self, name):
        self.name = name

    def run(self):
        exec(f"self.{self.name}()")


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        self.name = name

    def test_method(self):
        self.was_run = True
