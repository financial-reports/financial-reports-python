# financial_reports_generated_client.DownloaderApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloader_jobs_status_retrieve**](DownloaderApi.md#downloader_jobs_status_retrieve) | **GET** /downloader/jobs/{job_id}/status/ | 


# **downloader_jobs_status_retrieve**
> JobStatus downloader_jobs_status_retrieve(job_id)

### Example

* Api Key Authentication (cookieAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.job_status import JobStatus
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with financial_reports_generated_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = financial_reports_generated_client.DownloaderApi(api_client)
    job_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        api_response = await api_instance.downloader_jobs_status_retrieve(job_id)
        print("The response of DownloaderApi->downloader_jobs_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloaderApi->downloader_jobs_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **UUID**|  | 

### Return type

[**JobStatus**](JobStatus.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

