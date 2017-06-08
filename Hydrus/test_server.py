# -*- coding: utf-8 -*-

import views
import unittest
import tempfile
import os
import pdb

class ViewsTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, views.app.config['DATABASE'] = tempfile.mkstemp()
        views.app.config['TESTING'] = True
        self.app = views.app.test_client()


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(views.app.config['DATABASE'])

    def test_EntryPoint(self):
        response_get = self.app.get("/demo-api")
        response_post = self.app.post("/demo-api", data={})
        response_delete = self.app.delete("/demo-api")
        assert response_get.status_code==200
        assert response_post.status_code==405
        assert response_delete.status_code==405

    def test_EntryPoint_context(self):
        response = self.app.get("/demo-api/contexts/EntryPoint.jsonld")
        assert response.status_code==200
        
    def test_Vocab(self):
        response = self.app.get()
        pass

if __name__ == '__main__':
    unittest.main()
