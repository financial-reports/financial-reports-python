# financial_reports_generated_client.DefaultApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filing_processed_post**](DefaultApi.md#filing_processed_post) | **POST** /filing.processed | Filing Processed Event


# **filing_processed_post**
> filing_processed_post(filing_processed_payload=filing_processed_payload)

Filing Processed Event

Triggered when a new filing is successfully ingested, processed, and made available in the API. This is the primary event for tracking new data.

### Example


```python
import financial_reports_generated_client
from financial_reports_generated_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.financialreports.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = financial_reports_generated_client.Configuration(
    host = "https://api.financialreports.eu"
)


# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.DefaultApi(api_client)
    filing_processed_payload = financial_reports_generated_client.FilingProcessedPayload() # FilingProcessedPayload |  (optional)

    try:
        # Filing Processed Event
        await api_instance.filing_processed_post(filing_processed_payload=filing_processed_payload)
    except Exception as e:
        print("Exception when calling DefaultApi->filing_processed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filing_processed_payload** | [**FilingProcessedPayload**](FilingProcessedPayload.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (Success) Your endpoint should return a 2xx status code to acknowledge receipt. |  -  |
**4xx** | (Client Error) Your endpoint returned an error. We may retry based on the status code. |  -  |
**5xx** | (Server Error) Your endpoint is down or unavailable. We will retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

