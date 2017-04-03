import os
import views
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, views.app.config['DATABASE'] = tempfile.mkstemp()
        views.app.config['TESTING'] = True
        self.app = views.app.test_client()
        with views.app.app_context():
            views.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(views.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
