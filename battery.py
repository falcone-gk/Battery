"""
Funciones que manejarán la configuración de la bateria.
"""

import os
from decorators import is_allowed

@is_allowed
def battery_conservation(n):
    """
    Activa o desactiva el modo de conservación de la bateria.

    Parameters
    ----------
    n: int
        Toma los valores de 1 o 0 para activar o desactivar, respectivamente,
        el modo conservación de bateria.
    """

    # Comando para cambiar el modo de conservación de bateria.
    mode = '"echo {} '.format(n)
    file = '/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"'
    full_cmd = mode + '>' + file

    # Corre todo el comando en modo superusuario.
    os.system('su -c {}'.format(full_cmd))

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Change battery conservation mode')
    parser.add_argument('-m', '--mode', type=int)
    args = parser.parse_args()
    mode = args.mode
    battery_conservation(mode)

if __name__ == '__main__':
    main()
