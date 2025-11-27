# financial_reports_generated_client.FilingCategoriesApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filing_categories_list**](FilingCategoriesApi.md#filing_categories_list) | **GET** /filing-categories/ | List Filing Categories
[**filing_categories_retrieve**](FilingCategoriesApi.md#filing_categories_retrieve) | **GET** /filing-categories/{id}/ | Retrieve Filing Category


# **filing_categories_list**
> PaginatedFilingCategoryList filing_categories_list(page=page, page_size=page_size)

List Filing Categories

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve the 11 standardized disclosure types (categories) defined by the FRCF.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_filing_category_list import PaginatedFilingCategoryList
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
    api_instance = financial_reports_generated_client.FilingCategoriesApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List Filing Categories
        api_response = await api_instance.filing_categories_list(page=page, page_size=page_size)
        print("The response of FilingCategoriesApi->filing_categories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingCategoriesApi->filing_categories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedFilingCategoryList**](PaginatedFilingCategoryList.md)

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

# **filing_categories_retrieve**
> FilingCategory filing_categories_retrieve(id)

Retrieve Filing Category

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve details for a specific filing category by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.filing_category import FilingCategory
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
    api_instance = financial_reports_generated_client.FilingCategoriesApi(api_client)
    id = 56 # int | A unique integer value identifying this filing category.

    try:
        # Retrieve Filing Category
        api_response = await api_instance.filing_categories_retrieve(id)
        print("The response of FilingCategoriesApi->filing_categories_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingCategoriesApi->filing_categories_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filing category. | 

### Return type

[**FilingCategory**](FilingCategory.md)

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

