from clases.user import *
import unittest

class Testing(unittest.TestCase):
    def test_listar_canciones(self):    
        lista = listarCanciones()
        self.assertTrue(not lista.empty)

if __name__ == '__main__':
    unittest.main()