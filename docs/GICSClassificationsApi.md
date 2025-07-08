# financial_reports_generated_client.GICSClassificationsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**industries_list**](GICSClassificationsApi.md#industries_list) | **GET** /industries/ | List GICS Industries
[**industries_retrieve**](GICSClassificationsApi.md#industries_retrieve) | **GET** /industries/{id}/ | Retrieve GICS Industry
[**industry_groups_list**](GICSClassificationsApi.md#industry_groups_list) | **GET** /industry-groups/ | List GICS Industry Groups
[**industry_groups_retrieve**](GICSClassificationsApi.md#industry_groups_retrieve) | **GET** /industry-groups/{id}/ | Retrieve GICS Industry Group
[**sectors_list**](GICSClassificationsApi.md#sectors_list) | **GET** /sectors/ | List GICS Sectors
[**sectors_retrieve**](GICSClassificationsApi.md#sectors_retrieve) | **GET** /sectors/{id}/ | Retrieve GICS Sector
[**sub_industries_list**](GICSClassificationsApi.md#sub_industries_list) | **GET** /sub-industries/ | List GICS Sub-Industries
[**sub_industries_retrieve**](GICSClassificationsApi.md#sub_industries_retrieve) | **GET** /sub-industries/{id}/ | Retrieve GICS Sub-Industry


# **industries_list**
> PaginatedIndustryList industries_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_group_code=industry_group_code, industry_group_code_in=industry_group_code_in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code)

List GICS Industries

Retrieve a paginated list of GICS Industries. Supports filtering by `code`, `name`, parent `industry_group_code`, list of `industry_group_code_in`, and grandparent `sector_code`.

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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
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
        # List GICS Industries
        api_response = await api_instance.industries_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_group_code=industry_group_code, industry_group_code_in=industry_group_code_in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code)
        print("The response of GICSClassificationsApi->industries_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->industries_list: %s\n" % e)
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
**200** | Successfully retrieved the list of industries. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **industries_retrieve**
> Industry industries_retrieve(id)

Retrieve GICS Industry

Retrieve details for a specific GICS Industry by its ID.

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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve GICS Industry
        api_response = await api_instance.industries_retrieve(id)
        print("The response of GICSClassificationsApi->industries_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->industries_retrieve: %s\n" % e)
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
**200** | Successfully retrieved the industry details. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |
**404** | Industry not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **industry_groups_list**
> PaginatedIndustryGroupList industry_groups_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code, sector_code_in=sector_code_in)

List GICS Industry Groups

Retrieve a paginated list of GICS Industry Groups. Supports filtering by `code`, `name`, parent `sector_code`, and a list of parent `sector_code_in`.

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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
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
        # List GICS Industry Groups
        api_response = await api_instance.industry_groups_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code, sector_code_in=sector_code_in)
        print("The response of GICSClassificationsApi->industry_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->industry_groups_list: %s\n" % e)
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
**200** | Successfully retrieved the list of industry groups. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **industry_groups_retrieve**
> IndustryGroup industry_groups_retrieve(id)

Retrieve GICS Industry Group

Retrieve details for a specific GICS Industry Group by its ID.

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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve GICS Industry Group
        api_response = await api_instance.industry_groups_retrieve(id)
        print("The response of GICSClassificationsApi->industry_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->industry_groups_retrieve: %s\n" % e)
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
**200** | Successfully retrieved the industry group details. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |
**404** | Industry Group not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sectors_list**
> PaginatedSectorList sectors_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, search=search)

List GICS Sectors

Retrieve a paginated list of GICS Sectors. Supports filtering by `code` (exact, case-insensitive, or multiple values) and partial `name` search.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_sector_list import PaginatedSectorList
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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        # List GICS Sectors
        api_response = await api_instance.sectors_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, search=search)
        print("The response of GICSClassificationsApi->sectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->sectors_list: %s\n" % e)
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

### Return type

[**PaginatedSectorList**](PaginatedSectorList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of sectors. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sectors_retrieve**
> Sector sectors_retrieve(id)

Retrieve GICS Sector

Retrieve details for a specific GICS Sector by its ID (primary key).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.sector import Sector
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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve GICS Sector
        api_response = await api_instance.sectors_retrieve(id)
        print("The response of GICSClassificationsApi->sectors_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->sectors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Sector**](Sector.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the sector details. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |
**404** | Sector not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_industries_list**
> PaginatedSubIndustryList sub_industries_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_code=industry_code, industry_code_in=industry_code_in, industry_group_code=industry_group_code, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code)

List GICS Sub-Industries

Retrieve a paginated list of GICS Sub-Industries. Supports filtering by `code`, `name`, parent `industry_code`, list of `industry_code_in`, grandparent `industry_group_code`, and great-grandparent `sector_code`.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_sub_industry_list import PaginatedSubIndustryList
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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    industry_code = 'industry_code_example' # str | Filter by parent Industry GICS code (e.g., 101010) (optional)
    industry_code_in = ['industry_code_in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    industry_group_code = 'industry_group_code_example' # str | Filter by grandparent Industry Group GICS code (e.g., 1010) (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    sector_code = 'sector_code_example' # str | Filter by great-grandparent Sector GICS code (e.g., 10) (optional)

    try:
        # List GICS Sub-Industries
        api_response = await api_instance.sub_industries_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_code=industry_code, industry_code_in=industry_code_in, industry_group_code=industry_group_code, name__icontains=name__icontains, page=page, page_size=page_size, search=search, sector_code=sector_code)
        print("The response of GICSClassificationsApi->sub_industries_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->sub_industries_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **code__iexact** | **str**|  | [optional] 
 **code__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **industry_code** | **str**| Filter by parent Industry GICS code (e.g., 101010) | [optional] 
 **industry_code_in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **industry_group_code** | **str**| Filter by grandparent Industry Group GICS code (e.g., 1010) | [optional] 
 **name__icontains** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **sector_code** | **str**| Filter by great-grandparent Sector GICS code (e.g., 10) | [optional] 

### Return type

[**PaginatedSubIndustryList**](PaginatedSubIndustryList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of sub-industries. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_industries_retrieve**
> SubIndustry sub_industries_retrieve(id)

Retrieve GICS Sub-Industry

Retrieve details for a specific GICS Sub-Industry by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.sub_industry import SubIndustry
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
    api_instance = financial_reports_generated_client.GICSClassificationsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve GICS Sub-Industry
        api_response = await api_instance.sub_industries_retrieve(id)
        print("The response of GICSClassificationsApi->sub_industries_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GICSClassificationsApi->sub_industries_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SubIndustry**](SubIndustry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the sub-industry details. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |
**404** | Sub-Industry not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

