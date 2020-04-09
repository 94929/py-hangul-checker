# py-hangul-checker
Python implementation of Hanhul (Korean Language) Spell Checker

## Status
[![image](https://img.shields.io/travis/jha929/py-hangul-checker.svg)](https://travis-ci.org/jha929/py-hangul-checker)
[![image](https://img.shields.io/pypi/pyversions/py-hangul-checker.svg)](https://pypi.python.org/pypi/py-hangul-checker)

## How to install
```zsh
$ pip install py-hangul-checker
```

## How to use
```python
>>> from hangul_checker import KoreanSpellChecker
>>> sentence_to_be_checked = "간편 하게 쓰세요!"
>>> ksc = KoreanSpellChecker()
>>> res = ksc.check_spelling(sentence_to_be_checked)
>>> res
"간편하게 쓰세요!"
```
