"""
Gestión de pacientes en una clinica
En la clinica "La Fuerza" se requiere desarrollar un sistema de gestión de pacientes. El sistema
debe gestionar la información de los pacientes atendidos en el día. Para cada paciente, se
almacenará:
• numero de historia clinica (un numero entero).
• Nombre del paciente (una cadena de texto).
• Edad del paciente (un numero entero).
• diagnostico (una cadena de texto).
• Cantidad de dias de internacion (un numero entero).
La información de todos los pacientes debe almacenarse en un array bidimensional, donde
cada fila representará un paciente, y las columnas contendrán los datos mencionados arriba.
Recordar que el array debe comenzar vacío.
Presentamos un ejemplo de cómo debería verse:
Requerimientos:

1. Interfaz del programa:
• El sistema debe mostrar un menú interactivo para que el usuario pueda elegir
entre las diferentes opciones del sistema (cargar pacientes, buscar paciente
por historia clinica, determinar paciente con más/menos dias de internacion,
ordenar pacientes por numero de historia clinica, salir del sistema, etc.).
• El menú debe estar dentro de un bucle que permita al usuario realizar
múltiples operaciones hasta que decida salir.
Ejemplo de cómo podría verse el menú

2. Cargar pacientes:
• Permitir al usuario ingresar los datos de los pacientes, almacenando la
información en una lista anidada (arreglo bidimensional), como se muestra en
la imagen de arriba. La cantidad de pacientes a ingresar debe ser determinada
por el usuario.

3. Mostrar la lista de pacientes:
• Imprimir en pantalla todos los datos de los pacientes almacenados en el
arreglo bidimensional, mostrando cada fila como un paciente.

4. Búsqueda de pacientes:
• Implementar una función que, dado el numero de historia clinica de un
paciente, busque en la lista y muestre todos los datos de dicho paciente (o un
mensaje indicando que no se encontró al paciente).

5. Ordenamiento de pacientes:
• Implementar una función que permita ordenar la lista de pacientes por el
numero de historia clinica en forma ascendente. Se podrá utilizar cualquier
algoritmo de ordenamiento.

6. Determinar el paciente con mayor cantidad de dias de internacion:
• Implementar una función que calcule e imprima el paciente con más dias de
internacion, mostrando sus datos completos.

7. Determinar el paciente con menor cantidad de dias de internacion:
• Implementar una función que calcule e imprima el paciente con menos dias de
internacion, mostrando sus datos completos.

8. Cantidad de pacientes con dias de internacion mayor a 5 dias.
• Implementar una función que recorra la lista de pacientes y cuente cuántos
pacientes tienen más de 5 dias de internacion.

9. Promedio de dias de internacion de todos los pacientes.
• Implementar una función que calcule el promedio de dias de internacion de
todos los pacientes registrados.

Importante:
▪ Si el usuario selecciona cualquier opcion sin que existan pacientes registrados en el
sistema, aparecerá un mensaje en pantalla notificando que no hay pacientes
registrados para la operación solicitada.
Sugerencias:
▪ Se recomienda la validación de los datos ingresados por el usuario.
▪ Organizar el código en funciones y, si es posible, en módulos independientes. Utilizar
import para incorporar funcionalidades de otros módulos cuando sea necesario.
▪ Se aconseja incluir documentación de funciones, sugerencia de tipos y comentarios
explicativos donde lo consideren necesario.
▪ Utilizar las estructuras que vimos hasta este momento de la cursada.
▪ Utilizar correctamente arreglos bidimensionales para almacenar la información.
▪ Proporcionar salidas claras para el usuario. La presentación de los datos debe ser
comprensible y legible. Se recomienda utilizar f-string.

Entrega del programa
▪ La entrega se deberá realizar mediante el link al repositorio de GitHub.
"""



def menu():  
    pacientes = []  

    while True:
        print("""
    ------[ Menu Principal ]------ 
    1. Cargar pacientes
    2. Mostrar lista de pacientes
    3. Buscar paciente por historia clinica
    4. Ordenar pacientes por historia clinica
    5. Paciente con más dias de internacion
    6. Paciente con menos dias de internacion
    7. Contar pacientes con más de 5 dias de internacion
    8. Promedio de das de internacion"
    9. Salir
              """)  
        opcion = input("Seleccione una opcion (1-9): ")
        if validar_entero(opcion):
            opcion = int(opcion)
            if 1 <= opcion <= 9:
                if opcion == 1:
                    pacientes = cargar_pacientes()
                elif opcion == 2:
                    lista_pacientes(pacientes)
                elif opcion == 3:
                    historia_clinica = input("Ingrese el numero de historia clinica del paciente a buscar: ")
                    if validar_entero(historia_clinica):
                        buscar_paciente(pacientes, int(historia_clinica))
                    else:
                        print("historia clinica inexistente.")
                elif opcion == 4:
                    ordenar_pacientes(pacientes)
                elif opcion == 5:
                    paciente_mas_dias(pacientes)
                elif opcion == 6:
                    paciente_menos_dias(pacientes)
                elif opcion == 7:
                    pacientes_mas_5_dias(pacientes)
                elif opcion == 8:
                    promedio_dias_internacion(pacientes)
                elif opcion == 9:
                    print("Saliendo del sistema...")
                    break
            else:
                print("Opcion invalida, seleccione una opcion (1-9): ")

