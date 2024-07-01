from clases.user import *
from clases.cancion import *
import unittest

class Testing(unittest.TestCase):
    def test_anadir_cancion(self):

        # necesito un usuario para añadir una cancion
        u = usuario()
        
        # creamos una cancion de ejemplo
        artista = "shakira"
        nombre = "suerte"
        letra = "suerte que en el sur hayas nacido y que burlemos las distancias..."
        c = cancion(artista,nombre,letra)

        # y la añadimos
        result = u.anadirCancion(c)

        self.assertTrue(result)        

if __name__ == '__main__':
    unittest.main()