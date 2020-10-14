from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

import sys
if sys.platform.startswith("win"):
    import _locale
    # pylint: disable=protected-access
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if 'fr' in reply and 'en' in reply and 'hello' in reply:
            return CheckResult.correct()
        return CheckResult.wrong('Try to print both languages and word you want to translate.')


if __name__ == '__main__':
    TranslatorTest('translator.translator').run_tests()
