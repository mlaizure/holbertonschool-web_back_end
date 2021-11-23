#!/usr/bin/env python3
"""module for testing client.py"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import Response


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """tests that repo has expected license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class([{"org_payload": TEST_PAYLOAD[0][0],
                       "repos_payload": TEST_PAYLOAD[0][1],
                       "expected_repos": TEST_PAYLOAD[0][2],
                       "apache2_repos": TEST_PAYLOAD[0][3]}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration test for github org client"""
    @classmethod
    def setUpClass(cls):
        """mock external calls"""
        cls.get_patcher = patch('requests.get')
        cls.patcher = cls.get_patcher.start()
        cls.patcher.side_effect = cls.side_effect

    @classmethod
    def tearDownClass(cls):
        """stop the patcher"""
        cls.patcher.stop()

    @classmethod
    def side_effect(cls, *args):
        """gets appropriate mock response based on url"""
        url = args[0]
        mock_res = Mock(spec_set=Response)
        cls.patcher.return_value = mock_res
        if url == 'https://api.github.com/orgs/google':
            mock_res.json.return_value = cls.org_payload
        elif url == 'https://api.github.com/orgs/google/repos':
            mock_res.json.return_value = cls.repos_payload
        return mock_res

    def test_public_repos(self):
        """tests public_repos method"""
        test = GithubOrgClient('google')
        self.assertEqual(test.public_repos(), self.__class__.expected_repos)

    def test_public_repos_with_license(self):
        """test public_repos method with license arg"""
        test = GithubOrgClient('google')
        self.assertEqual(test.public_repos(license='apache-2.0'),
                         self.__class__.apache2_repos)
