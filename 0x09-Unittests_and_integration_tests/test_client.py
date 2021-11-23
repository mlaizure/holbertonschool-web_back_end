#!/usr/bin/env python3
"""module for testing client.py"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """tests that public_repos_url returns correct payload"""
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock(
                    return_value={'repos_url': 'test_url'})):
            test = GithubOrgClient('test_org')
            self.assertEqual(test._public_repos_url, 'test_url')

    @patch('client.get_json', return_value=[{'name': 'repo1'},
                                            {'name': 'repo2'}])
    def test_public_repos(self, mock_gj):
        """tests that public_repos returns expected list of repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_pru.return_value = 'test_url'
            test = GithubOrgClient('test_org')
            self.assertEqual(test.public_repos(), ['repo1', 'repo2'])
            mock_pru.assert_called_once()
            mock_gj.assert_called_once_with('test_url')
