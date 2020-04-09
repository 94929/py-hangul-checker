import requests

from bs4 import BeautifulSoup


class KoreanSpellChecker:
    spell_checker_url = \
        'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy'
    spell_checked_tag = 'em'

    #
    # Public Methods
    #
    def check_spelling(self, sentence):
        self.__check_sentence_len(sentence)

        params = {
            'q': sentence,
            'where': 'nexearch',
            'color_blindness': '0',
        }
        response = requests.get(self.spell_checker_url, params=params)
        response.raise_for_status()

        response_in_html = response.text
        response_in_parsed_html = \
            BeautifulSoup(response_in_html, 'html.parser')
        return response_in_parsed_html.find(self.spell_checked_tag).get_text()

    #
    # Private Methods
    #
    def __check_sentence_len(self, sentence):
        if len(sentence) > 500:
            raise Exception('Input sentence length exceeds maximum limit')


if __name__ == '__main__':
    sentence = "부담갖지말고먹어"
    ksc = KoreanSpellChecker()
    res = ksc.check_spelling(sentence)
    print(res)

