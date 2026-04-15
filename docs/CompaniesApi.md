# financial_reports_generated_client.CompaniesApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_financials_retrieve**](CompaniesApi.md#companies_financials_retrieve) | **GET** /companies/{id}/financials/ | Retrieve Company Financials
[**companies_list**](CompaniesApi.md#companies_list) | **GET** /companies/ | List Companies
[**companies_next_annual_report_retrieve**](CompaniesApi.md#companies_next_annual_report_retrieve) | **GET** /companies/{id}/next-annual-report/ | Predict Next Annual Report
[**companies_retrieve**](CompaniesApi.md#companies_retrieve) | **GET** /companies/{id}/ | Retrieve Company Details


# **companies_financials_retrieve**
> PaginatedCompanyFinancialStatementList companies_financials_retrieve(id, fiscal_period=fiscal_period, fiscal_year=fiscal_year, fiscal_year_from=fiscal_year_from, fiscal_year_to=fiscal_year_to, line_items=line_items, statement_type=statement_type)

Retrieve Company Financials

Returns deduplicated, standardized financial KPIs for a company, structured by fiscal period and statement type.

When multiple filings report the same period (e.g. an annual report and its ESEF package), the data from the most recently published filing is returned.

Use the `depth` and `parent_code` fields on each line item to render the Capital IQ-style statement hierarchy.

**Access Level Required:** Requires **RAG / Agent (Level 3)**.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_company_financial_statement_list import PaginatedCompanyFinancialStatementList
from financial_reports_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.financialreports.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = financial_reports_generated_client.Configuration(
    host = "https://api.financialreports.eu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    id = 56 # int | A unique integer value identifying this company.
    fiscal_period = 'fiscal_period_example' # str | Filter by fiscal period. (optional)
    fiscal_year = 56 # int | Filter by exact fiscal year (e.g. `2024`). (optional)
    fiscal_year_from = 56 # int | Fiscal year range start (inclusive). (optional)
    fiscal_year_to = 56 # int | Fiscal year range end (inclusive). (optional)
    line_items = 'line_items_example' # str | Comma-separated KPI codes to include (e.g. `revenue,ebitda,net_income_loss`). Omit to return all extracted line items. Only statements containing at least one of the requested codes are returned. (optional)
    statement_type = 'statement_type_example' # str | Filter by statement type. (optional)

    try:
        # Retrieve Company Financials
        api_response = await api_instance.companies_financials_retrieve(id, fiscal_period=fiscal_period, fiscal_year=fiscal_year, fiscal_year_from=fiscal_year_from, fiscal_year_to=fiscal_year_to, line_items=line_items, statement_type=statement_type)
        print("The response of CompaniesApi->companies_financials_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_financials_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 
 **fiscal_period** | **str**| Filter by fiscal period. | [optional] 
 **fiscal_year** | **int**| Filter by exact fiscal year (e.g. &#x60;2024&#x60;). | [optional] 
 **fiscal_year_from** | **int**| Fiscal year range start (inclusive). | [optional] 
 **fiscal_year_to** | **int**| Fiscal year range end (inclusive). | [optional] 
 **line_items** | **str**| Comma-separated KPI codes to include (e.g. &#x60;revenue,ebitda,net_income_loss&#x60;). Omit to return all extracted line items. Only statements containing at least one of the requested codes are returned. | [optional] 
 **statement_type** | **str**| Filter by statement type. | [optional] 

### Return type

[**PaginatedCompanyFinancialStatementList**](PaginatedCompanyFinancialStatementList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Company not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_list**
> PaginatedCompanyMinimalList companies_list(countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, sector=sector, sub_industry=sub_industry, ticker=ticker, view=view)

List Companies

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve a paginated list of companies.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_company_minimal_list import PaginatedCompanyMinimalList
from financial_reports_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.financialreports.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = financial_reports_generated_client.Configuration(
    host = "https://api.financialreports.eu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    countries = 'countries_example' # str | Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values. (optional)
    industry = 'industry_example' # str | Filter by ISIC Group code. (optional)
    industry_group = 'industry_group_example' # str | Filter by ISIC Division code. (optional)
    isin = 'isin_example' # str | Filter by Company ISIN. Case-insensitive. (optional)
    lei = 'lei_example' # str | Filter by Company Legal Entity Identifier (LEI). Case-insensitive. (optional)
    on_watchlist = True # bool | Filter by companies on the user's watchlist. Use 'true' to see only watchlist companies, 'false' to exclude them. Omitting the parameter returns all companies. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. Available fields: `id`, `name`, `date_ipo`, `year_founded`, `country_iso__name`. Prefix with '-' for descending order (e.g., `-name`). (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    sector = 'sector_example' # str | Filter by ISIC Section code. (optional)
    sub_industry = 'sub_industry_example' # str | Filter by ISIC Class code. (optional)
    ticker = 'ticker_example' # str | Filter by Company primary stock Ticker symbol. Case-insensitive. (optional)
    view = summary # str | Controls the level of detail. Omit for a default 'summary' view, or use 'full' to include all details for each company. (optional) (default to summary)

    try:
        # List Companies
        api_response = await api_instance.companies_list(countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, sector=sector, sub_industry=sub_industry, ticker=ticker, view=view)
        print("The response of CompaniesApi->companies_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values. | [optional] 
 **industry** | **str**| Filter by ISIC Group code. | [optional] 
 **industry_group** | **str**| Filter by ISIC Division code. | [optional] 
 **isin** | **str**| Filter by Company ISIN. Case-insensitive. | [optional] 
 **lei** | **str**| Filter by Company Legal Entity Identifier (LEI). Case-insensitive. | [optional] 
 **on_watchlist** | **bool**| Filter by companies on the user&#39;s watchlist. Use &#39;true&#39; to see only watchlist companies, &#39;false&#39; to exclude them. Omitting the parameter returns all companies. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. Available fields: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;date_ipo&#x60;, &#x60;year_founded&#x60;, &#x60;country_iso__name&#x60;. Prefix with &#39;-&#39; for descending order (e.g., &#x60;-name&#x60;). | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sector** | **str**| Filter by ISIC Section code. | [optional] 
 **sub_industry** | **str**| Filter by ISIC Class code. | [optional] 
 **ticker** | **str**| Filter by Company primary stock Ticker symbol. Case-insensitive. | [optional] 
 **view** | **str**| Controls the level of detail. Omit for a default &#39;summary&#39; view, or use &#39;full&#39; to include all details for each company. | [optional] [default to summary]

### Return type

[**PaginatedCompanyMinimalList**](PaginatedCompanyMinimalList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The response structure will be the full Company object if &#x60;view&#x3D;full&#x60; is used. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_next_annual_report_retrieve**
> NextAnnualReport companies_next_annual_report_retrieve(id)

Predict Next Annual Report

Calculates the expected release window for the next annual report based on historical filing patterns.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.next_annual_report import NextAnnualReport
from financial_reports_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.financialreports.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = financial_reports_generated_client.Configuration(
    host = "https://api.financialreports.eu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    id = 56 # int | A unique integer value identifying this company.

    try:
        # Predict Next Annual Report
        api_response = await api_instance.companies_next_annual_report_retrieve(id)
        print("The response of CompaniesApi->companies_next_annual_report_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_next_annual_report_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 

### Return type

[**NextAnnualReport**](NextAnnualReport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns the predicted date window and confidence score. |  -  |
**404** | Not Found. Not enough historical data to make a confident prediction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_retrieve**
> Company companies_retrieve(id)

Retrieve Company Details

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve detailed information for a single company by its internal ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.company import Company
from financial_reports_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.financialreports.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = financial_reports_generated_client.Configuration(
    host = "https://api.financialreports.eu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    id = 56 # int | A unique integer value identifying this company.

    try:
        # Retrieve Company Details
        api_response = await api_instance.companies_retrieve(id)
        print("The response of CompaniesApi->companies_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 

### Return type

[**Company**](Company.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

