import string

class Assertions(object):

    __slots__ = ['driver', 'verification_errors']

    def __init__(self, driver, verification_errors):
        self.driver = driver
        self.verification_errors = verification_errors

    def assert_equal(self, first, second):
        assert first == second

    def verify_equal(self, first, second, msg=""):
        try:
            self.assert_equal(first, second)
        except AssertionError as error:
            e = error.__class__
            if msg:
                m = "%s: %s in %s = %s" % (msg, e.__name__, first, second)
            else:
                m = "%s: %s in %s = %s" % (e.__name__, e.__doc__, first, second)
            self.verification_errors.append(m)

    def assert_not_equal(self, first, second, msg=""):
        assert first != second

    def verify_not_equal(self, first, second, msg=""):
        try:
            self.assert_not_equal(first, second, msg)
        except AssertionError as error:
            if msg:
                m = "%s:\n%s" % (msg, str(error))
            else:
                m = str(error)
            self.verification_errors.append(m)

    def assert_true(self, expression):
        assert bool(expression) is True

    def verify_true(self, expression, msg=None):
        try:
            self.assert_true(expression)
        except AssertionError as error:
            e = error.__class__
            if msg:
                m = "%s: %s in %s" % (msg, e.__name__, expression)
            else:
                m = "%s: %s in %s" % (e.__name__, e.__doc__, expression)
            self.verification_errors.append(m)

    def assert_false(self, expression):
        assert bool(expression) is False

    def verify_false(self, expression, msg=None):
        try:
            assert bool(expression) is False
        except AssertionError as error:
            e = error.__class__
            if msg:
                m = "%s:%s in %s" % (msg, e.__name__, expression)
            else:
                m = e.__name__, e.__doc__, expression
            print('assert error - ', m)
            self.verification_errors.append(m)