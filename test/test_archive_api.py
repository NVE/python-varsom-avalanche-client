# coding: utf-8

"""
    Snøskredvarsel API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v5.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import varsom_avalanche_client
from api.archive_api import ArchiveApi  # noqa: E501
from varsom_avalanche_client.rest import ApiException


class TestArchiveApi(unittest.TestCase):
    """ArchiveApi unit test stubs"""

    def setUp(self):
        self.api = api.archive_api.ArchiveApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_all(self):
        """Test case for archive_all

        """
        pass

    def test_archive_region_id(self):
        """Test case for archive_region_id

        """
        pass

    def test_archive_regions(self):
        """Test case for archive_regions

        """
        pass

    def test_archive_warning_id(self):
        """Test case for archive_warning_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
