# or 10
# and 20
# not 30
# true 40
# false 50
# ( 60
# ) 70
# identificador 100
# numero 200
def ini(tokens):
    i = 0
    error = ''
    i, error = exp_logica(tokens, i)
    if error != '':
        return error
    if i < len(tokens):
        return 'ERROR: EXPRESION LOGICA NO VALIDA'
    return 'VALIDO'

def exp_logica(tokens, i):
    error = ''
    i, error = termino(tokens, i)
    while error == '' and i< len(tokens) and tokens[i] == 10:
        i = i + 1
        i, error = termino(tokens, i)
    return i, error

def termino(tokens, i):
    error = ''
    i, error = factor(tokens, i)
    while error == '' and i < len(tokens) and tokens[i] == 20:
        i = i + 1
        i, error = factor(tokens, i)
    return i, error

def factor(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 30:
        i = i + 1
        i, error = factor(tokens, i)

    elif i < len(tokens) and tokens[i] == 60:
        i = i + 1
        i, error = exp_logica(tokens, i)
        if error == '':
            if i < len(tokens) and tokens[i] == 70:
                i = i + 1
            else:
                error = 'ERROR: SE ESPERABA UN )'

    elif i < len(tokens) and tokens[i] in (40, 50, 100, 200):
        i = i + 1
    else:
        error = 'ERROR: SE ESPERABA (, NOT, TRUE, FALSE, IDENTIFICADOR O NUMERO'

    return i, error
# (false and not 3)
tokens = [60, 50, 20, 30, 200, 70]

print(ini(tokens))
