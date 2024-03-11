def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
   
    if anno < 1582 and anno % 4 !=0:
            return "no es bisiesto"
    if anno < 1582 and anno % 100 != 0:
            return "es bisiesto"
    if anno < 1582 and anno % 100 == 0:
            return "no es bisiesto"
    if anno >= 1582 and anno % 400 ==0:
            return "es bisiesto"
    if anno % 4 != 0:
            return "no es bisiesto"

    else:
            return "es bisiesto"
 
         
    

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
