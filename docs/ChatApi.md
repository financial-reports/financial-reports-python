# financial_reports_generated_client.ChatApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_sessions_destroy**](ChatApi.md#chat_sessions_destroy) | **DELETE** /chat/sessions/{session_id}/ | 
[**chat_sessions_messages_retrieve**](ChatApi.md#chat_sessions_messages_retrieve) | **GET** /chat/sessions/{session_id}/messages/ | 
[**chat_sessions_partial_update**](ChatApi.md#chat_sessions_partial_update) | **PATCH** /chat/sessions/{session_id}/ | 
[**chat_sessions_share_create**](ChatApi.md#chat_sessions_share_create) | **POST** /chat/sessions/{session_id}/share/ | 
[**chat_sessions_title_retrieve**](ChatApi.md#chat_sessions_title_retrieve) | **GET** /chat/sessions/{session_id}/title/ | 
[**chat_stream_create**](ChatApi.md#chat_stream_create) | **POST** /chat/stream/ | 


# **chat_sessions_destroy**
> chat_sessions_destroy(session_id)

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
    api_instance = financial_reports_generated_client.ChatApi(api_client)
    session_id = 56 # int | 

    try:
        await api_instance.chat_sessions_destroy(session_id)
    except Exception as e:
        print("Exception when calling ChatApi->chat_sessions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_sessions_messages_retrieve**
> chat_sessions_messages_retrieve(session_id)

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
    api_instance = financial_reports_generated_client.ChatApi(api_client)
    session_id = 56 # int | 

    try:
        await api_instance.chat_sessions_messages_retrieve(session_id)
    except Exception as e:
        print("Exception when calling ChatApi->chat_sessions_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_sessions_partial_update**
> chat_sessions_partial_update(session_id)

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
    api_instance = financial_reports_generated_client.ChatApi(api_client)
    session_id = 56 # int | 

    try:
        await api_instance.chat_sessions_partial_update(session_id)
    except Exception as e:
        print("Exception when calling ChatApi->chat_sessions_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_sessions_share_create**
> chat_sessions_share_create(session_id)

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
    api_instance = financial_reports_generated_client.ChatApi(api_client)
    session_id = 56 # int | 

    try:
        await api_instance.chat_sessions_share_create(session_id)
    except Exception as e:
        print("Exception when calling ChatApi->chat_sessions_share_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_sessions_title_retrieve**
> chat_sessions_title_retrieve(session_id)

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
    api_instance = financial_reports_generated_client.ChatApi(api_client)
    session_id = 56 # int | 

    try:
        await api_instance.chat_sessions_title_retrieve(session_id)
    except Exception as e:
        print("Exception when calling ChatApi->chat_sessions_title_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_stream_create**
> chat_stream_create()

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
    api_instance = financial_reports_generated_client.ChatApi(api_client)

    try:
        await api_instance.chat_stream_create()
    except Exception as e:
        print("Exception when calling ChatApi->chat_stream_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

