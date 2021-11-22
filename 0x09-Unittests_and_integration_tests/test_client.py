#!/usr/bin/env python3
"""module for testing client.py"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """tests GithubOrgClient functionality"""
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json', return_value={'k': 'v'})
    def test_org(self, org_name, mock_gj):
        """tests that GithubOrgClient.org returns correct value"""
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org, {'k': 'v'})
        url = 'https://api.github.com/orgs/{}'.format(org_name)
        mock_gj.assert_called_once_with(url)
