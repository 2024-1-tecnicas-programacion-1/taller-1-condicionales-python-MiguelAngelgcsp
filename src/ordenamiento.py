def evaluar(numero1, numero2, numero3, numero4):
    # TODO: Coloca aquí el código del ejercicio 5: Ordenamiento
    def ordenar_numeros(numeros):
        for i in range(len(numeros) - 1):
            for j in range(len(numeros) - i - 1):
                if numeros[j] > numeros[j + 1]:
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
        # Devolvemos la cadena ordenada dentro de la función de ordenamiento
        return ", ".join(map(str, numeros))

    # Creamos una lista con los números proporcionados
    numeros = [numero1, numero2, numero3, numero4]
    # Llamamos a la función de ordenamiento y devolvemos el resultado
    return ordenar_numeros(numeros)

   

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
