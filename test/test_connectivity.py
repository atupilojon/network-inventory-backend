import json
import unittest2 as test
from flask import Response
from api import create_app


class APITestCase(test.TestCase):

    def setUp(self) -> None:
        self.app = create_app().test_client()

    def tearDown(self) -> None:
        pass

    def test_apiRunning(self):
        response: Response = self.app.get('/api/v1/test')
        response_body = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_body['connected'])


if __name__ == '__main__':
    test.main()
