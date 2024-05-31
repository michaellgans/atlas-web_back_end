#!/usr/bin/env python3
""" Task 4 - Testing GithubOrgClient """

import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ Task 5 - Mocking Properties """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://cats.com"}
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "http://cats.com")

    @patch("client.get_json")
    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """ Task 6 - More Patching """
        mock_public_repos_url.return_value = "www.cats.com"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        test_class = GithubOrgClient("test")
        result = test_class.public_repos()

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

        self.assertEqual(result, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, value, expected):
        """ Task 7 - Parameterize """
        self.assertEqual(GithubOrgClient.has_license(repo, value), expected)
