"""
Decoradores para los scripts del archivo battery.py
"""

def is_allowed(func):
    def wrapper(*args, **kwargs):

        param = args[0]

        if param == 0:
            print('Se desactivará el modo de conservación de bateria')
        elif param == 1:
            print('Se activará el modo de conservación de bateria')
        else:
            print('Parámetro no permitido: {}'.format(param))
            return

        func(*args, **kwargs)
        print('Realizado exitosamente!')

    return wrapper
