# financial_reports_generated_client.ChatAgentApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_sessions_destroy**](ChatAgentApi.md#chat_sessions_destroy) | **DELETE** /chat/sessions/{session_id}/ | Delete Chat Session
[**chat_sessions_messages_retrieve**](ChatAgentApi.md#chat_sessions_messages_retrieve) | **GET** /chat/sessions/{session_id}/messages/ | Retrieve Chat History
[**chat_sessions_partial_update**](ChatAgentApi.md#chat_sessions_partial_update) | **PATCH** /chat/sessions/{session_id}/ | Update Chat Session
[**chat_stream_create**](ChatAgentApi.md#chat_stream_create) | **POST** /chat/stream/ | Stream Financial Assistant Agent


# **chat_sessions_destroy**
> chat_sessions_destroy(session_id)

Delete Chat Session

Permanently deletes a chat session and all associated messages.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
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
    api_instance = financial_reports_generated_client.ChatAgentApi(api_client)
    session_id = 56 # int | 

    try:
        # Delete Chat Session
        await api_instance.chat_sessions_destroy(session_id)
    except Exception as e:
        print("Exception when calling ChatAgentApi->chat_sessions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Session deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_sessions_messages_retrieve**
> ChatMessageList chat_sessions_messages_retrieve(session_id)

Retrieve Chat History

Fetches all messages for a specific chat session, including context metadata.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.chat_message_list import ChatMessageList
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
    api_instance = financial_reports_generated_client.ChatAgentApi(api_client)
    session_id = 56 # int | 

    try:
        # Retrieve Chat History
        api_response = await api_instance.chat_sessions_messages_retrieve(session_id)
        print("The response of ChatAgentApi->chat_sessions_messages_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAgentApi->chat_sessions_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 

### Return type

[**ChatMessageList**](ChatMessageList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Session not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_sessions_partial_update**
> ChatSessionUpdateResponse chat_sessions_partial_update(session_id, patched_chat_session_update_request=patched_chat_session_update_request)

Update Chat Session

Rename a chat session title.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.chat_session_update_response import ChatSessionUpdateResponse
from financial_reports_generated_client.models.patched_chat_session_update_request import PatchedChatSessionUpdateRequest
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
    api_instance = financial_reports_generated_client.ChatAgentApi(api_client)
    session_id = 56 # int | 
    patched_chat_session_update_request = financial_reports_generated_client.PatchedChatSessionUpdateRequest() # PatchedChatSessionUpdateRequest |  (optional)

    try:
        # Update Chat Session
        api_response = await api_instance.chat_sessions_partial_update(session_id, patched_chat_session_update_request=patched_chat_session_update_request)
        print("The response of ChatAgentApi->chat_sessions_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAgentApi->chat_sessions_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**|  | 
 **patched_chat_session_update_request** | [**PatchedChatSessionUpdateRequest**](PatchedChatSessionUpdateRequest.md)|  | [optional] 

### Return type

[**ChatSessionUpdateResponse**](ChatSessionUpdateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_stream_create**
> SSEEvent chat_stream_create(chat_interaction_request=chat_interaction_request)

Stream Financial Assistant Agent

Streams the Gemini agent's thoughts, tool calls, and final response using Server-Sent Events (SSE).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.chat_interaction_request import ChatInteractionRequest
from financial_reports_generated_client.models.sse_event import SSEEvent
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
    api_instance = financial_reports_generated_client.ChatAgentApi(api_client)
    chat_interaction_request = financial_reports_generated_client.ChatInteractionRequest() # ChatInteractionRequest |  (optional)

    try:
        # Stream Financial Assistant Agent
        api_response = await api_instance.chat_stream_create(chat_interaction_request=chat_interaction_request)
        print("The response of ChatAgentApi->chat_stream_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAgentApi->chat_stream_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_interaction_request** | [**ChatInteractionRequest**](ChatInteractionRequest.md)|  | [optional] 

### Return type

[**SSEEvent**](SSEEvent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE Stream. Events include: &#x60;session_created&#x60;, &#x60;status&#x60;, &#x60;thought&#x60;, &#x60;tool_call&#x60;, &#x60;tool_execution_start&#x60;, &#x60;tool_execution_result&#x60;, &#x60;text&#x60;, &#x60;citation&#x60;, &#x60;error&#x60;, and &#x60;done&#x60;. Chat titles are generated asynchronously after session creation. |  -  |
**400** | Bad Request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

