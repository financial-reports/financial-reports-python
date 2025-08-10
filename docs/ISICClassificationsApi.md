# financial_reports_generated_client.ISICClassificationsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**isic_classes_list**](ISICClassificationsApi.md#isic_classes_list) | **GET** /isic-classes/ | List ISIC Classes
[**isic_classes_retrieve**](ISICClassificationsApi.md#isic_classes_retrieve) | **GET** /isic-classes/{id}/ | Retrieve ISIC Class
[**isic_divisions_list**](ISICClassificationsApi.md#isic_divisions_list) | **GET** /isic-divisions/ | List ISIC Divisions
[**isic_divisions_retrieve**](ISICClassificationsApi.md#isic_divisions_retrieve) | **GET** /isic-divisions/{id}/ | Retrieve ISIC Division
[**isic_groups_list**](ISICClassificationsApi.md#isic_groups_list) | **GET** /isic-groups/ | List ISIC Groups
[**isic_groups_retrieve**](ISICClassificationsApi.md#isic_groups_retrieve) | **GET** /isic-groups/{id}/ | Retrieve ISIC Group
[**isic_sections_list**](ISICClassificationsApi.md#isic_sections_list) | **GET** /isic-sections/ | List ISIC Sections
[**isic_sections_retrieve**](ISICClassificationsApi.md#isic_sections_retrieve) | **GET** /isic-sections/{id}/ | Retrieve ISIC Section


# **isic_classes_list**
> PaginatedISICClassList isic_classes_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_code=industry_code, industry_group_code=industry_group_code, name__icontains=name__icontains, page=page, page_size=page_size, sector_code=sector_code)

List ISIC Classes

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve a paginated list of ISIC Classes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_isic_class_list import PaginatedISICClassList
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    industry_code = 'industry_code_example' # str | Filter by parent ISIC Group code (e.g., 011) (optional)
    industry_group_code = 'industry_group_code_example' # str | Filter by grandparent ISIC Division code (e.g., 01) (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    sector_code = 'sector_code_example' # str | Filter by great-grandparent ISIC Section code (e.g., A) (optional)

    try:
        # List ISIC Classes
        api_response = await api_instance.isic_classes_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_code=industry_code, industry_group_code=industry_group_code, name__icontains=name__icontains, page=page, page_size=page_size, sector_code=sector_code)
        print("The response of ISICClassificationsApi->isic_classes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_classes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **code__iexact** | **str**|  | [optional] 
 **code__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **industry_code** | **str**| Filter by parent ISIC Group code (e.g., 011) | [optional] 
 **industry_group_code** | **str**| Filter by grandparent ISIC Division code (e.g., 01) | [optional] 
 **name__icontains** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sector_code** | **str**| Filter by great-grandparent ISIC Section code (e.g., A) | [optional] 

### Return type

[**PaginatedISICClassList**](PaginatedISICClassList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isic_classes_retrieve**
> ISICClass isic_classes_retrieve(id)

Retrieve ISIC Class

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve details for a specific ISIC Class by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.isic_class import ISICClass
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    id = 56 # int | A unique integer value identifying this sub industry.

    try:
        # Retrieve ISIC Class
        api_response = await api_instance.isic_classes_retrieve(id)
        print("The response of ISICClassificationsApi->isic_classes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_classes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sub industry. | 

### Return type

[**ISICClass**](ISICClass.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isic_divisions_list**
> PaginatedISICDivisionList isic_divisions_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, sector_code=sector_code)

List ISIC Divisions

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve a paginated list of ISIC Divisions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_isic_division_list import PaginatedISICDivisionList
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    sector_code = 'sector_code_example' # str | Filter by parent ISIC Section code (e.g., A) (optional)

    try:
        # List ISIC Divisions
        api_response = await api_instance.isic_divisions_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size, sector_code=sector_code)
        print("The response of ISICClassificationsApi->isic_divisions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_divisions_list: %s\n" % e)
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
 **sector_code** | **str**| Filter by parent ISIC Section code (e.g., A) | [optional] 

### Return type

[**PaginatedISICDivisionList**](PaginatedISICDivisionList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isic_divisions_retrieve**
> ISICDivision isic_divisions_retrieve(id)

Retrieve ISIC Division

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve details for a specific ISIC Division by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.isic_division import ISICDivision
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    id = 56 # int | A unique integer value identifying this industry group.

    try:
        # Retrieve ISIC Division
        api_response = await api_instance.isic_divisions_retrieve(id)
        print("The response of ISICClassificationsApi->isic_divisions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_divisions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this industry group. | 

### Return type

[**ISICDivision**](ISICDivision.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isic_groups_list**
> PaginatedISICGroupList isic_groups_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_group_code=industry_group_code, name__icontains=name__icontains, page=page, page_size=page_size, sector_code=sector_code)

List ISIC Groups

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve a paginated list of ISIC Groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_isic_group_list import PaginatedISICGroupList
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    industry_group_code = 'industry_group_code_example' # str | Filter by parent ISIC Division code (e.g., 01) (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    sector_code = 'sector_code_example' # str | Filter by grandparent ISIC Section code (e.g., A) (optional)

    try:
        # List ISIC Groups
        api_response = await api_instance.isic_groups_list(code=code, code__iexact=code__iexact, code__in=code__in, industry_group_code=industry_group_code, name__icontains=name__icontains, page=page, page_size=page_size, sector_code=sector_code)
        print("The response of ISICClassificationsApi->isic_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **code__iexact** | **str**|  | [optional] 
 **code__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **industry_group_code** | **str**| Filter by parent ISIC Division code (e.g., 01) | [optional] 
 **name__icontains** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sector_code** | **str**| Filter by grandparent ISIC Section code (e.g., A) | [optional] 

### Return type

[**PaginatedISICGroupList**](PaginatedISICGroupList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isic_groups_retrieve**
> ISICGroup isic_groups_retrieve(id)

Retrieve ISIC Group

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve details for a specific ISIC Group by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.isic_group import ISICGroup
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    id = 56 # int | A unique integer value identifying this industry.

    try:
        # Retrieve ISIC Group
        api_response = await api_instance.isic_groups_retrieve(id)
        print("The response of ISICClassificationsApi->isic_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this industry. | 

### Return type

[**ISICGroup**](ISICGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isic_sections_list**
> PaginatedISICSectionList isic_sections_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size)

List ISIC Sections

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve a paginated list of ISIC Sections.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_isic_section_list import PaginatedISICSectionList
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    code = 'code_example' # str |  (optional)
    code__iexact = 'code__iexact_example' # str |  (optional)
    code__in = ['code__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List ISIC Sections
        api_response = await api_instance.isic_sections_list(code=code, code__iexact=code__iexact, code__in=code__in, name__icontains=name__icontains, page=page, page_size=page_size)
        print("The response of ISICClassificationsApi->isic_sections_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_sections_list: %s\n" % e)
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

### Return type

[**PaginatedISICSectionList**](PaginatedISICSectionList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isic_sections_retrieve**
> ISICSection isic_sections_retrieve(id)

Retrieve ISIC Section

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve details for a specific ISIC Section by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.isic_section import ISICSection
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
    api_instance = financial_reports_generated_client.ISICClassificationsApi(api_client)
    id = 56 # int | A unique integer value identifying this sector.

    try:
        # Retrieve ISIC Section
        api_response = await api_instance.isic_sections_retrieve(id)
        print("The response of ISICClassificationsApi->isic_sections_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ISICClassificationsApi->isic_sections_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sector. | 

### Return type

[**ISICSection**](ISICSection.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

