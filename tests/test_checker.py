import ast
import unittest

from flake8_super_call import DunderClassSuperChecker


def check(checker_class, super_class_call):
    tree = ast.parse(super_class_call)
    return next(checker_class(tree).run(), None)


class TestDunderClassSuperChecker(unittest.TestCase):

    def test_bad_super_call(self):
        lineno, offset, message, _ = check(
            DunderClassSuperChecker, 'super(self.__class__, self)'
        )
        self.assertEqual(lineno, 1)
        self.assertEqual(offset, 0)
        self.assertTrue(message.startswith('S777'))

    def test_good_super_call(self):
        self.assertIsNone(
            check(DunderClassSuperChecker, 'super(ClassName, self)')
        )


if __name__ == '__main__':
    unittest.main()
