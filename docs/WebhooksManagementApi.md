# financial_reports_generated_client.WebhooksManagementApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filing_processed_post**](WebhooksManagementApi.md#filing_processed_post) | **POST** /filing.processed | Filing Processed Event
[**filing_received_post**](WebhooksManagementApi.md#filing_received_post) | **POST** /filing.received | Filing Received Event


# **filing_processed_post**
> filing_processed_post(filing_processed_payload=filing_processed_payload)

Filing Processed Event

Triggered when a filing has been successfully analyzed, classified, and converted to Markdown. This event contains the complete metadata and content.

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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    filing_processed_payload = financial_reports_generated_client.FilingProcessedPayload() # FilingProcessedPayload |  (optional)

    try:
        # Filing Processed Event
        await api_instance.filing_processed_post(filing_processed_payload=filing_processed_payload)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->filing_processed_post: %s\n" % e)
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
**200** | (Success) Acknowledge receipt. |  -  |
**4xx** | (Client Error) Retry logic may apply. |  -  |
**5xx** | (Server Error) We will retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filing_received_post**
> filing_received_post(filing_processed_payload=filing_processed_payload)

Filing Received Event

Triggered immediately when a filing is ingested. Metadata (Filing Type, Language) and Markdown content may be null at this stage.

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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    filing_processed_payload = financial_reports_generated_client.FilingProcessedPayload() # FilingProcessedPayload |  (optional)

    try:
        # Filing Received Event
        await api_instance.filing_received_post(filing_processed_payload=filing_processed_payload)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->filing_received_post: %s\n" % e)
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
**200** | (Success) Acknowledge receipt. |  -  |
**4xx** | (Client Error) Retry logic may apply. |  -  |
**5xx** | (Server Error) We will retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

