import unittest
# Importamos nuestras funciones, esto puede cambiar de acuerdo a tus necesidades,
# aquí pongo un ejemplo
from main import *

class TestDays(unittest.TestCase):
    def setUp(self):
        # Aquí, opcionalmente, ejecuta lo que deberías ejecutar antes
        # de comenzar cada test.
        pass


    def test_calculate(self):
        expected = "The citizen with identification 12345. and with date of birth 1999-05-12 00:00:00 Has lived 8070 day(s)"
        current  = calculate("12345","1999-05-12")
        # Pásalo en el orden: actual, esperado
        self.assertEqual(expected, current)
