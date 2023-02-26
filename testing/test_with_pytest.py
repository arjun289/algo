def setup_module(module):
    print("Set up MODULE {0}".format(module.__name__))


def teardown_module(module):
    print("Tear down MODULE {0}".format(module.__name__))


def test_a_function():
    print("RUNNING TEST FUNCTION")


class BaseTest:
    def setup_class(cls):
        print("Set up CLASS {0}".format(cls.__name__))

    def teardown_class(cls):
        print("Tear down CLASS {0}\n".format(cls.__name__))

    def setup_moethod(self, method):
        print("Set up method {0}".format(method.__name__))

    def teardown_method(self, method):
        print("Tear down method {0}".format(method.__name__))


class TestClass1(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 1-1")

    def test_method_2(self):
        print("RUNNING METHOD 1-2")


class TestClass2(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 2-1")

    def test_method_2(self):
        print("RUNNING METHOD 2-2")
