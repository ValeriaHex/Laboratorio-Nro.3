# for 10
# target_list 20
# in 30
# expression_list 40
# : 50
# simple_stat 60
# suite 70
# else 80
# Newline 90
# suite_else 100
def ini(tokens):
    i = 0
    error = ''
    i, error = bucle_for(tokens, i)
    if error != '':
        return error
    if i < len(tokens):
        return 'ERROR: SE ENCONTRO TOKEN NO ESPERADO'
    return 'VALIDO'

def bucle_for(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 10:
        i = i + 1
        i, error = target_list(tokens, i)
        if error == '':
            if i < len(tokens) and tokens[i] == 30:
                i = i + 1
                i, error = expression_list(tokens, i)
                if error == '':
                    if i < len(tokens) and tokens[i] == 50:
                        i = i + 1
                        i, error = cuerpo(tokens, i)

                        if error == '':
                            if i < len(tokens) and tokens[i] == 80:
                                i = i + 1
                                if i < len(tokens) and tokens[i] == 50:
                                    i = i + 1
                                    if i < len(tokens) and tokens[i] == 90:
                                        i = i + 1
                                        i, error = suite_else(tokens, i)
                                    else:
                                        error = 'ERROR: SE ESPERABA NEWLINE'
                                else:
                                    error = 'ERROR: SE ESPERABA ":" DESPUES DE else'
                    else:
                        error = 'ERROR: SE ESPERABA ":"'
            else:
                error = 'ERROR: SE ESPERABA in'
    else:
        error = 'ERROR: SE ESPERABA for'

    return i, error

def target_list(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 20:
        i = i + 1
    else:
        error = 'ERROR: SE ESPERABA "target_list"'
    return i, error

def expression_list(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 40:
        i = i + 1
    else:
        error = 'ERROR: SE ESPERABA expression_lisst'
    return i, error

def cuerpo(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 60:
        i = i + 1
    elif i < len(tokens) and tokens[i] == 70:
        i = i + 1
    else:
        error = 'ERROR: SE ESPERABA UN simple_stat O suite'
    return i, error

def suite_else(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 100:
        i = i + 1
    else:
        error = 'ERROR: SE ESPERABA suite_else'

    return i, error

# for num in numeros:
#   suite
# else:
#   suite_else

tokens = [10, 20, 30, 40, 50, 70, 80, 50, 90, 100]

print(ini(tokens))
