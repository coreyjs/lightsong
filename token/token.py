import enum
from typing import Final


class TokenType(enum.Enum):
    FUNCTION = 'FUNCTION'
    LET = 'let'
    TRUE = 'true'
    FALSE = 'false'
    IF = 'if'
    ELSE = 'else'
    RETURN = 'return'
    IDENT = 'IDENT'


class Token:
    def __init__(self, token_type: TokenType, literal: str):
        self.token_type = token_type
        self.literal = literal


class TokenHandler:
    def __init__(self):
        self.keyword_map = {
            'func': TokenType.FUNCTION,
            'let': TokenType.LET,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'return': TokenType.RETURN
        }
        self.ILLEGAL: Final = "ILLEGAL"
        self.EOF: Final = "EOF"

        # Identifiers and Literals
        self.IDENT: Final = "IDENT"  # add, foobar, x, y
        self.INT: Final = "INT"  # 1234

        # Operators
        self.ASSIGN: Final = "="
        self.PLUS: Final = "+"
        self.MINUS: Final = "-"
        self.BANG: Final = "!"
        self.ASTERISK: Final = "*"
        self.SLASH: Final = "/"

        self.LT: Final = "<"
        self.GT: Final = ">"

        # Delimiters
        self.COMMA: Final = ","
        self.SEMICOLON: Final = ";"

        # Equavilancy
        self.EQ: Final = "=="
        self.NOT_EQ: Final = "!=="

        self.LPAREN: Final = "("
        self.RPAREN: Final = ")"
        self.LBRACE: Final = "{"
        self.RBRACE: Final = "}"

        # Keywords
        self.FUNCTION = "FUNCTION"
        self.LET = "LET"
        self.TRUE = "TRUE"
        self.FALSE = "FALSE"
        self.IF = "IF"
        self.ELSE = "ELSE"
        self.RETURN = "RETURN"


    def look_up_ident(self, ident: str) -> TokenType:
        """
        look_up_ident checks the keywords table to see whether the given
        identifier is in fact a keyword.  If it is, it returns the keyword's
        TokenType constant.  If it isnt, we just get back token.IDENT,
        which is the TokenType for all user-defined identifiers.
        :param ident:
        :return:
        """
        if ident not in self.keyword_map:
            return TokenType.IDENT

        return self.keyword_map[ident]


