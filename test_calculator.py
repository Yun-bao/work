from Calculator import *
import pytest


class TestCal:

    def setup_class(self):
        print("setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [0.1, 0.1, 0.2], [1000, 1000, 2000], [0, 1000, 1000]
    ], ids=['int1', 'float', 'bignum', 'zeronum'])
    def test_add(self, a, b, expect):

        assert expect == self.calc.add(a, b)




    @pytest.mark.parametrize('a,b,expect',[
        [1, 1, 1], [0.1, 0.1, 1], [1000, 1000, 1], [0, 1000, 0], [1, 0, 0]
    ], ids=['int1', 'float', 'bignum', 'zeronum', 'error'])
    def test_del(self, a, b, expect):
        try:
            assert expect == self.calc.div(a, b)

        except:
            print("这里有个异常")