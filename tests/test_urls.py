import unittest

class TestURLs(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()








'''
class TestURLs(unittest.TestCase):

    def setUp(self):
        admin._views = []
        rest_api.resources = []

        app = create_app('config.TestConfig')
        self.client = app.test_client()
        db.app = app
        db.create_all()
'''
