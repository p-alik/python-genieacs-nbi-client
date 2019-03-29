"""python_genieacs_nbi_client."""

import unittest
from os import getpid
from python_genieacs_nbi_client.utils import build_request, build_post_request


class Test(unittest.TestCase):
    """Unit tests for genieacs.nbi.utils."""

    def test_build_request(self):
        """Test python_genieacs_nbi_client.utils.build_request()"""
        for method in ("POST", "DELETE", "PUT"):
            _url = "/".join(["http://xyz", method])
            data = {"foo": getpid(), "method": method}
            req = build_request(
                url=_url, method=method, data=data)
            self.assertEqual(req.method, method)
            self.assertEqual(req.full_url, _url)
            self.assertIsNotNone(req.data)

        req = build_request(url="http://xyz")
        self.assertEqual(req.method, "GET")
        self.assertIsNone(req.data)

    def test_build_post_request(self):
        """Test python_genieacs_nbi_client.utils.build_post_request()."""
        _url = "/".join(["http://xyz", "abc"])
        data = {"foo": getpid()}
        req = build_post_request(url=_url, data=data)
        self.assertEqual(req.method, "POST")
        self.assertEqual(req.full_url, _url)
        self.assertIsNotNone(req.data)
