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

from financial_reports_generated_client.api.watchlist_api import WatchlistApi


class TestWatchlistApi(unittest.IsolatedAsyncioTestCase):
    """WatchlistApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = WatchlistApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_watchlist_companies_create(self) -> None:
        """Test case for watchlist_companies_create

        Add Company to Watchlist
        """
        pass

    async def test_watchlist_companies_destroy(self) -> None:
        """Test case for watchlist_companies_destroy

        Remove Company from Watchlist
        """
        pass

    async def test_watchlist_retrieve(self) -> None:
        """Test case for watchlist_retrieve

        Get User's Watchlist
        """
        pass


if __name__ == '__main__':
    unittest.main()
