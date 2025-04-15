# financial_reports_generated_client.IndustryGroupsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**industry_groups_list**](IndustryGroupsApi.md#industry_groups_list) | **GET** /industry-groups/ | 
[**industry_groups_retrieve**](IndustryGroupsApi.md#industry_groups_retrieve) | **GET** /industry-groups/{id}/ | 


# **industry_groups_list**
> PaginatedIndustryGroupList industry_groups_list(page=page, page_size=page_size, search=search, sector=sector)

Retrieve a list of all available GICS Industry Groups. Can be filtered by parent sector ID.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

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

# Configure HTTP basic authorization: basicAuth
configuration = financial_reports_generated_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.IndustryGroupsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    sector = 56 # int |  (optional)

    try:
        api_response = await api_instance.industry_groups_list(page=page, page_size=page_size, search=search, sector=sector)
        print("The response of IndustryGroupsApi->industry_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustryGroupsApi->industry_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **sector** | **int**|  | [optional] 

### Return type

[**PaginatedIndustryGroupList**](PaginatedIndustryGroupList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

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

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

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

# Configure HTTP basic authorization: basicAuth
configuration = financial_reports_generated_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

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

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

