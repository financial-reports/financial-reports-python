# financial_reports_generated_client.FinancialDataApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**line_item_definitions_list**](FinancialDataApi.md#line_item_definitions_list) | **GET** /line-item-definitions/ | List Line Item Definitions
[**line_item_definitions_retrieve**](FinancialDataApi.md#line_item_definitions_retrieve) | **GET** /line-item-definitions/{code}/ | Retrieve Line Item Definition


# **line_item_definitions_list**
> PaginatedLineItemDefinitionList line_item_definitions_list(depth=depth, is_capital_iq_standard=is_capital_iq_standard, page=page, page_size=page_size, parent_code=parent_code, search=search, statement_type=statement_type)

List Line Item Definitions

Retrieve the full dictionary of standardized financial KPIs.

Each definition describes one line item that may appear in extracted financial statements (Income Statement, Balance Sheet, Cash Flow Statement). Use the `depth` and `parent_code` fields to reconstruct the Capital IQ-style hierarchy.

**Access Level Required:** Requires **Standard Access (Level 1)**.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_line_item_definition_list import PaginatedLineItemDefinitionList
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
    api_instance = financial_reports_generated_client.FinancialDataApi(api_client)
    depth = 56 # int | Filter by hierarchy depth (0 = top-level, 1 = component, 2 = sub-component). (optional)
    is_capital_iq_standard = True # bool |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    parent_code = 'parent_code_example' # str | Filter by parent line item code (e.g. 'gross_profit' returns its children). (optional)
    search = 'search_example' # str | A search term. (optional)
    statement_type = 'statement_type_example' # str | Filter by statement type (IS, BS, CFS, SUP).  * `IS` - Income Statement * `BS` - Balance Sheet * `CFS` - Cash Flow Statement * `SUP` - Supplemental / Ratio (optional)

    try:
        # List Line Item Definitions
        api_response = await api_instance.line_item_definitions_list(depth=depth, is_capital_iq_standard=is_capital_iq_standard, page=page, page_size=page_size, parent_code=parent_code, search=search, statement_type=statement_type)
        print("The response of FinancialDataApi->line_item_definitions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->line_item_definitions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **int**| Filter by hierarchy depth (0 &#x3D; top-level, 1 &#x3D; component, 2 &#x3D; sub-component). | [optional] 
 **is_capital_iq_standard** | **bool**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent_code** | **str**| Filter by parent line item code (e.g. &#39;gross_profit&#39; returns its children). | [optional] 
 **search** | **str**| A search term. | [optional] 
 **statement_type** | **str**| Filter by statement type (IS, BS, CFS, SUP).  * &#x60;IS&#x60; - Income Statement * &#x60;BS&#x60; - Balance Sheet * &#x60;CFS&#x60; - Cash Flow Statement * &#x60;SUP&#x60; - Supplemental / Ratio | [optional] 

### Return type

[**PaginatedLineItemDefinitionList**](PaginatedLineItemDefinitionList.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **line_item_definitions_retrieve**
> LineItemDefinition line_item_definitions_retrieve(code)

Retrieve Line Item Definition

Retrieve a single line item definition by its code.

**Access Level Required:** Requires **Standard Access (Level 1)**.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.line_item_definition import LineItemDefinition
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
    api_instance = financial_reports_generated_client.FinancialDataApi(api_client)
    code = 'code_example' # str | 

    try:
        # Retrieve Line Item Definition
        api_response = await api_instance.line_item_definitions_retrieve(code)
        print("The response of FinancialDataApi->line_item_definitions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->line_item_definitions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**LineItemDefinition**](LineItemDefinition.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

