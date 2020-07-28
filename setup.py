from setuptools import setup

setup(
    name='semver-bnf',
    version='0.0.1',
    description="A semantic version helper that uses Backus-Naur form",
    url="https://github.com/jcoelho93/semver-bnf",
    author="José Coelho",
    license="MIT",
    packages=['semver_bnf'],
    install_requires=[
        'bnfparsing @ git+https://github.com/somemarsupials/bnfparsing@master'
    ],
    zip_safe=False
)