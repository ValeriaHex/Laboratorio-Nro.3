# def 10
# nombre o identificador 20
# ( 30
# ) 40
# , 50
# : 60
# simple_stat 70
# statement 80
def ini(tokens):
    i = 0
    error = ''
    i, error = def_funcion(tokens,i)
    if error != '':
        return error
    if i < len(tokens):
        return 'ERROR: EXPRESION LOGICA NO VALIDA'
    return 'VALIDO'

def def_funcion(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 10:
        i = i + 1
        if i < len(tokens) and tokens[i] == 20:
            i = i + 1
            if i < len(tokens) and tokens[i] == 30:
                i = i + 1
                i, error = parametros(tokens, i)

                if error == '':
                    if i < len(tokens) and tokens[i] == 40:
                        i = i + 1
                    else:
                        error = 'ERROR: SE ESPERABA )'
            else:
                error = 'ERROR: SE ESPERABA ('
            if error == '':
                if i < len(tokens) and tokens[i] == 60:
                    i = i + 1
                    i, error = cuerpo(tokens, i)
                else:
                    error = 'ERROR: SE ESPERABA :'
        else:
            error = 'ERROR: SE ESPERABA EL NOMBRE DE LA FUNCION'
    else:
        error = 'ERROR: SE ESPERABA "def"'
    return i, error

def parametros(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 20:
        i = i + 1
        while error == '' and i < len(tokens) and tokens[i] == 50:
            i = i + 1
            if i < len(tokens) and tokens[i] == 20:
                i = i + 1
            else:
                error = 'ERROR: SE ESPERABA UN PARAMETRO'
    return i, error

def cuerpo(tokens, i):
    error = ''
    if i < len(tokens) and tokens[i] == 70:
        i = i + 1
    elif i < len(tokens) and tokens[i] == 80:
        i = i + 1
        while i < len(tokens) and tokens[i] == 80:
            i = i + 1
    else:
        error = 'ERROR: SE ESPERABA UNA SENTENCIA'
    return i, error

# def calcular(a, b):
#     sentencia
#     sentencia

tokens = [10, 20, 30, 20, 50, 20, 40, 60, 80, 80]

print(ini(tokens))
