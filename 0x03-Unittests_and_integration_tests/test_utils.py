#!/usr/bin/env python3
""" Parameterize a unit test Module """
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap Class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """ TO know utils.access_nested_map function and
        test that the method returns what it is supposed to. """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """ Tests `access_nested_map`'s exception raising. """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
