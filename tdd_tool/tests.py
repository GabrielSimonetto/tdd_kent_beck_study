from tdd_tool import TestCase, WasRun

class TestCaseTest(TestCase):
    def test_was_run(self):
        test = WasRun("test_method")
        assert not test.was_run

        test.run()
        assert test.was_run

TestCaseTest("test_was_run").run()

