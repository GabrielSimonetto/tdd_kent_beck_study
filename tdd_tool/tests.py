from tdd_tool import TestCase, WasRun

class TestCaseTest(TestCase):
    # def set_up(self):
    #     self.test = WasRun("test_method")

    # def test_running(self):
    #     self.test.run()
    #     assert self.test.was_run

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert test.log == "set_up test_method teardown ", (
            f"this log contained: {test.log}"
        )

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()


TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
TestCaseTest("test_failed_result").run()
# TestCaseTest("test_running").run()
# TestCaseTest("test_set_up").run()

