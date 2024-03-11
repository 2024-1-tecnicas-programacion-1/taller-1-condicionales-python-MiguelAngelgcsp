def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    
    
    if (num_victorias_a < 0 or num_victorias_b < 0 or num_victorias_b > 7 or num_victorias_a > 7 or
            (num_victorias_a >= num_victorias_b + 3 and num_victorias_a >= 6) or
            (num_victorias_b >= num_victorias_a + 3 and num_victorias_b >= 6)):
        return "El resultado es inválido"
        
    elif (num_victorias_a == num_victorias_b and num_victorias_a <= 6 and num_victorias_b <= 6) or \
         (num_victorias_a == num_victorias_b + 1 or num_victorias_b == num_victorias_a + 1):
        return "Aun no termina"
    
    elif num_victorias_a > num_victorias_b + 1:
        return "El ganador es el A"
        
    elif num_victorias_b > num_victorias_a + 1:
        return "El ganador es el B"            

    return ""            
        
    

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
