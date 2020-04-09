import unittest

from hangul_checker.hangul_checker import KoreanSpellChecker


class TestKoreanSpellChecker(unittest.TestCase):

    def setUp(self):
        self.korean_spell_checker = KoreanSpellChecker()

    def tearDown(self):
        del self.korean_spell_checker

    def test_check_spelling(self):
        sentence_in = u'부담갖지 말고 드세요!'
        sentence_out = self.korean_spell_checker.check_spelling(sentence_in)
        self.assertEqual(sentence_out, u'부담 갖지 말고 드세요!')

