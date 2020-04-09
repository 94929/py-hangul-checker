from os import path

from setuptools import setup, find_packages


def get_readme():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
        readme = readme_file.read()
    return readme


setup(
    name="py-hangul-checker",
    version="0.1.1",
    author="Jinsung Ha",
    author_email="jsung5381@naver.com",
    description="Python implementation of Hanhul (Korean Language) Spell Checker",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    url="https://github.com/jha929/py-hangul-checker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)

