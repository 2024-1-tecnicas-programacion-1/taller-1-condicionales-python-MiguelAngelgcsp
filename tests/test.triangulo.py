import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.triangulo import evaluar

class TestTriangulo(unittest.TestCase):
    def test_no_es_un_triangulo_valido(self):
        valor_esperado = "No es un triángulo válido"
        valor_actual = evaluar(3.9, 6.0, 1.2)
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
    
    class TestTriangulo(unittest.TestCase):

     def test_no_es_un_triangulo_valido(self):
        valor_esperado = "El triangulo es equilatero"
        valor_actual = evaluar(3, 3, 3)
        self.assertEqual(valor_esperado, valor_actual)

    class TestTriangulo(unittest.TestCase):
     def test_no_es_un_triangulo_valido(self):
        valor_esperado = "El triangulo es isoceles"
        valor_actual = evaluar(1.9, 2, 2)
        self.assertEqual(valor_esperado, valor_actual)
    
    class TestTriangulo(unittest.TestCase):
     def test_no_es_un_triangulo_valido(self):
        valor_esperado = "El triangulo es escaleno"
        valor_actual = evaluar(3.0, 5.0, 4.0)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
