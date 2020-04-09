import requests

from bs4 import BeautifulSoup


class KoreanSpellChecker:
    spell_checker_url = 'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?_callback=jQuery112407704652679626749_1586403615462&q={}&where=nexearch&color_blindness=0&_=1586403615463'

    def __check_sentence_len(self, sentence):
        if len(sentence) > 500:
            raise Exception("Input sentence length exceeds maximum limit")

    def check_spelling(self, sentence):
        self.__check_sentence_len(sentence)

        dest_path = self.spell_checker_url.format(sentence)
        html = requests.get(dest_path).text
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find('em').get_text()


if __name__ == '__main__':
    sentence = "부담갖지말고먹어"
    ksc = KoreanSpellChecker()
    res = ksc.check_spelling(sentence)
    print(res)

