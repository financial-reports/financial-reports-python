# financial_reports_generated_client.WebhooksManagementApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_create**](WebhooksManagementApi.md#webhooks_create) | **POST** /webhooks/ | Create Webhook
[**webhooks_destroy**](WebhooksManagementApi.md#webhooks_destroy) | **DELETE** /webhooks/{id}/ | Delete Webhook
[**webhooks_list**](WebhooksManagementApi.md#webhooks_list) | **GET** /webhooks/ | List Webhooks
[**webhooks_partial_update**](WebhooksManagementApi.md#webhooks_partial_update) | **PATCH** /webhooks/{id}/ | Partial Update Webhook
[**webhooks_regenerate_secret_create**](WebhooksManagementApi.md#webhooks_regenerate_secret_create) | **POST** /webhooks/{id}/regenerate-secret/ | Regenerate Secret Key
[**webhooks_retrieve**](WebhooksManagementApi.md#webhooks_retrieve) | **GET** /webhooks/{id}/ | Retrieve Webhook
[**webhooks_test_create**](WebhooksManagementApi.md#webhooks_test_create) | **POST** /webhooks/{id}/test/ | Test Webhook
[**webhooks_update**](WebhooksManagementApi.md#webhooks_update) | **PUT** /webhooks/{id}/ | Update Webhook


# **webhooks_create**
> Webhook webhooks_create(webhook)

Create Webhook

Create a new webhook subscription. The `secret_key` will be generated and returned to you.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    webhook = {"url":"https://api.your-domain.com/webhook-receiver","is_active":true,"include_markdown":false,"include_isins":false,"subscribed_filing_types":["10-K","Annual Report"]} # Webhook | 

    try:
        # Create Webhook
        api_response = await api_instance.webhooks_create(webhook)
        print("The response of WebhooksManagementApi->webhooks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_destroy**
> webhooks_destroy(id)

Delete Webhook

Permanently delete a webhook subscription by its ID.

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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.

    try:
        # Delete Webhook
        await api_instance.webhooks_destroy(id)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_list**
> PaginatedWebhookList webhooks_list(page=page, page_size=page_size)

List Webhooks

Retrieve a list of all webhooks configured for your account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_webhook_list import PaginatedWebhookList
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List Webhooks
        api_response = await api_instance.webhooks_list(page=page, page_size=page_size)
        print("The response of WebhooksManagementApi->webhooks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedWebhookList**](PaginatedWebhookList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_partial_update**
> Webhook webhooks_partial_update(id, patched_webhook=patched_webhook)

Partial Update Webhook

Partially update the details of a specific webhook. Note: The `secret_key` cannot be set via this endpoint.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.patched_webhook import PatchedWebhook
from financial_reports_generated_client.models.webhook import Webhook
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.
    patched_webhook = {"is_active":false} # PatchedWebhook |  (optional)

    try:
        # Partial Update Webhook
        api_response = await api_instance.webhooks_partial_update(id, patched_webhook=patched_webhook)
        print("The response of WebhooksManagementApi->webhooks_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 
 **patched_webhook** | [**PatchedWebhook**](PatchedWebhook.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

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

# **webhooks_regenerate_secret_create**
> WebhookRegenerateSecret webhooks_regenerate_secret_create(id, webhook)

Regenerate Secret Key

Generates a new, unique `secret_key` for this webhook. The old key will be invalidated immediately. This action is irreversible.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
from financial_reports_generated_client.models.webhook_regenerate_secret import WebhookRegenerateSecret
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.
    webhook = financial_reports_generated_client.Webhook() # Webhook | 

    try:
        # Regenerate Secret Key
        api_response = await api_instance.webhooks_regenerate_secret_create(id, webhook)
        print("The response of WebhooksManagementApi->webhooks_regenerate_secret_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_regenerate_secret_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 
 **webhook** | [**Webhook**](Webhook.md)|  | 

### Return type

[**WebhookRegenerateSecret**](WebhookRegenerateSecret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully regenerated the secret key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_retrieve**
> Webhook webhooks_retrieve(id)

Retrieve Webhook

Retrieve the details of a specific webhook by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.

    try:
        # Retrieve Webhook
        api_response = await api_instance.webhooks_retrieve(id)
        print("The response of WebhooksManagementApi->webhooks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_test_create**
> webhooks_test_create(id, webhook)

Test Webhook

Sends a pre-defined 'filing.processed.test' event to the configured webhook URL to verify its functionality.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.
    webhook = financial_reports_generated_client.Webhook() # Webhook | 

    try:
        # Test Webhook
        await api_instance.webhooks_test_create(id, webhook)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_test_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 
 **webhook** | [**Webhook**](Webhook.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test event was sent and the endpoint responded successfully. |  -  |
**400** | Test event failed (e.g., endpoint returned an error, invalid URL). |  -  |
**408** | Test event timed out. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update**
> Webhook webhooks_update(id, webhook)

Update Webhook

Update the details of a specific webhook. Note: The `secret_key` cannot be set via this endpoint.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.
    webhook = {url=https://api.your-domain.com/webhook-receiver, is_active=true, include_markdown=false, include_isins=false, subscribed_filing_types=[10-K, Annual Report]} # Webhook | 

    try:
        # Update Webhook
        api_response = await api_instance.webhooks_update(id, webhook)
        print("The response of WebhooksManagementApi->webhooks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 
 **webhook** | [**Webhook**](Webhook.md)|  | 

### Return type

[**Webhook**](Webhook.md)

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

