# financial_reports_generated_client.FilingsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filings_list**](FilingsApi.md#filings_list) | **GET** /filings/ | List Filings
[**filings_markdown_retrieve**](FilingsApi.md#filings_markdown_retrieve) | **GET** /filings/{id}/markdown/ | Retrieve Filing Markdown
[**filings_retrieve**](FilingsApi.md#filings_retrieve) | **GET** /filings/{id}/ | Retrieve Filing Details


# **filings_list**
> PaginatedFilingSummaryList filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, company=company, company_isin=company_isin, countries=countries, extensions=extensions, file_size_max=file_size_max, file_size_min=file_size_min, language=language, languages=languages, lei=lei, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, sources=sources, type=type, types=types, updated_date_from=updated_date_from, updated_date_to=updated_date_to, view=view)

List Filings

**Access Level Required:** Requires **Level 1** Plan or higher.

---
Retrieve a paginated list of regulatory filings.

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
    extensions = 'extensions_example' # str | Filter by file extension(s). Single (e.g., PDF) or comma-separated (e.g., PDF,XBRL). Case-insensitive. (optional)
    file_size_max = 56 # int | Filter by maximum file size in bytes. (optional)
    file_size_min = 56 # int | Filter by minimum file size in bytes. (optional)
    language = 'language_example' # str | Filter by a single filing language ISO 639-1 code (e.g., en). (optional)
    languages = 'languages_example' # str | Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). (optional)
    lei = 'lei_example' # str | Filter by Company Legal Entity Identifier (LEI). (optional)
    on_watchlist = True # bool | Filter by companies on the user's watchlist. Use 'true' to see only watchlist companies, 'false' to exclude them. Omitting the parameter returns all companies. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. Available fields: `id`, `release_datetime`, `added_to_platform`. Prefix with '-' for descending order (e.g., `-release_datetime`). (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    release_datetime_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    release_datetime_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    search = 'search_example' # str | A search term. (optional)
    source = 3.4 # float | Filter by a single data source ID. (optional)
    sources = 'sources_example' # str | Filter by data source ID(s). Comma-separated for multiple values (e.g., 38,40,51). (optional)
    type = 'type_example' # str | Filter by Filing Type code (e.g., 10-K). (optional)
    types = 'types_example' # str | Filter by multiple Filing Type codes. Comma-separated (e.g., 10-K,10-Q). (optional)
    updated_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by the date a filing was last updated on the platform (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    updated_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by the date a filing was last updated on the platform (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    view = summary # str | Controls the level of detail. Omit for a default 'summary' view, or use 'full' to include all details for each filing. (optional) (default to summary)

    try:
        # List Filings
        api_response = await api_instance.filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, company=company, company_isin=company_isin, countries=countries, extensions=extensions, file_size_max=file_size_max, file_size_min=file_size_min, language=language, languages=languages, lei=lei, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, sources=sources, type=type, types=types, updated_date_from=updated_date_from, updated_date_to=updated_date_to, view=view)
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
 **extensions** | **str**| Filter by file extension(s). Single (e.g., PDF) or comma-separated (e.g., PDF,XBRL). Case-insensitive. | [optional] 
 **file_size_max** | **int**| Filter by maximum file size in bytes. | [optional] 
 **file_size_min** | **int**| Filter by minimum file size in bytes. | [optional] 
 **language** | **str**| Filter by a single filing language ISO 639-1 code (e.g., en). | [optional] 
 **languages** | **str**| Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). | [optional] 
 **lei** | **str**| Filter by Company Legal Entity Identifier (LEI). | [optional] 
 **on_watchlist** | **bool**| Filter by companies on the user&#39;s watchlist. Use &#39;true&#39; to see only watchlist companies, &#39;false&#39; to exclude them. Omitting the parameter returns all companies. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. Available fields: &#x60;id&#x60;, &#x60;release_datetime&#x60;, &#x60;added_to_platform&#x60;. Prefix with &#39;-&#39; for descending order (e.g., &#x60;-release_datetime&#x60;). | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **release_datetime_from** | **datetime**| Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **release_datetime_to** | **datetime**| Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source** | **float**| Filter by a single data source ID. | [optional] 
 **sources** | **str**| Filter by data source ID(s). Comma-separated for multiple values (e.g., 38,40,51). | [optional] 
 **type** | **str**| Filter by Filing Type code (e.g., 10-K). | [optional] 
 **types** | **str**| Filter by multiple Filing Type codes. Comma-separated (e.g., 10-K,10-Q). | [optional] 
 **updated_date_from** | **datetime**| Filter by the date a filing was last updated on the platform (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **updated_date_to** | **datetime**| Filter by the date a filing was last updated on the platform (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **view** | **str**| Controls the level of detail. Omit for a default &#39;summary&#39; view, or use &#39;full&#39; to include all details for each filing. | [optional] [default to summary]

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
**200** | Success. The response structure will be the full Filing object if &#x60;view&#x3D;full&#x60; is used. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_markdown_retrieve**
> filings_markdown_retrieve(id)

Retrieve Filing Markdown

**Access Level Required:** Access to full filing content in Markdown requires a **Level 2** Plan or higher.

---
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
    id = 56 # int | A unique integer value identifying this filing.

    try:
        # Retrieve Filing Markdown
        await api_instance.filings_markdown_retrieve(id)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_markdown_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filing. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Markdown content as plain text. |  -  |
**403** | Forbidden. Your plan does not include access to this endpoint. |  -  |
**404** | Not Found. The filing or its processed content does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_retrieve**
> Filing filings_retrieve(id)

Retrieve Filing Details

**Access Level Required:** Requires **Level 1** Plan or higher.

---
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
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

