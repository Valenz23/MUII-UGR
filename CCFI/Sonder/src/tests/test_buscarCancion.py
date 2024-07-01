from clases.user import *
import unittest

class Testing(unittest.TestCase):
    def test_buscar_cancion(self):

        # buscar por el atributo artista el valor dragon
        atributo = 'artista'
        valor = 'dragon'        

        cancion = buscarCancion(atributo,valor)
        self.assertTrue(cancion)

if __name__ == '__main__':
    unittest.main()