def cargar_pacientes() -> list:
    pacientes = []  
    cantidad = input("Cuantos pacientes desea ingresar? ")
    while not validar_entero(cantidad) or int(cantidad) <= 0:
        cantidad = input(f"{cantidad} no es una cantidad valida, ingrese una cantidad valida de pacientes: ")
    
    cantidad = int(cantidad)
    
    for _ in range(cantidad):                    # Funcion que toma los datos de los pacientes y los ingresa en el sistema 
        historia_clinica = input("Ingrese el numero de historia clinica: ") 
        while not validar_entero(historia_clinica):     # Valida que los datos ingresados sean posibles
            historia_clinica = input("Numero de historia clinica invalido, ingrese un numero de historia clinica valido: ")

        nombre = input("Ingrese el nombre del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        while not validar_entero(edad) or int(edad) < 0:  
            edad = input("Edad invalida, ingrese una edad valida: ")

        diagnostico = input("Ingrese el diagnostico: ")

        dias_internacion = input("Ingrese la cantidad de dias de internacion: ")
        while not validar_entero(dias_internacion) or int(dias_internacion) < 0:
            dias_internacion = input("La cantidad de dias es invalida, ingrese una cantidad de dias valida: ")

        pacientes.append([int(historia_clinica), nombre, int(edad), diagnostico, int(dias_internacion)])
        print("Siguiente paciente...")

    print("Carga de pacientes finalizada")

    return pacientes  

def lista_pacientes(pacientes: list) -> None:  # Funcion que muestra la lista de pacientes
    if not pacientes:  
        print("No hay pacientes registrados.")  
        return  
    print("[Lista de pacientes]")  
    for paciente in pacientes:  
        print(f"historia clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias de internacion: {paciente[4]}")  
    print("--------------------------------")  

def buscar_paciente(pacientes: list, historia_clinica: int) -> None:  # Funcion que busca un paciente por historia clinica
    for paciente in pacientes:  
        if paciente[0] == historia_clinica:  
            print(f"Paciente encontrado: historia clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias de internacion: {paciente[4]}")  
            return  
    print("Paciente no encontrado.")  

def ordenar_pacientes(pacientes: list) -> None:  # Funcion que ordena los pacientes segun historia clinica de menor a mayor
    if not pacientes:                            # (Aclaracion) la funcion no muestra los pacientes por que no fue pedido en la consigna, solo los ordena.c
        print("No hay pacientes para ordenar.")  
        return  
        
    n = len(pacientes)                          # Utilizacion del algoritmo de ordenamiento Bubble Sort
    for i in range(n):  
        for j in range(0, n-i-1):  
            if pacientes[j][0] > pacientes[j+1][0]:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]  
    print("Pacientes ordenados de menor a mayor por historia clinica.")  

def paciente_mas_dias(pacientes: list) -> None:  # Funcion que muestra el paciente con mas dias de internacion
    if not pacientes:  
        print("No hay pacientes registrados.")  
        return  
    
    paciente_max = pacientes[0]  
    for paciente in pacientes:  
        if paciente[4] > paciente_max[4]:  # Comparacion de dias de internacion  
            paciente_max = paciente  
            
    print(f"Paciente con más dias de internacion: historia clinica: {paciente_max[0]}, Nombre: {paciente_max[1]}, dias de internacion: {paciente_max[4]}")  

def paciente_menos_dias(pacientes: list) -> None:  # Funcion que muestra el paciente con menos dias de internacion
    if not pacientes:  
        print("No hay pacientes registrados.")  
        return  
    
    paciente_min = pacientes[0]  
    for paciente in pacientes:  
        if paciente[4] < paciente_min[4]:  # Comparacion de dias de internacion  
            paciente_min = paciente  
            
    print(f"Paciente con menos dias de internacion: historia clinica: {paciente_min[0]}, Nombre: {paciente_min[1]}, dias de internacion: {paciente_min[4]}")  

def pacientes_mas_5_dias(pacientes: list) -> None: # Funcion que identifica la cantidad de pacientes con mas de 5 dias de internacion
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1
    print(f"Cantidad de pacientes con más de 5 dias de internacion: {contador}")

def promedio_dias_internacion(pacientes: list) -> None: # Funcion que muestra el promedio de dias de internacion
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]
    
    promedio = total_dias / len(pacientes)
    print(f"Promedio de dias de internacion: {promedio:.2f}")

def validar_entero(valor: str) -> bool: # Funcion que valida que lo que se esta ingresando es un entero para que el codigo no explote en mil pedazos
    if valor == "" or (valor[0] == '-' and len(valor) == 1):
        return False
    if valor[0] == '-':
        valor = valor[1:]

    for num in valor:
        if num not in "0123456789":
            return False
    return True

menu()