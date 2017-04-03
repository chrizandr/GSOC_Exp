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
        with views.app.app_context():
            views.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(views.app.config['DATABASE'])

    def test_EntryPoint(self):
        response = self.app.get("/demo-api")
        pdb.set_trace()

if __name__ == '__main__':
    unittest.main()
