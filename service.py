import json

# Abrir mascotas, r es permiso de lectura
with open('mascotas.json', 'r') as archivo_mascotas:
    data = json.load(archivo_mascotas)

#Este for es para convertir datos en una lista de listas
datos_mascotas = []
# p = animal

if len(data) > 0 :
    for p in data:
        mascotas = [p["nombre"], p["codigo"], p["edad"], p["peso"], p["raza"], p["especie"], p["diagnostico"], p["medicamentos"]]
        # print(mascotas)
        datos_mascotas.append(mascotas)


# FUNCIONES PRIMARIAS
def crear_mascota():
    datos_ingresados = pedir_datos()
    datos_mascotas.append(datos_ingresados)
    print(datos_mascotas)
    
def buscar_mascota():
    codigo_buscado = input('Ingrese el codigo: ')
    for i in range(len(datos_mascotas)):
            if codigo_buscado == datos_mascotas[i][1]:
                print('\nDatos de la mascota: ')
                print(f'Nombre: {datos_mascotas[i][0].capitalize()}')
                print(f'Codigo: {datos_mascotas[i][1]}')
                print(f'Edad: {datos_mascotas[i][2]}')
                print(f'Peso: {datos_mascotas[i][3]}')
                print(f'raza: {datos_mascotas[i][4]}')
                print(f'especie: {datos_mascotas[i][5]}')
                print(f'Diagnostico: {datos_mascotas[i][6]}')
                print(f'Diagnostico: {datos_mascotas[i][7]}\n')
                break
            else:
                print('Mascota no encontrada')

def eliminar_mascota():

    codigo_buscado = input('Ingrese el codigo: ')
    for i in range(len(datos_mascotas)):
            if codigo_buscado == datos_mascotas[i][1]:
                print(datos_mascotas[i])
                continuar = input('Esta seguro que desea eliminar la mascota? si/no: ').lower().strip()
                # validar si el usuario desea eliminar la mascota
                if continuar == 'no':
                    print('Operacion cancelada')
                    return
                else: 
        
                    datos_mascotas.remove(i)
                    print(datos_mascotas)
                    print('Mascota eliminada con exito')
            else:
                print('Mascota no encontrada')
    

def listar_mascota():
    for i in range(len(datos_mascotas)):
        print(f'\n {i + 1}) {datos_mascotas[i][0].capitalize()} Codigo:{datos_mascotas[i][1]}')



def guardar_archivo():
    
    for p in (datos_mascotas):
                mascota = {
                "nombre": p[0],
                "codigo": p[1],
                "edad": p[3],
                "peso": p[4],
                "sexo": p[5],
                "telefono": p[6],
                "diagnostico": p[7],
                "medicamentos": p[8]
                }
                data.append(mascota)
    
    with open('mascotas.json', 'w') as mascotas:
        json.dump(data, mascotas)
    pass



# FUNCIONES SECUNDARIAS


def pedir_datos():
    # pedir datos del paciente
    
    nombre = str(input(f'Ingrese el nombre: '))
    
    while(True):
        codigo=input("Ingrese el codigo: ")
        if codigo =="":
            print("Error, debe ingresar el codigo:")
        else:
            break
    edad = input(f'Ingrese la edad: ')
    peso = input(f'Ingrese el peso: ')
    raza = input(f'Ingrese la raza: ')
    especie = input(f'Ingrese la especie: ')
    diagnostico = input(f'Ingrese el diagnostico: ')
    medicamento = input(f'Ingrese el medicamento: ')
    
    # Hacemos una lista con los datos obtenidos
    nueva_mascota = [
    nombre,
    codigo,
    edad,
    peso,
    raza,
    especie,
    diagnostico,
    medicamento
    ]
    return nueva_mascota