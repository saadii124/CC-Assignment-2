import re


def lex(expression):
    tokens = []
    # define regex patterns for each token type
    id_regex = r'[a-zA-Z_][a-zA-Z0-9_]*'
    op_regex = r'[+-/*]'
    paren_regex = r'[()]'
    # compile the regex patterns
    id_pattern = re.compile(id_regex)
    op_pattern = re.compile(op_regex)
    paren_pattern = re.compile(paren_regex)

    # iterate through the expression, character by character
    i = 0
    while i < len(expression):
        # try to match each character against the regex patterns
        id_match = id_pattern.match(expression, i)
        op_match = op_pattern.match(expression, i)
        paren_match = paren_pattern.match(expression, i)
        # if the character matches an identifier, add it to the list of tokens
        if id_match:
            tokens.append(('IDENTIFIER', id_match.group()))
            i = id_match.end()
        # if the character matches an operator, add it to the list of tokens
        elif op_match:
            tokens.append(('OPERATOR', op_match.group()))
            i = op_match.end()
        # if the character matches a parenthesis, add it to the list of tokens
        elif paren_match:
            tokens.append(('PAREN', paren_match.group()))
            i = paren_match.end()
        # if the character doesn't match any of the regex patterns, raise an error
        else:
            raise ValueError(f'Invalid character "{expression[i]}" at index {i}')
    return tokens


# test the lexer
print(lex('a+(b*c)'))
