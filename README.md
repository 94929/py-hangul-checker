# py-hangul-checker
Python implementation of Hanhul (Korean Language) Spell Checker

## 설치법
```zsh
$ pip install py-hangul-checker
```

## 사용법
```python
>>> sentence_to_be_checked = "간편 하게 쓰세요!"
>>> ksc = KoreanSpellChecker()
>>> res = ksc.check_spelling(sentence_to_be_checked)
>>> res
"간편하게 쓰세요!"
```
