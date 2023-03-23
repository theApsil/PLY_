import ply.lex as lex

# Define a list of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

# Define regular expressions for each token
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Define a regular expression for floating point numbers
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


# Define a regular expression for integer numbers
def t_NUMBER_int(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a regular expression for invalid characters
def t_error(t):
    #print(f"Invalid character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Define a function to parse an arithmetic expression
def parse_arithmetic_expression(expression):
    lexer.input(expression)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    # Check for division by zero
    for i in range(len(tokens) - 1):
        if tokens[i].type == 'DIVIDE' and tokens[i + 1].value == 0:
            raise ZeroDivisionError("Division by zero")

    # Output tokens in the requested format
    output = ''
    for token in tokens:
        output += f'<LexToken({token.type}, {repr(token.value)}, {token.lineno}, {token.lexpos})>,\n'
    return output[:-2]  # remove trailing comma and newline


if __name__ == "__main__":
    expression = '3.1 + 4 * (2 - 1) / 2'
    tokens = parse_arithmetic_expression(expression)
    print(expression, '\n', tokens)

