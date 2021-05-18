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
    val = os.system('su -c {}'.format(full_cmd))
    return val

def battery_status():
    """
    Show battery settings.
    """

    file = '/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode'

    with open(file, 'r') as f:
        value = int(f.readline().strip())
        f.close()

    return value

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Change battery conservation mode')
    parser.add_argument('-m', '--mode', type=int, help='battery conservation mode')
    parser.add_argument('-s', '--settings', action='store_true', help='show battery settings')

    args = parser.parse_args()

    if isinstance(args.mode, int):
        mode = args.mode
        battery_conservation(mode)

    elif args.settings:

        value = battery_status()
        msg = 'Conservación de batería'
        status = {1: 'activado.', 0: 'desactivado'}
        print(msg, status[value])


if __name__ == '__main__':
    main()
