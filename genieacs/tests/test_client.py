"""genieacs.test."""

import unittest
from genieacs.nbi import client


class Test(unittest.TestCase):
    """Unit tests for client.Client."""
    @classmethod
    def setUpClass(cls):
        cls.instance = client.Client()

    def setUp(self):
        self.assertIsInstance(self.instance, client.Client)

    def test_properties(self):
        """Test Client properties"""
        self.assertEqual(
            self.instance.address,
            'http://localhost:7557')
        self.assertFalse(self.instance.verbose)
        args = {"verbose": True, "address": "http://foo.bar"}
        nbic = client.Client(**args)
        self.assertTrue(nbic.verbose)
        self.assertEqual(nbic.address, args["address"])

    def test_url(self):
        """Test Client.url()"""
        suffix = "foo"
        self.assertEqual(self.instance.url(suffix),
                         "/".join([self.instance.address, suffix]))
        args = ("bar", 1, 2)
        url = "/".join(["{}", suffix]
                       ).format(self.instance.address, *args)
        self.assertEqual(self.instance.url(suffix, *args), url)

    def test_devices_url(self):
        """Test Client.url()"""
        device_id = "xyz-123"
        url = "/".join([self.instance.address, "devices", device_id])
        self.assertEqual(self.instance.devices_url(device_id), url)
        self.assertEqual(self.instance.devices_url(),
                         "/".join([self.instance.address, "devices"]))

    @unittest.skip(
        "skip Client.dispatch_device_task()")
    def test_dispatch_device_task(self):
        "Test Client.dispatch_device_task()"

    @unittest.skip("skip Client.perform_request()")
    def test_perform_request(self):
        "Test Client.perform_request()"

    @unittest.skip("skip Client.reboot() yet")
    def test_reboot(self):
        "Test Client.reboot()"

    @unittest.skip("skip Client.refresh_object()")
    def test_refresh_object(self):
        "Test Client.refresh_object()"


if __name__ == "__main__":
    unittest.main()
