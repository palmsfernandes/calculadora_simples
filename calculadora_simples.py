"""Caluladora com While"""

while True:
    numero_1 = input('Digite um número: ')
    operador = input('Digite operador (+ | - | * | /): ')
    numero_2 = input('Digite outro número: ')
    
    numeros_validos = None
    primeiro_num_float = 0
    segundo_num_float = 0
    
    try:
        primeiro_num_float = float(numero_1)
        segundo_num_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um dos números são invalidos')
        continue
    
    operador_permitidos = '+-/*'
    
    if operador not in operador_permitidos:
        print('Operador invalido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo: ')
    
    if operador == '+':
        print(primeiro_num_float + segundo_num_float)
    elif operador == '-':
        print(primeiro_num_float - segundo_num_float)
    elif operador == '/':
        print(primeiro_num_float / segundo_num_float)
    elif operador == '*':
        print(primeiro_num_float * segundo_num_float)
    
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break