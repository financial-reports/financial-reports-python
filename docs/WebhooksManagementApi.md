# financial_reports_generated_client.WebhooksManagementApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_create**](WebhooksManagementApi.md#webhooks_create) | **POST** /webhooks/ | Create Webhook
[**webhooks_deliveries_replay_create**](WebhooksManagementApi.md#webhooks_deliveries_replay_create) | **POST** /webhooks/{id}/deliveries/{delivery_uuid}/replay/ | Replay Delivery
[**webhooks_deliveries_retrieve**](WebhooksManagementApi.md#webhooks_deliveries_retrieve) | **GET** /webhooks/{id}/deliveries/ | List Delivery Logs
[**webhooks_delivery_detail_retrieve**](WebhooksManagementApi.md#webhooks_delivery_detail_retrieve) | **GET** /webhooks/{id}/deliveries/{delivery_uuid}/ | Retrieve Delivery Detail
[**webhooks_destroy**](WebhooksManagementApi.md#webhooks_destroy) | **DELETE** /webhooks/{id}/ | Delete Webhook
[**webhooks_list**](WebhooksManagementApi.md#webhooks_list) | **GET** /webhooks/ | List Webhooks
[**webhooks_partial_update**](WebhooksManagementApi.md#webhooks_partial_update) | **PATCH** /webhooks/{id}/ | Partial Update Webhook
[**webhooks_regenerate_secret_create**](WebhooksManagementApi.md#webhooks_regenerate_secret_create) | **POST** /webhooks/{id}/regenerate-secret/ | Regenerate Secret Key
[**webhooks_retrieve**](WebhooksManagementApi.md#webhooks_retrieve) | **GET** /webhooks/{id}/ | Retrieve Webhook
[**webhooks_test_create**](WebhooksManagementApi.md#webhooks_test_create) | **POST** /webhooks/{id}/test/ | Test Webhook
[**webhooks_update**](WebhooksManagementApi.md#webhooks_update) | **PUT** /webhooks/{id}/ | Update Webhook


# **webhooks_create**
> WebhookCreateResponse webhooks_create(webhook)

Create Webhook

Creates a webhook. The `secret_key` is in this response **only**, so store it.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
from financial_reports_generated_client.models.webhook_create_response import WebhookCreateResponse
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    webhook = {"url":"https://api.your-domain.com/webhook-receiver","is_active":true,"include_markdown":false,"include_isins":false,"trigger_on_filing_received":false,"trigger_on_filing_processed":true,"trigger_on_filing_updated":false,"trigger_on_dividend_events":false,"deliver_late_filings":false,"track_all_companies":false,"subscribed_filing_types":["10-K","IR"]} # Webhook | 

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

[**WebhookCreateResponse**](WebhookCreateResponse.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webhook created. The &#x60;secret_key&#x60; is returned only in this response. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_deliveries_replay_create**
> WebhookReplayResponse webhooks_deliveries_replay_create(delivery_uuid, id, webhook)

Replay Delivery

Queues the delivery's event to be sent again (202). The new attempt appears in the delivery logs. `filing.removed` and dividend events can't be replayed.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
from financial_reports_generated_client.models.webhook_replay_response import WebhookReplayResponse
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    delivery_uuid = 'delivery_uuid_example' # str | 
    id = 56 # int | A unique integer value identifying this webhook.
    webhook = financial_reports_generated_client.Webhook() # Webhook | 

    try:
        # Replay Delivery
        api_response = await api_instance.webhooks_deliveries_replay_create(delivery_uuid, id, webhook)
        print("The response of WebhooksManagementApi->webhooks_deliveries_replay_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_deliveries_replay_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this webhook. | 
 **webhook** | [**Webhook**](Webhook.md)|  | 

### Return type

[**WebhookReplayResponse**](WebhookReplayResponse.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Replay has been queued. |  -  |
**404** | Delivery not found for this webhook. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_deliveries_retrieve**
> PaginatedWebhookDeliveryList webhooks_deliveries_retrieve(id)

List Delivery Logs

The webhook's delivery attempts, paginated.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_webhook_delivery_list import PaginatedWebhookDeliveryList
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.

    try:
        # List Delivery Logs
        api_response = await api_instance.webhooks_deliveries_retrieve(id)
        print("The response of WebhooksManagementApi->webhooks_deliveries_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_deliveries_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 

### Return type

[**PaginatedWebhookDeliveryList**](PaginatedWebhookDeliveryList.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved delivery logs. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_delivery_detail_retrieve**
> WebhookDeliveryDetail webhooks_delivery_detail_retrieve(delivery_uuid, id)

Retrieve Delivery Detail

One delivery attempt, with the request payload and headers. The payload is rebuilt from the filing as it is now.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook_delivery_detail import WebhookDeliveryDetail
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    delivery_uuid = 'delivery_uuid_example' # str | 
    id = 56 # int | A unique integer value identifying this webhook.

    try:
        # Retrieve Delivery Detail
        api_response = await api_instance.webhooks_delivery_detail_retrieve(delivery_uuid, id)
        print("The response of WebhooksManagementApi->webhooks_delivery_detail_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_delivery_detail_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this webhook. | 

### Return type

[**WebhookDeliveryDetail**](WebhookDeliveryDetail.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved delivery details. |  -  |
**404** | Delivery not found for this webhook. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_destroy**
> webhooks_destroy(id)

Delete Webhook

Deletes a webhook permanently.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
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

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_list**
> PaginatedWebhookList webhooks_list(page=page, page_size=page_size)

List Webhooks

All webhooks on your account. Secret keys are not included.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
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

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_partial_update**
> Webhook webhooks_partial_update(id, patched_webhook=patched_webhook)

Partial Update Webhook

Changes only the fields you send.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
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

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_regenerate_secret_create**
> WebhookSecret webhooks_regenerate_secret_create(id, webhook)

Regenerate Secret Key

Issues a new `secret_key` for this webhook. The old key stops working immediately.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
from financial_reports_generated_client.models.webhook_secret import WebhookSecret
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

[**WebhookSecret**](WebhookSecret.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully regenerated the secret key. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_retrieve**
> Webhook webhooks_retrieve(id)

Retrieve Webhook

One webhook by its ID. The secret key is not included.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
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

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_test_create**
> WebhookTestResponse webhooks_test_create(id, webhook)

Test Webhook

Sends a `filing.processed.test` event to the webhook's URL and reports how it answered. The attempt appears in the delivery logs.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.webhook import Webhook
from financial_reports_generated_client.models.webhook_test_response import WebhookTestResponse
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.
    webhook = financial_reports_generated_client.Webhook() # Webhook | 

    try:
        # Test Webhook
        api_response = await api_instance.webhooks_test_create(id, webhook)
        print("The response of WebhooksManagementApi->webhooks_test_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagementApi->webhooks_test_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this webhook. | 
 **webhook** | [**Webhook**](Webhook.md)|  | 

### Return type

[**WebhookTestResponse**](WebhookTestResponse.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test event was sent and the endpoint responded successfully. |  -  |
**400** | Test event failed (e.g., endpoint returned an error, invalid URL). |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update**
> Webhook webhooks_update(id, webhook)

Update Webhook

Replaces a webhook's settings.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
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
    api_instance = financial_reports_generated_client.WebhooksManagementApi(api_client)
    id = 56 # int | A unique integer value identifying this webhook.
    webhook = {url=https://api.your-domain.com/webhook-receiver, is_active=true, include_markdown=false, include_isins=false, trigger_on_filing_received=false, trigger_on_filing_processed=true, trigger_on_filing_updated=false, trigger_on_dividend_events=false, deliver_late_filings=false, track_all_companies=false, subscribed_filing_types=[10-K, IR]} # Webhook | 

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

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

