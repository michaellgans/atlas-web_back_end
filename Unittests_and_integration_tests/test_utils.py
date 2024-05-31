#!/usr/bin/env python3
""" Task 0 - Parameterize a unit test """

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Task 0 - Create a class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """ Tests assertEqual """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, error) -> None:
        """ Task 1 - Test assertRaises """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), error)


class TestGetJson(unittest.TestCase):
    """ Task 2 - Mock HTTP Calls """

    @parameterized.expand([
        ("http://example.com", {"payload", True}),
        ("http://holberton.io", {"payload", False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, mock_get):
        """ Task 2 - Test get_json """
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = payload

        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """ Task 3 - parameterize and patch """

    def test_memoize(self):
        """ Task 3 - test memoize """
        class TestClass:
            """ Class to test """
            def a_method(self):
                """ Returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized version of a_method """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock:
            test = TestClass()
            self.assertEqual(test.a_property, mock.return_value)
            self.assertEqual(test.a_property, mock.return_value)
            mock.assert_called_once()
