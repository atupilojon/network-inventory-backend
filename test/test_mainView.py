import unittest2 as test
from api import create_app


class APITestCase(test.TestCase):

    def setUp(self) -> None:
        self.app = create_app().test_client()

    def tearDown(self) -> None:
        pass

    def test_apiRunning(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    test.main()
