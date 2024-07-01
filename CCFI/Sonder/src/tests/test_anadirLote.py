from clases.user import *
import unittest

class Testing(unittest.TestCase):
    def test_anadir_lote(self):

        a = admin()

        lote = "BBDD/lote.csv"

        result = a.anadirLote(lote)
        
        # los IDs de las canciones del lote
        a.borrarCancion("2222")
        a.borrarCancion("4444")
        a.borrarCancion("6666")
        a.borrarCancion("8888")

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()