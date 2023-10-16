print("****inicia la tarea****")

# Este ejercicio es para distinguir datos de entrada y
# hacer operaciones matematicas con su resultado.

# Para este ejercicio, tenga en cuenta que todo dato incorrecto
# lo enviara al principio.

# tenemos un ciclo para validar si son numeros, letras o simbolos
while True:

    dato_usuario = input("ingrese letras o numeros: ")
    print(f"\nusted ha escrito: {dato_usuario}")
    try:

        # caso 1. Aqui solo se efectua una peticion y usamos un ciclo para mostrar todas las operaciones en conjunto.
        if dato_usuario.isdigit():
            print(
                f"""************\nsu dato {dato_usuario} es un numero,\ny le aplicaremos operaciones aritmeticas.\n***********""")
            dato_usuario = int(dato_usuario)
            numero_usuario = input("ingrese un numero: ")
            numero_usuario = int(numero_usuario)
            for calcular in range(5):
                if calcular == 1:
                    resultado = dato_usuario + numero_usuario
                    print(
                        f"Sumar {dato_usuario} con {numero_usuario} es igual a {resultado}")
                elif calcular == 2:
                    resultado = dato_usuario - numero_usuario
                    print(
                        f"Restar {dato_usuario} con {numero_usuario} es igual a {resultado}")
                elif calcular == 3:
                    resultado = dato_usuario * numero_usuario
                    print(
                        f"Multiplicar {dato_usuario} con {numero_usuario} es igual a {resultado}")
                elif calcular == 4:
                    resultado = dato_usuario / numero_usuario
                    print(
                        f"Dividir {dato_usuario} con {numero_usuario} es igual a {resultado}")
                else:

                    continue

            print("----------")
            exit()

# caso 2. Se usa la longitud del input, se pide un segundo dato y se elige el calculo a aplicar:
        elif dato_usuario.isalpha():
            print(
                f"""************\nsu dato {dato_usuario} son caracteres,\ny lo convertiremos en: {len(dato_usuario)}\n***********""")
            dato_nuevo = len(dato_usuario)

            numero_usuario = input(
                f"ingrese un nuevo numero para usarlo con su dato {dato_nuevo}: ")
            numero_usuario = int(numero_usuario)
            print("""**********
                  \n1. (Sumar)  2. (Restar)  3. (Multiplicar)  4. (Dividir)""")
            calcular = input("elija el cálculo que desea aplicar: ")
            calcular = int(calcular)
            match calcular:
                case 1:
                    resultado = dato_nuevo + numero_usuario
                    print(f"eligió una suma, y su resultado es {resultado}")
                case 2:
                    resultado = dato_nuevo - numero_usuario
                    print(f"eligió una resta, y su resultado es {resultado}")
                case 3:
                    resultado = dato_nuevo * numero_usuario
                    print(f"eligió multiplicar, y su resultado es {resultado}")
                case 4:
                    resultado = dato_nuevo / numero_usuario
                    print(f"eligió dividir, y su resultado es {resultado}")

                case default:
                    print("esa operacion no existe\n..............")
                    continue

            print("----------")
            exit()
# caso 3. Aqui se manejan los errores de entrada del input inicial.
        else:
            print(
                "no mezclas ni símbolos ni espacios vacíos, solo letras o numeros\n...............")

# Manejo de errores y excepciones entre los datos para los ciclos.
    except ValueError:
        print("Dato incorrecto. Vuelva a intentarlo\n...............")
