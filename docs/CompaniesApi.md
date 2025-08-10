# financial_reports_generated_client.CompaniesApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_list**](CompaniesApi.md#companies_list) | **GET** /companies/ | List Companies
[**companies_retrieve**](CompaniesApi.md#companies_retrieve) | **GET** /companies/{id}/ | Retrieve Company Details


# **companies_list**
> PaginatedCompanyMinimalList companies_list(countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker)

List Companies

**Access Level Required:** Requires **Level 1** Plan or higher.

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
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    sector = 'sector_example' # str | Filter by ISIC Section code. (optional)
    sub_industry = 'sub_industry_example' # str | Filter by ISIC Class code. (optional)
    ticker = 'ticker_example' # str | Filter by Company primary stock Ticker symbol. Case-insensitive. (optional)

    try:
        # List Companies
        api_response = await api_instance.companies_list(countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker)
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
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **sector** | **str**| Filter by ISIC Section code. | [optional] 
 **sub_industry** | **str**| Filter by ISIC Class code. | [optional] 
 **ticker** | **str**| Filter by Company primary stock Ticker symbol. Case-insensitive. | [optional] 

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
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_retrieve**
> Company companies_retrieve(id)

Retrieve Company Details

**Access Level Required:** Requires **Level 1** Plan or higher.

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

