import os
import logging
import bnfparsing
from .exceptions import InvalidSemver

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class SemanticVersion:
    spec_version = "2.0.0"
    def __init__(self, raw_string: str):
        self.raw_str = raw_string
        try:
            SemverParser().parse(raw_string)
        except bnfparsing.exceptions.NotFoundError as e:
            raise InvalidSemver(raw_string) from e


class SemverParser(bnfparsing.ParserBase):
    def __init__(self):
        super().__init__(ws_handler=bnfparsing.ignore)
        with open(os.path.join(__location__,'grammar.bnf')) as grammar_file:
            grammar = grammar_file.read()
            logging.debug("Grammar loaded: %s", grammar)
            self.grammar(grammar)
