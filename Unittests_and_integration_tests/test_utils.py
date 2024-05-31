#!/usr/bin/env python3
""" Task 0 - Parameterize a unit test """

import unittest
from utils import access_nested_map
from parameterized import parameterized


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
        """ Test assertRaises """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), error)
