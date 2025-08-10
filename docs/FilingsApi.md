# financial_reports_generated_client.FilingsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filings_list**](FilingsApi.md#filings_list) | **GET** /filings/ | List Filings
[**filings_markdown_retrieve**](FilingsApi.md#filings_markdown_retrieve) | **GET** /filings/{filing_id}/markdown/ | Retrieve Filing Markdown
[**filings_retrieve**](FilingsApi.md#filings_retrieve) | **GET** /filings/{id}/ | Retrieve Filing Details


# **filings_list**
> PaginatedFilingSummaryList filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, company=company, company_isin=company_isin, countries=countries, dissemination_datetime_from=dissemination_datetime_from, dissemination_datetime_to=dissemination_datetime_to, language=language, languages=languages, lei=lei, ordering=ordering, page=page, page_size=page_size, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, type=type, updated_date_from=updated_date_from, updated_date_to=updated_date_to)

List Filings

Retrieve a paginated list of regulatory filings.
This endpoint supports extensive filtering via query parameters, including:
- **Company Identification**: Filter by internal `company` ID, `company_isin` (case-insensitive), or company `lei`.
- **Company Location**: Filter by `countries` using comma-separated ISO Alpha-2 codes (e.g., `US,GB`).
- **Filing Attributes**: Filter by `source` ID, `language` (single ISO 639-1 code), `languages` (comma-separated ISO 639-1 codes), or filing `type` code.
- **Date Ranges**: Filter by various date fields. All datetime filters expect an ISO 8601 format (e.g., `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DD`):
    - `added_to_platform_from` / `added_to_platform_to`: Date the filing was added to the platform.
    - `dissemination_datetime_from` / `dissemination_datetime_to`: Original dissemination date/time of the filing.
    - `release_datetime_from` / `release_datetime_to`: Actual release date/time of the filing.

Additionally, you can use the `search` parameter to perform a text search across the company name and filing title.
Results can be ordered using the `ordering` parameter with the fields: `release_datetime` and `added_to_platform` (e.g., `?ordering=-release_datetime`).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_filing_summary_list import PaginatedFilingSummaryList
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
    api_instance = financial_reports_generated_client.FilingsApi(api_client)
    added_to_platform_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by date added to platform (inclusive start date, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    added_to_platform_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by date added to platform (inclusive end date, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    company = 56 # int | Filter by internal Company ID. (optional)
    company_isin = 'company_isin_example' # str | Filter by Company ISIN. Case-insensitive. (optional)
    countries = 'countries_example' # str | Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values (e.g., US,GB,DE). (optional)
    dissemination_datetime_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by dissemination datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    dissemination_datetime_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by dissemination datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    language = 'language_example' # str | Filter by a single filing language ISO 639-1 code (e.g., en). (optional)
    languages = 'languages_example' # str | Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). (optional)
    lei = 'lei_example' # str | Filter by Company Legal Entity Identifier (LEI). (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    release_datetime_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    release_datetime_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    search = 'search_example' # str | A search term. (optional)
    source = 56 # int |  (optional)
    type = 'type_example' # str | Filter by Filing Type code (e.g., ANNREP). (optional)
    updated_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by last update datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    updated_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by last update datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)

    try:
        # List Filings
        api_response = await api_instance.filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, company=company, company_isin=company_isin, countries=countries, dissemination_datetime_from=dissemination_datetime_from, dissemination_datetime_to=dissemination_datetime_to, language=language, languages=languages, lei=lei, ordering=ordering, page=page, page_size=page_size, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, type=type, updated_date_from=updated_date_from, updated_date_to=updated_date_to)
        print("The response of FilingsApi->filings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **added_to_platform_from** | **datetime**| Filter by date added to platform (inclusive start date, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **added_to_platform_to** | **datetime**| Filter by date added to platform (inclusive end date, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **company** | **int**| Filter by internal Company ID. | [optional] 
 **company_isin** | **str**| Filter by Company ISIN. Case-insensitive. | [optional] 
 **countries** | **str**| Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values (e.g., US,GB,DE). | [optional] 
 **dissemination_datetime_from** | **datetime**| Filter by dissemination datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **dissemination_datetime_to** | **datetime**| Filter by dissemination datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **language** | **str**| Filter by a single filing language ISO 639-1 code (e.g., en). | [optional] 
 **languages** | **str**| Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). | [optional] 
 **lei** | **str**| Filter by Company Legal Entity Identifier (LEI). | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **release_datetime_from** | **datetime**| Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **release_datetime_to** | **datetime**| Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source** | **int**|  | [optional] 
 **type** | **str**| Filter by Filing Type code (e.g., ANNREP). | [optional] 
 **updated_date_from** | **datetime**| Filter by last update datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **updated_date_to** | **datetime**| Filter by last update datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 

### Return type

[**PaginatedFilingSummaryList**](PaginatedFilingSummaryList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of filings. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_markdown_retrieve**
> str filings_markdown_retrieve(filing_id)

Retrieve Filing Markdown

Retrieve the raw processed content of a single filing in Markdown format.

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
    api_instance = financial_reports_generated_client.FilingsApi(api_client)
    filing_id = 56 # int | 

    try:
        # Retrieve Filing Markdown
        api_response = await api_instance.filings_markdown_retrieve(filing_id)
        print("The response of FilingsApi->filings_markdown_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_markdown_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filing_id** | **int**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Not Found. The filing or its processed content does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_retrieve**
> Filing filings_retrieve(id)

Retrieve Filing Details

Retrieve detailed information for a single filing by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.filing import Filing
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
    api_instance = financial_reports_generated_client.FilingsApi(api_client)
    id = 56 # int | A unique integer value identifying this filing.

    try:
        # Retrieve Filing Details
        api_response = await api_instance.filings_retrieve(id)
        print("The response of FilingsApi->filings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filing. | 

### Return type

[**Filing**](Filing.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the filing details. |  -  |
**401** | Authentication credentials were not provided or are invalid. |  -  |
**404** | Filing not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

