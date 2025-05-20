# financial_reports_generated_client.CompaniesApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_list**](CompaniesApi.md#companies_list) | **GET** /companies/ | 
[**companies_retrieve**](CompaniesApi.md#companies_retrieve) | **GET** /companies/{id}/ | 


# **companies_list**
> PaginatedCompanyList companies_list(countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker)

Retrieve a paginated list of companies.

Supports filtering via query parameters defined in the CompanyFilter,
searching via the 'search' parameter (searches name, ISINs, LEI, Ticker),
and ordering via the 'ordering' parameter (allowed fields: name, date_ipo, year_founded, country_iso__name).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_company_list import PaginatedCompanyList
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
    countries = 'countries_example' # str | Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values (e.g., US,GB,DE). (optional)
    industry = 'industry_example' # str | Filter by GICS Industry code. (optional)
    industry_group = 'industry_group_example' # str | Filter by GICS Industry Group code. (optional)
    isin = 'isin_example' # str | Find companies matching the provided ISIN. (optional)
    lei = 'lei_example' # str | Find a company by its LEI. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    sector = 'sector_example' # str | Filter by GICS Sector code. (optional)
    sub_industry = 'sub_industry_example' # str | Filter by GICS Sub-Industry code. (optional)
    ticker = 'ticker_example' # str | Find a company by its Ticker. (optional)

    try:
        api_response = await api_instance.companies_list(countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker)
        print("The response of CompaniesApi->companies_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values (e.g., US,GB,DE). | [optional] 
 **industry** | **str**| Filter by GICS Industry code. | [optional] 
 **industry_group** | **str**| Filter by GICS Industry Group code. | [optional] 
 **isin** | **str**| Find companies matching the provided ISIN. | [optional] 
 **lei** | **str**| Find a company by its LEI. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **sector** | **str**| Filter by GICS Sector code. | [optional] 
 **sub_industry** | **str**| Filter by GICS Sub-Industry code. | [optional] 
 **ticker** | **str**| Find a company by its Ticker. | [optional] 

### Return type

[**PaginatedCompanyList**](PaginatedCompanyList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_retrieve**
> Company companies_retrieve(id)

Retrieve detailed information for a single company by its internal ID.
Lookup by ISIN, LEI, or Ticker via this specific endpoint is not supported by default.
Use the list endpoint with filters (`?isin=...`, `?lei=...`, `?ticker=...`) instead.

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
    id = 56 # int | 

    try:
        api_response = await api_instance.companies_retrieve(id)
        print("The response of CompaniesApi->companies_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

