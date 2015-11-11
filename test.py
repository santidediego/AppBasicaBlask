import unittest
import os
import paginaEstatica
import tempfile
from flask.ext.testing import TestCase

class paginaEstaticaTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, paginaEstatica.app.config['DATABASE'] = tempfile.mkstemp()
        paginaEstatica.app.config['TESTING'] = True
        self.app = paginaEstatica.app.test_client()
        #paginaEstatica.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(paginaEstatica.app.config['DATABASE'])

    #Aqui acaba el esqueleto principal

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_name_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/user/santiago')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
