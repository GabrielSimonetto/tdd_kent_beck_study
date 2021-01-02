from tdd_tool import TestCase, WasRun

class TestCaseTest(TestCase):
    # def set_up(self):
    #     self.test = WasRun("test_method")

    # def test_running(self):
    #     self.test.run()
    #     assert self.test.was_run

    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert self.test.log == "set_up test_method teardown ", (
            f"this log contained: {self.test.log}"
        )



TestCaseTest("test_template_method").run()
# TestCaseTest("test_running").run()
# TestCaseTest("test_set_up").run()

