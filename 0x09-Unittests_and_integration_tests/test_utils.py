#!/usr/bin/env python3
"""module for testing utils.py"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """tests access_nested_map functionality"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access_nested_map funciton"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """tests errors of access_nested_map function"""
        with self.assertRaises(KeyError) as err_msg:
            access_nested_map(nested_map, path)
            self.assertEqual(err_msg, expected)


class TestGetJson(unittest.TestCase):
    """tests get_json functionality"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """test get_json function"""
        with patch('requests.get') as mock_req:
            mock_req.return_value.json.return_value = test_payload
            response = get_json(test_url)
            mock_req.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """tests memoize functionality"""
    def test_memoize(self):
        """test memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_method.assert_called_once()
