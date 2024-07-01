from clases.user import *
import unittest

class Testing(unittest.TestCase):
    def test_borrar_cancion(self):

        # borramos la canción de shakira del otro test

        a = admin()

        result = a.borrarCancion("9999")

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()