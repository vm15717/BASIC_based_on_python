# CONSTANTS
DIGITS = '0123456789'
# ERRORS


class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)


# TOKENS
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'


class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def make_tokens(self):
        tokens_list = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens_list.append(self.make_number())
            elif self.current_char == '+':
                tokens_list.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens_list.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens_list.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens_list.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == ')':
                tokens_list.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '(':
                tokens_list.append(Token(TT_LPAREN))
                self.advance()
            else:
                # return some error
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")
        return tokens_list, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))


def run_excalibur(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error
