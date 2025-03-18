
# Función para verificar un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para verificar si un número es palindrómico
def es_palindromico(n):
    return str(n) == str(n)[::-1]

# Función para encontrar y mostrar los pares de primos gemelos
def encontrar_primos_gemelos(limite):
    primos_gemelos = []
    for i in range(2, limite):
        if es_primo(i) and es_primo(i + 2):
            primos_gemelos.append((i, i + 2))
    return primos_gemelos

# Función para encontrar y mostrar los primos palindrómicos
def encontrar_primos_palindromicos(limite):
    primos_palindromicos = []
    for i in range(10, limite):
        if es_primo(i) and es_palindromico(i):
            primos_palindromicos.append(i)
    return primos_palindromicos

# Menú interactivo
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Encontrar números primos gemelos")
        print("2. Encontrar números primos palindrómicos")
        print("3. Salir")
        opcion = input("> ")

        if opcion == "1":
            limite = int(input("Ingrese el límite superior: "))
            pares_gemelos = encontrar_primos_gemelos(limite)
            print("Pares de primos gemelos encontrados:", pares_gemelos)

        elif opcion == "2":
            limite = int(input("Ingrese el límite superior: "))
            primos_palindromicos = encontrar_primos_palindromicos(limite)
            print("Primos palindrómicos encontrados:", primos_palindromicos)

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()


    # Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para verificar si un número es palindrómico
def es_palindromico(n):
    return str(n) == str(n)[::-1]

# Función para encontrar y mostrar los pares de primos gemelos
def encontrar_primos_gemelos(limite):
    primos_gemelos = []
    for i in range(2, limite):
        if es_primo(i) and es_primo(i + 2):
            primos_gemelos.append((i, i + 2))
    return primos_gemelos

# Función para encontrar y mostrar los primos palindrómicos
def encontrar_primos_palindromicos(limite):
    primos_palindromicos = []
    for i in range(10, limite):
        if es_primo(i) and es_palindromico(i):
            primos_palindromicos.append(i)
    return primos_palindromicos

# Menú interactivo
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Encontrar números primos gemelos")
        print("2. Encontrar números primos palindrómicos")
        print("3. Salir")
        opcion = input("> ")

        if opcion == "1":
            limite = int(input("Ingrese el límite superior: "))
            pares_gemelos = encontrar_primos_gemelos(limite)
            print("Pares de primos gemelos encontrados:", pares_gemelos)

        elif opcion == "2":
            limite = int(input("Ingrese el límite superior: "))
            primos_palindromicos = encontrar_primos_palindromicos(limite)
            print("Primos palindrómicos encontrados:", primos_palindromicos)

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
    

    