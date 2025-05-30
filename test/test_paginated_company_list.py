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

from financial_reports_generated_client.models.paginated_company_list import PaginatedCompanyList

class TestPaginatedCompanyList(unittest.TestCase):
    """PaginatedCompanyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedCompanyList:
        """Test PaginatedCompanyList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedCompanyList`
        """
        model = PaginatedCompanyList()
        if include_optional:
            return PaginatedCompanyList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    financial_reports_generated_client.models.company.Company(
                        id = 56, 
                        name = '', 
                        lei = '', 
                        country_code = '', 
                        sector = null, 
                        industry_group = null, 
                        industry = null, 
                        sub_industry = null, 
                        ir_link = '', 
                        homepage_link = '', 
                        date_public = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        date_ipo = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        main_stock_exchange = '', 
                        social_facebook = '', 
                        social_instagram = '', 
                        social_twitter = '', 
                        social_linkedin = '', 
                        social_youtube = '', 
                        social_tiktok = '', 
                        social_pinterest = '', 
                        social_xing = '', 
                        social_glassdoor = '', 
                        year_founded = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        corporate_video_id = '', 
                        served_area = '', 
                        headcount = 56, 
                        contact_email = '', 
                        ticker = '', 
                        is_listed = True, )
                    ]
            )
        else:
            return PaginatedCompanyList(
                count = 123,
                results = [
                    financial_reports_generated_client.models.company.Company(
                        id = 56, 
                        name = '', 
                        lei = '', 
                        country_code = '', 
                        sector = null, 
                        industry_group = null, 
                        industry = null, 
                        sub_industry = null, 
                        ir_link = '', 
                        homepage_link = '', 
                        date_public = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        date_ipo = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        main_stock_exchange = '', 
                        social_facebook = '', 
                        social_instagram = '', 
                        social_twitter = '', 
                        social_linkedin = '', 
                        social_youtube = '', 
                        social_tiktok = '', 
                        social_pinterest = '', 
                        social_xing = '', 
                        social_glassdoor = '', 
                        year_founded = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        corporate_video_id = '', 
                        served_area = '', 
                        headcount = 56, 
                        contact_email = '', 
                        ticker = '', 
                        is_listed = True, )
                    ],
        )
        """

    def testPaginatedCompanyList(self):
        """Test PaginatedCompanyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
