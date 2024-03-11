def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    
    
    if dividendo % divisor == 0:
        cociente = dividendo // divisor
        residuo = dividendo % divisor
        return "La division es exacta. \n" + "Cociente: " + str(cociente) + "\n" + "Residuo: " + str(residuo)
    else:
        cociente = dividendo / divisor
        residuo = dividendo % divisor
        return "La division no es exacta. \n" + "Cociente: " + str(cociente) + "\n" + "Residuo: " + str(residuo)
    


if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
