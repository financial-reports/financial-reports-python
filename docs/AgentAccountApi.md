# financial_reports_generated_client.AgentAccountApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_checkout_link**](AgentAccountApi.md#agent_checkout_link) | **POST** /agent/checkout-link/ | Mint a Stripe link for the owner to add a card (pay-as-you-go)
[**agent_key_rotate**](AgentAccountApi.md#agent_key_rotate) | **POST** /agent/key/rotate/ | Rotate this agent key
[**agent_owner_confirmation**](AgentAccountApi.md#agent_owner_confirmation) | **POST** /agent/owner-confirmation/ | Email the account owner a confirmation link
[**agent_signup**](AgentAccountApi.md#agent_signup) | **POST** /agent/signup/ | Create an API key as an AI agent
[**agent_status**](AgentAccountApi.md#agent_status) | **GET** /agent/status/ | Agent account status


# **agent_checkout_link**
> Dict[str, Optional[object]] agent_checkout_link()

Mint a Stripe link for the owner to add a card (pay-as-you-go)

E5 ``POST /agent/checkout-link``.

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
    api_instance = financial_reports_generated_client.AgentAccountApi(api_client)

    try:
        # Mint a Stripe link for the owner to add a card (pay-as-you-go)
        api_response = await api_instance.agent_checkout_link()
        print("The response of AgentAccountApi->agent_checkout_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAccountApi->agent_checkout_link: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Optional[object]]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**200** | Open link reused. |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_key_rotate**
> Dict[str, Optional[object]] agent_key_rotate()

Rotate this agent key

E6 ``POST /agent/key/rotate``: requires the CURRENT key (never by email).

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
    api_instance = financial_reports_generated_client.AgentAccountApi(api_client)

    try:
        # Rotate this agent key
        api_response = await api_instance.agent_key_rotate()
        print("The response of AgentAccountApi->agent_key_rotate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAccountApi->agent_key_rotate: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Optional[object]]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**429** |  |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_owner_confirmation**
> Dict[str, Optional[object]] agent_owner_confirmation()

Email the account owner a confirmation link

E4 ``POST /agent/owner-confirmation``.

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
    api_instance = financial_reports_generated_client.AgentAccountApi(api_client)

    try:
        # Email the account owner a confirmation link
        api_response = await api_instance.agent_owner_confirmation()
        print("The response of AgentAccountApi->agent_owner_confirmation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAccountApi->agent_owner_confirmation: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Optional[object]]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_signup**
> Dict[str, Optional[object]] agent_signup(agent_signup_request)

Create an API key as an AI agent

Creates an account for the given email and returns an API key once. No email is sent. The key works for a small Level-1 read-only sandbox; beyond it data calls return 402 until the owner confirms (POST /agent/owner-confirmation) or a card is added (POST /agent/checkout-link).

### Example


```python
import financial_reports_generated_client
from financial_reports_generated_client.models.agent_signup_request import AgentSignupRequest
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
    api_instance = financial_reports_generated_client.AgentAccountApi(api_client)
    agent_signup_request = {"email":"dana@acme-quant.com","agent_name":"acme-research-bot"} # AgentSignupRequest | 

    try:
        # Create an API key as an AI agent
        api_response = await api_instance.agent_signup(agent_signup_request)
        print("The response of AgentAccountApi->agent_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAccountApi->agent_signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_signup_request** | [**AgentSignupRequest**](AgentSignupRequest.md)|  | 

### Return type

**Dict[str, Optional[object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Key created (shown once). |  -  |
**400** | invalid_email / email_not_allowed / invalid_agent_name. |  -  |
**409** | account_exists. |  -  |
**429** | rate_limited. |  -  |
**503** | signup_paused / signup_unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_status**
> Dict[str, Optional[object]] agent_status()

Agent account status

E3 ``GET /agent/status``.

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
    api_instance = financial_reports_generated_client.AgentAccountApi(api_client)

    try:
        # Agent account status
        api_response = await api_instance.agent_status()
        print("The response of AgentAccountApi->agent_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAccountApi->agent_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Optional[object]]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

