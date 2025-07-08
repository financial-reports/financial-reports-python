# financial_reports_generated_client.ProcessedFilingsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**processed_filings_retrieve**](ProcessedFilingsApi.md#processed_filings_retrieve) | **GET** /processed-filings/{id}/ | Retrieve Processed Filing Content


# **processed_filings_retrieve**
> ProcessedFiling processed_filings_retrieve(id)

Retrieve Processed Filing Content

Retrieve the processed content (e.g., markdown) for a single filing by its ProcessedFiling ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.processed_filing import ProcessedFiling
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
    api_instance = financial_reports_generated_client.ProcessedFilingsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve Processed Filing Content
        api_response = await api_instance.processed_filings_retrieve(id)
        print("The response of ProcessedFilingsApi->processed_filings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessedFilingsApi->processed_filings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProcessedFiling**](ProcessedFiling.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the processed filing content. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |
**404** | Processed filing not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

