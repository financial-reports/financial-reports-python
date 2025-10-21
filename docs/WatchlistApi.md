# financial_reports_generated_client.WatchlistApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watchlist_companies_create**](WatchlistApi.md#watchlist_companies_create) | **POST** /watchlist/companies/ | Add Company to Watchlist
[**watchlist_companies_destroy**](WatchlistApi.md#watchlist_companies_destroy) | **DELETE** /watchlist/companies/{company_id}/ | Remove Company from Watchlist
[**watchlist_retrieve**](WatchlistApi.md#watchlist_retrieve) | **GET** /watchlist/ | Get User&#39;s Watchlist


# **watchlist_companies_create**
> WatchlistResponse watchlist_companies_create(watchlist_action)

Add Company to Watchlist

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Adds a specified company to the authenticated user's watchlist.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.watchlist_action import WatchlistAction
from financial_reports_generated_client.models.watchlist_response import WatchlistResponse
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
    api_instance = financial_reports_generated_client.WatchlistApi(api_client)
    watchlist_action = {"company_id":14} # WatchlistAction | 

    try:
        # Add Company to Watchlist
        api_response = await api_instance.watchlist_companies_create(watchlist_action)
        print("The response of WatchlistApi->watchlist_companies_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchlistApi->watchlist_companies_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlist_action** | [**WatchlistAction**](WatchlistAction.md)|  | 

### Return type

[**WatchlistResponse**](WatchlistResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Company successfully added to the watchlist. |  -  |
**400** | Bad Request. The company may already be in the watchlist or the input was invalid. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_companies_destroy**
> WatchlistResponse watchlist_companies_destroy(company_id)

Remove Company from Watchlist

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Removes a specified company from the authenticated user's watchlist using the `company_id` from the URL path.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.watchlist_response import WatchlistResponse
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
    api_instance = financial_reports_generated_client.WatchlistApi(api_client)
    company_id = 56 # int | 

    try:
        # Remove Company from Watchlist
        api_response = await api_instance.watchlist_companies_destroy(company_id)
        print("The response of WatchlistApi->watchlist_companies_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchlistApi->watchlist_companies_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | 

### Return type

[**WatchlistResponse**](WatchlistResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company successfully removed from the watchlist. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |
**404** | Not Found. The company either does not exist or was not in the user&#39;s watchlist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchlist_retrieve**
> List[WatchlistCompany] watchlist_retrieve()

Get User's Watchlist

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Fetches all companies currently in the authenticated user's watchlist.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.watchlist_company import WatchlistCompany
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
    api_instance = financial_reports_generated_client.WatchlistApi(api_client)

    try:
        # Get User's Watchlist
        api_response = await api_instance.watchlist_retrieve()
        print("The response of WatchlistApi->watchlist_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchlistApi->watchlist_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WatchlistCompany]**](WatchlistCompany.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the watchlist. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

