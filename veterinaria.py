
from service import *

while True:
    
    print('')
    print('Servicio de atencion medica de urgencias')
    print('--------------------------------------')
    print('1 - Crear ficha mascota')
    print('2 - Buscar por codigo mascota')
    print('3 - Eliminar por codigo mascota')
    print('4 - Listar mascotas')
    print('5 - Salir')
    op = int(input('Ingrese una opcion: '))

    match op:
        case 1:
            crear_mascota()
        case 2:
            buscar_mascota()
        case 3:
            eliminar_mascota()
        case 4:
            listar_mascota()
        case 5:
            guardar_archivo()
            print('Gracias por usar nuestro servicio')
            break
    continuar = input('Desea continuar? si/no: ').lower().split()
    if continuar == 'no':
        guardar_archivo()
        print('Gracias por usar nuestro servicio')
        break
        