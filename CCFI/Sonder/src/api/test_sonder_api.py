from . import sonder_api as api

import hug
import unittest

class TestSonderApi(unittest.TestCase): 

    def test1_api_status(self):
        data = hug.test.get(api,'/status')
        self.assertEqual(data.status, hug.HTTP_200)

    def test2_api_buscar_cancion(self):
        data = hug.test.get(api,'/buscar', {'atributo':'artista','valor':'dragon'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test3_api_add_cancion(self):
        data = hug.test.put(api, '/add', {'id':'1004', 'artista':'test', 'titulo':'test', 'letra':'test'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test4_api_add_lote(self):
        data = hug.test.put(api, '/lote', {'path':'BBDD/lote.csv'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test5_api_listar_canciones(self):
        data = hug.test.get(api, '/lista')
        self.assertEqual(data.status, hug.HTTP_200)

    def test6_api_modificar_letra(self):
        data = hug.test.put(api, '/mod', {'id':'1004','letra':'api letra'})
        self.assertEqual(data.status, hug.HTTP_200)    

    def test7a_api_delete_cancion(self):
        data = hug.test.delete(api, '/del', {'id':'1004'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test7b_api_delete_cancion(self):
        data = hug.test.delete(api, '/del', {'id':'2222'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test7c_api_delete_cancion(self):
        data = hug.test.delete(api, '/del', {'id':'4444'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test7d_api_delete_cancion(self):
        data = hug.test.delete(api, '/del', {'id':'6666'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test7e_api_delete_cancion(self):
        data = hug.test.delete(api, '/del', {'id':'8888'})
        self.assertEqual(data.status, hug.HTTP_200)
    
if __name__ == '__main__':
    unittest.main()