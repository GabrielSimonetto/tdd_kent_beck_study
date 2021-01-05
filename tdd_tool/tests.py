from tdd_tool import TestCase, WasRun, TestSuite, TestResult

class TestCaseTest(TestCase):
    # def __init__(self):
    #     self.result = TestResult()

    def set_up(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("test_method")
        # result = TestResult()
        test.run(self.result)
        assert test.log == "set_up test_method teardown ", (
            f"this log contained: {test.log}"
        )

    def test_result(self):
        test = WasRun("test_method")
        # result = TestResult()
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        # result = TestResult()
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def test_failed_result_formatting(self):
        # result = TestResult()
        self.result.test_started()
        self.result.test_failed()
        assert("1 run, 1 failed" == self.result.summary())

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))

        # result = TestResult()
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

# result = TestResult()
# print(TestCaseTest("test_template_method").run(result).summary())
# print(TestCaseTest("test_result").run(result).summary())
# print(TestCaseTest("test_failed_result_formatting").run(result).summary())
# print(TestCaseTest("test_failed_result").run(result).summary())
# print(TestCaseTest("test_suite").run(result).summary())

# bla = TestCaseTest()
# print(bla.test_template_method().run().summary())
# print(bla.test_result().run().summary())
# print(bla.test_failed_result_formatting().run().summary())
# print(bla.test_failed_result().run().summary())
# print(bla.test_suite().run().summary())

# TestCaseTest('bork').test_suite()

suite = TestSuite()
suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_result_formatting"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_suite"))

result = TestResult()
suite.run(result)
print(result.summary())
