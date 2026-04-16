# financial_reports_generated_client.ISINsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**isins_list**](ISINsApi.md#isins_list) | **GET** /isins/ | List ISINs
[**isins_retrieve**](ISINsApi.md#isins_retrieve) | **GET** /isins/{code}/ | Retrieve ISIN


# **isins_list**
> PaginatedISINList isins_list(code=code, codes=codes, company=company, is_primary=is_primary, page=page, page_size=page_size, search=search)

List ISINs

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Search and resolve ISINs (International Securities Identification Numbers) to companies.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_isin_list import PaginatedISINList
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

# Configure Bearer authorization (JWT): CognitoJWT
configuration = financial_reports_generated_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.ISINsApi(api_client)
    code = 'code_example' # str |  (optional)
    codes = 'codes_example' # str | Filter by multiple ISIN codes. Comma-separated (e.g., US1234567890,DE1234567890). (optional)
    company = 56 # int | Filter by internal Company ID. (optional)
    is_primary = True # bool |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | Fuzzy search by ISIN code (e.g., 'US03'). (optional)

    try:
        # List ISINs
        api_response = await api_instance.isins_list(code=code, codes=codes, company=company, is_primary=is_primary, page=page, page_size=page_size, search=search)
        print("The response of ISINsApi->isins_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISINsApi->isins_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **codes** | **str**| Filter by multiple ISIN codes. Comma-separated (e.g., US1234567890,DE1234567890). | [optional] 
 **company** | **int**| Filter by internal Company ID. | [optional] 
 **is_primary** | **bool**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| Fuzzy search by ISIN code (e.g., &#39;US03&#39;). | [optional] 

### Return type

[**PaginatedISINList**](PaginatedISINList.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isins_retrieve**
> ISIN isins_retrieve(code)

Retrieve ISIN

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve details for a specific ISIN.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.isin import ISIN
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

# Configure Bearer authorization (JWT): CognitoJWT
configuration = financial_reports_generated_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.ISINsApi(api_client)
    code = 'code_example' # str | 

    try:
        # Retrieve ISIN
        api_response = await api_instance.isins_retrieve(code)
        print("The response of ISINsApi->isins_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISINsApi->isins_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**ISIN**](ISIN.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

