import unittest2 as test
from flask import Response
from api import create_app
from api.dao.dao_ipaddress import delete_all_ipaddr
import json


class IPAddressTest(test.TestCase):

    def setUp(self) -> None:
        self.app = create_app().test_client()
        self.new_ipaddr \
            = {"ipaddress": {"number": "172.28.98.199", "mask": 32, "type": "management"}}

    def tearDown(self) -> None:
        pass

    def test_load_ok_ip_addr(self):
        response: Response = self.app.post('/api/v1/ipaddr', json=self.new_ipaddr)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.get_data())['message'], 'IP address added')

    def test_delete_ok_ip_addr(self):
        response: Response = self.app.delete('/api/v1/ipaddr', json=self.new_ipaddr)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.get_data())['message'], 'IP address deleted')


if __name__ == '__main__':
    test.main()
