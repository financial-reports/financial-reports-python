# financial_reports_generated_client.IndustriesApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**industries_list**](IndustriesApi.md#industries_list) | **GET** /industries/ | 
[**industries_retrieve**](IndustriesApi.md#industries_retrieve) | **GET** /industries/{id}/ | 


# **industries_list**
> PaginatedIndustryList industries_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_group_code=industry_group_code, industry_group_code_in=industry_group_code_in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code)

Retrieve a list of all available GICS Industries. Can be filtered by parent industry group ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_industry_list import PaginatedIndustryList
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
    api_instance = financial_reports_generated_client.IndustriesApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    industry_group_code = 'industry_group_code_example' # str | Filter by parent Industry Group GICS code (e.g., 1010) (optional)
    industry_group_code_in = ['industry_group_code_in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    sector_code = 'sector_code_example' # str | Filter by grandparent Sector GICS code (e.g., 10) (optional)

    try:
        api_response = await api_instance.industries_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_group_code=industry_group_code, industry_group_code_in=industry_group_code_in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code)
        print("The response of IndustriesApi->industries_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->industries_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **code__iexact** | **str**|  | [optional] 
 **code__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **industry_group_code** | **str**| Filter by parent Industry Group GICS code (e.g., 1010) | [optional] 
 **industry_group_code_in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **name__icontains** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **sector_code** | **str**| Filter by grandparent Sector GICS code (e.g., 10) | [optional] 

### Return type

[**PaginatedIndustryList**](PaginatedIndustryList.md)

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

# **industries_retrieve**
> Industry industries_retrieve(id)

Retrieve details for a single GICS Industry by its primary key.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.industry import Industry
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
    api_instance = financial_reports_generated_client.IndustriesApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.industries_retrieve(id)
        print("The response of IndustriesApi->industries_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->industries_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Industry**](Industry.md)

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

