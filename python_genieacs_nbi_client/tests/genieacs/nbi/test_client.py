"""python_genieacs_nbi_client."""

import unittest
import genieacs.nbi.client


class Test(unittest.TestCase):
    """Unit tests for genieacs.nbi.client.Client."""
    @classmethod
    def setUpClass(cls):
        cls.instance = genieacs.nbi.client.Client()

    def setUp(self):
        self.assertIsInstance(self.instance, genieacs.nbi.client.Client)

    def test_properties(self):
        """Test genieacs.nbi.client.Client properties"""
        self.assertEqual(self.instance.address, 'http://localhost:7557')
        self.assertFalse(self.instance.verbose)
        args = {"verbose": True, "address": "http://foo.bar"}
        nbic = genieacs.nbi.client.Client(**args)
        self.assertTrue(nbic.verbose)
        self.assertEqual(nbic.address, args["address"])

    def test_url(self):
        """Test genieacs.nbi.client.Client.url()"""
        suffix = "foo"
        self.assertEqual(self.instance.url(suffix),
                         "/".join([self.instance.address, suffix]))
        args = ("bar", 1, 2)
        url = "/".join(["{}", suffix]).format(self.instance.address, *args)
        self.assertEqual(self.instance.url(suffix, *args), url)

    @unittest.skip(
        "skip genieacs.nbi.client.Client.dispatch_device_task() yet")
    def test_dispatch_device_task(self):
        "Test genieacs.nbi.client.Client.dispatch_device_task()"
        pass

    @unittest.skip("skip genieacs.nbi.client.Client.perform_request() yet")
    def test_perform_request(self):
        "Test genieacs.nbi.client.Client.perform_request()"
        pass

    @unittest.skip("skip genieacs.nbi.client.Client.reboot() yet")
    def test_reboot(self):
        "Test genieacs.nbi.client.Client.reboot()"
        pass

    @unittest.skip("skip genieacs.nbi.client.Client.refresh_object() yet")
    def test_refresh_object(self):
        "Test genieacs.nbi.client.Client.refresh_object()"
        pass


if __name__ == "__main__":
    unittest.main()
