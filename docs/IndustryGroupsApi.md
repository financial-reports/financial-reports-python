# financial_reports_generated_client.IndustryGroupsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**industry_groups_list**](IndustryGroupsApi.md#industry_groups_list) | **GET** /industry-groups/ | 
[**industry_groups_retrieve**](IndustryGroupsApi.md#industry_groups_retrieve) | **GET** /industry-groups/{id}/ | 


# **industry_groups_list**
> PaginatedIndustryGroupList industry_groups_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code, sector_code_in=sector_code_in)

Retrieve a list of all available GICS Industry Groups. Can be filtered by parent sector ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_industry_group_list import PaginatedIndustryGroupList
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
    api_instance = financial_reports_generated_client.IndustryGroupsApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    sector_code = 'sector_code_example' # str | Filter by parent Sector GICS code (e.g., 10) (optional)
    sector_code_in = ['sector_code_in_example'] # List[str] | Multiple values may be separated by commas. (optional)

    try:
        api_response = await api_instance.industry_groups_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code, sector_code_in=sector_code_in)
        print("The response of IndustryGroupsApi->industry_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustryGroupsApi->industry_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **code__iexact** | **str**|  | [optional] 
 **code__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **name__icontains** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **sector_code** | **str**| Filter by parent Sector GICS code (e.g., 10) | [optional] 
 **sector_code_in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 

### Return type

[**PaginatedIndustryGroupList**](PaginatedIndustryGroupList.md)

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

# **industry_groups_retrieve**
> IndustryGroup industry_groups_retrieve(id)

Retrieve details for a single GICS Industry Group by its primary key.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.industry_group import IndustryGroup
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
    api_instance = financial_reports_generated_client.IndustryGroupsApi(api_client)
    id = 56 # int | 

    try:
        api_response = await api_instance.industry_groups_retrieve(id)
        print("The response of IndustryGroupsApi->industry_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustryGroupsApi->industry_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**IndustryGroup**](IndustryGroup.md)

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

