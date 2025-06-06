# coding: utf-8

"""
    Financial Reports API

    API for accessing company filings, financial data, industry classifications, and related information.

    The version of the OpenAPI document: 1.0.0
    Contact: api@financialreports.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from financial_reports_generated_client.api.sub_industries_api import SubIndustriesApi


class TestSubIndustriesApi(unittest.IsolatedAsyncioTestCase):
    """SubIndustriesApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = SubIndustriesApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_sub_industries_list(self) -> None:
        """Test case for sub_industries_list

        """
        pass

    async def test_sub_industries_retrieve(self) -> None:
        """Test case for sub_industries_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
