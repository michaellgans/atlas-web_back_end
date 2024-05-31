#!/usr/bin/env python3
""" Task 4 - Testing GithubOrgClient """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    # Different orgs to test with the client
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    # Replaces the output of get_json with a patch
    # The string is: class.method that you're patching
    @patch("client.get_json")
    # Test Method
    def test_org(self, org, get_json):
        """ Tests GithubOrgClient with orgs """
        # Return value of the patch set to True
        # Means if get_json is called in the test, returns True
        get_json.return_value = {"payload": True}
        # Passes each org to the class to test it
        client = GithubOrgClient(org)
        # The actual test
        self.assertEqual(client.org, {"payload": True})
        # Makes sure get_json called only once
        get_json.assert_called_once()
