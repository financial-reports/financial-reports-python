# financial_reports_generated_client.FilingsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filings_history_retrieve**](FilingsApi.md#filings_history_retrieve) | **GET** /filings/{id}/history/ | Retrieve Filing History (Audit Trail)
[**filings_list**](FilingsApi.md#filings_list) | **GET** /filings/ | List Filings
[**filings_markdown_retrieve**](FilingsApi.md#filings_markdown_retrieve) | **GET** /filings/{id}/markdown/ | Retrieve Filing Markdown
[**filings_retrieve**](FilingsApi.md#filings_retrieve) | **GET** /filings/{id}/ | Retrieve Filing Details


# **filings_history_retrieve**
> PaginatedFilingHistoryList filings_history_retrieve(id)

Retrieve Filing History (Audit Trail)

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve a point-in-time audit trail of material changes made to this filing (e.g., classification or status updates).

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_filing_history_list import PaginatedFilingHistoryList
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
    api_instance = financial_reports_generated_client.FilingsApi(api_client)
    id = 56 # int | A unique integer value identifying this filing.

    try:
        # Retrieve Filing History (Audit Trail)
        api_response = await api_instance.filings_history_retrieve(id)
        print("The response of FilingsApi->filings_history_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_history_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filing. | 

### Return type

[**PaginatedFilingHistoryList**](PaginatedFilingHistoryList.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns a paginated list of historical changes, ordered newest first. |  -  |
**404** | Not Found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_list**
> PaginatedFilingSummaryList filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, categories=categories, category=category, company=company, company_isin=company_isin, countries=countries, extensions=extensions, file_size_max=file_size_max, file_size_min=file_size_min, fiscal_period=fiscal_period, fiscal_year=fiscal_year, ingestion_mode=ingestion_mode, language=language, languages=languages, lei=lei, listing_status=listing_status, max_confidence=max_confidence, min_confidence=min_confidence, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, period_ending_date=period_ending_date, period_ending_date_from=period_ending_date_from, period_ending_date_to=period_ending_date_to, processing_status=processing_status, processing_statuses=processing_statuses, reasoning_contains=reasoning_contains, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, source_filing_type=source_filing_type, sources=sources, type=type, types=types, updated_date_from=updated_date_from, updated_date_to=updated_date_to, view=view)

List Filings

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve a paginated list of regulatory filings.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
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
    api_instance = financial_reports_generated_client.FilingsApi(api_client)
    added_to_platform_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by date added to platform (inclusive start date, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    added_to_platform_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by date added to platform (inclusive end date, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    categories = 'categories_example' # str | Filter by multiple Filing Category IDs. Comma-separated (e.g., 1,3). (optional)
    category = 56 # int | Filter by a single Filing Category ID. (optional)
    company = 56 # int | Filter by internal Company ID. (optional)
    company_isin = 'company_isin_example' # str | Filter by Company ISIN. Case-insensitive. (optional)
    countries = 'countries_example' # str | Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values (e.g., US,GB,DE). (optional)
    extensions = 'extensions_example' # str | Filter by file extension(s). Single (e.g., PDF) or comma-separated (e.g., PDF,XBRL). Case-insensitive. (optional)
    file_size_max = 56 # int | Filter by maximum file size in bytes. (optional)
    file_size_min = 56 # int | Filter by minimum file size in bytes. (optional)
    fiscal_period = 'fiscal_period_example' # str | Filter by fiscal period. Possible values: `FY` (Full Year), `Q1`, `Q2`, `Q3`, `Q4`, `H1` (First Half), `H2` (Second Half). Only populated for filing types: 10-K, 10-K-ESEF, IR, ER. (optional)
    fiscal_year = 56 # int | Filter by fiscal year (e.g., `2024`). Only populated for filing types: 10-K, 10-K-ESEF, IR, ER. (optional)
    ingestion_mode = 'ingestion_mode_example' # str | Filter by ingestion mode. Whether the filing was added to the platform promptly after publication. `REALTIME`: added within the source's normal publication delay (5 to 48 hours after `release_datetime`, depending on the source). `BACKFILLED`: everything else, including historical imports and new filings that reached the platform late, for example after a source outage. Set once when the filing is added and not recalculated afterwards. (optional)
    language = 'language_example' # str | Filter by a single filing language ISO 639-1 code (e.g., en). (optional)
    languages = 'languages_example' # str | Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). (optional)
    lei = 'lei_example' # str | Filter by Company Legal Entity Identifier (LEI). (optional)
    listing_status = 'listing_status_example' # str | Filter by the issuing company's listing status, e.g. `LISTED` for listed firms only. This is the company's status **today**, not at the time of the filing. Exact, case-sensitive match; an unknown value returns `400`. (optional)
    max_confidence = 3.4 # float | Maximum classifier confidence for the assigned filing type (0.0-1.0). (optional)
    min_confidence = 3.4 # float | Minimum classifier confidence for the assigned filing type (0.0-1.0). (optional)
    on_watchlist = True # bool | Filter by companies on the user's watchlist. Use 'true' to see only watchlist companies, 'false' to exclude them. Omitting the parameter returns all companies. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. Available fields: `id`, `release_datetime`, `added_to_platform`, `filing_type_confidence`. Prefix with '-' for descending order (e.g., `-release_datetime`). NOTE: `-filing_type_confidence` lists filings with NO confidence score (NULL, over a quarter of the corpus) FIRST, because descending sorts place NULLs first. To rank scored filings most-confident-first, combine it with `min_confidence=0`, which excludes unscored ones. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    period_ending_date = 'period_ending_date_example' # str | Filter by the exact period ending date (YYYY-MM-DD, e.g., `2024-12-31`). Only populated for filing types: 10-K, 10-K-ESEF, IR, ER. (optional)
    period_ending_date_from = 'period_ending_date_from_example' # str | Filter by period ending date — inclusive start (YYYY-MM-DD). (optional)
    period_ending_date_to = 'period_ending_date_to_example' # str | Filter by period ending date — inclusive end (YYYY-MM-DD). (optional)
    processing_status = 'processing_status_example' # str | Filter by processing status. `COMPLETED` means the document has been processed and is ready to download; the other values are still in, or dropped out of, the processing pipeline. Exact, case-sensitive match; an unknown value returns `400`. (optional)
    processing_statuses = 'processing_statuses_example' # str | Comma-separated processing statuses (e.g. `COMPLETED,FAILED`). Case-insensitive. An unknown value returns `400` naming it. (optional)
    reasoning_contains = 'reasoning_contains_example' # str | Case-insensitive substring match on `filing_type_reasoning`, minimum 3 characters. Requires at least one other filter that actually constrains the query (a date range, company/ISIN/LEI, type, category or source), otherwise returns 400 — the field is unindexed. NOTE the guard checks that a companion filter constrains the query, not HOW MUCH: a deliberately wide date range is accepted and the request is then bounded by the API statement timeout rather than rejected. Narrow the companion filter for a fast answer. CAVEAT: this text is evidence of what the model looked at, NOT a statement of our classification policy; it can cite rules that do not exist. (optional)
    release_datetime_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    release_datetime_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    search = 'search_example' # str | Search across filing title and associated company name. Case-insensitive. Multiple whitespace-separated terms are AND-combined (each term must match either the title or the company name). (optional)
    source = 3.4 # float | Filter by a single data source ID. (optional)
    source_filing_type = 'source_filing_type_example' # str | Filter by the regulator's own form name, exactly as the source publishes it (e.g., 10-Q, 8-K, 6-K for SEC). Case-sensitive exact match; this is open free text that varies by regulator, not a controlled vocabulary. (optional)
    sources = 'sources_example' # str | Filter by data source ID(s). Comma-separated for multiple values (e.g., 38,40,51). (optional)
    type = 'type_example' # str | Filter by a single FinancialFilings Filing Type code (e.g., 10-K). An unrecognised code is rejected with a 400. These are FinancialFilings taxonomy codes, not regulator form names -- see GET /filing-types/. (optional)
    types = 'types_example' # str | Filter by multiple FinancialFilings Filing Type codes. Comma-separated (e.g., 10-K,IR). An unrecognised code is rejected with a 400. These are FinancialFilings taxonomy codes, not regulator form names -- a regulator's own form name belongs on the source_filing_type filter. See GET /filing-types/. (optional)
    updated_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by the date a filing was last updated on the platform (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    updated_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by the date a filing was last updated on the platform (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    view = 'summary' # str | Controls the level of detail. Omit for a default 'summary' view, or use 'full' to include all details for each filing. (optional) (default to 'summary')

    try:
        # List Filings
        api_response = await api_instance.filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, categories=categories, category=category, company=company, company_isin=company_isin, countries=countries, extensions=extensions, file_size_max=file_size_max, file_size_min=file_size_min, fiscal_period=fiscal_period, fiscal_year=fiscal_year, ingestion_mode=ingestion_mode, language=language, languages=languages, lei=lei, listing_status=listing_status, max_confidence=max_confidence, min_confidence=min_confidence, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, period_ending_date=period_ending_date, period_ending_date_from=period_ending_date_from, period_ending_date_to=period_ending_date_to, processing_status=processing_status, processing_statuses=processing_statuses, reasoning_contains=reasoning_contains, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, source_filing_type=source_filing_type, sources=sources, type=type, types=types, updated_date_from=updated_date_from, updated_date_to=updated_date_to, view=view)
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
 **categories** | **str**| Filter by multiple Filing Category IDs. Comma-separated (e.g., 1,3). | [optional] 
 **category** | **int**| Filter by a single Filing Category ID. | [optional] 
 **company** | **int**| Filter by internal Company ID. | [optional] 
 **company_isin** | **str**| Filter by Company ISIN. Case-insensitive. | [optional] 
 **countries** | **str**| Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values (e.g., US,GB,DE). | [optional] 
 **extensions** | **str**| Filter by file extension(s). Single (e.g., PDF) or comma-separated (e.g., PDF,XBRL). Case-insensitive. | [optional] 
 **file_size_max** | **int**| Filter by maximum file size in bytes. | [optional] 
 **file_size_min** | **int**| Filter by minimum file size in bytes. | [optional] 
 **fiscal_period** | **str**| Filter by fiscal period. Possible values: &#x60;FY&#x60; (Full Year), &#x60;Q1&#x60;, &#x60;Q2&#x60;, &#x60;Q3&#x60;, &#x60;Q4&#x60;, &#x60;H1&#x60; (First Half), &#x60;H2&#x60; (Second Half). Only populated for filing types: 10-K, 10-K-ESEF, IR, ER. | [optional] 
 **fiscal_year** | **int**| Filter by fiscal year (e.g., &#x60;2024&#x60;). Only populated for filing types: 10-K, 10-K-ESEF, IR, ER. | [optional] 
 **ingestion_mode** | **str**| Filter by ingestion mode. Whether the filing was added to the platform promptly after publication. &#x60;REALTIME&#x60;: added within the source&#39;s normal publication delay (5 to 48 hours after &#x60;release_datetime&#x60;, depending on the source). &#x60;BACKFILLED&#x60;: everything else, including historical imports and new filings that reached the platform late, for example after a source outage. Set once when the filing is added and not recalculated afterwards. | [optional] 
 **language** | **str**| Filter by a single filing language ISO 639-1 code (e.g., en). | [optional] 
 **languages** | **str**| Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). | [optional] 
 **lei** | **str**| Filter by Company Legal Entity Identifier (LEI). | [optional] 
 **listing_status** | **str**| Filter by the issuing company&#39;s listing status, e.g. &#x60;LISTED&#x60; for listed firms only. This is the company&#39;s status **today**, not at the time of the filing. Exact, case-sensitive match; an unknown value returns &#x60;400&#x60;. | [optional] 
 **max_confidence** | **float**| Maximum classifier confidence for the assigned filing type (0.0-1.0). | [optional] 
 **min_confidence** | **float**| Minimum classifier confidence for the assigned filing type (0.0-1.0). | [optional] 
 **on_watchlist** | **bool**| Filter by companies on the user&#39;s watchlist. Use &#39;true&#39; to see only watchlist companies, &#39;false&#39; to exclude them. Omitting the parameter returns all companies. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. Available fields: &#x60;id&#x60;, &#x60;release_datetime&#x60;, &#x60;added_to_platform&#x60;, &#x60;filing_type_confidence&#x60;. Prefix with &#39;-&#39; for descending order (e.g., &#x60;-release_datetime&#x60;). NOTE: &#x60;-filing_type_confidence&#x60; lists filings with NO confidence score (NULL, over a quarter of the corpus) FIRST, because descending sorts place NULLs first. To rank scored filings most-confident-first, combine it with &#x60;min_confidence&#x3D;0&#x60;, which excludes unscored ones. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **period_ending_date** | **str**| Filter by the exact period ending date (YYYY-MM-DD, e.g., &#x60;2024-12-31&#x60;). Only populated for filing types: 10-K, 10-K-ESEF, IR, ER. | [optional] 
 **period_ending_date_from** | **str**| Filter by period ending date — inclusive start (YYYY-MM-DD). | [optional] 
 **period_ending_date_to** | **str**| Filter by period ending date — inclusive end (YYYY-MM-DD). | [optional] 
 **processing_status** | **str**| Filter by processing status. &#x60;COMPLETED&#x60; means the document has been processed and is ready to download; the other values are still in, or dropped out of, the processing pipeline. Exact, case-sensitive match; an unknown value returns &#x60;400&#x60;. | [optional] 
 **processing_statuses** | **str**| Comma-separated processing statuses (e.g. &#x60;COMPLETED,FAILED&#x60;). Case-insensitive. An unknown value returns &#x60;400&#x60; naming it. | [optional] 
 **reasoning_contains** | **str**| Case-insensitive substring match on &#x60;filing_type_reasoning&#x60;, minimum 3 characters. Requires at least one other filter that actually constrains the query (a date range, company/ISIN/LEI, type, category or source), otherwise returns 400 — the field is unindexed. NOTE the guard checks that a companion filter constrains the query, not HOW MUCH: a deliberately wide date range is accepted and the request is then bounded by the API statement timeout rather than rejected. Narrow the companion filter for a fast answer. CAVEAT: this text is evidence of what the model looked at, NOT a statement of our classification policy; it can cite rules that do not exist. | [optional] 
 **release_datetime_from** | **datetime**| Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **release_datetime_to** | **datetime**| Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **search** | **str**| Search across filing title and associated company name. Case-insensitive. Multiple whitespace-separated terms are AND-combined (each term must match either the title or the company name). | [optional] 
 **source** | **float**| Filter by a single data source ID. | [optional] 
 **source_filing_type** | **str**| Filter by the regulator&#39;s own form name, exactly as the source publishes it (e.g., 10-Q, 8-K, 6-K for SEC). Case-sensitive exact match; this is open free text that varies by regulator, not a controlled vocabulary. | [optional] 
 **sources** | **str**| Filter by data source ID(s). Comma-separated for multiple values (e.g., 38,40,51). | [optional] 
 **type** | **str**| Filter by a single FinancialFilings Filing Type code (e.g., 10-K). An unrecognised code is rejected with a 400. These are FinancialFilings taxonomy codes, not regulator form names -- see GET /filing-types/. | [optional] 
 **types** | **str**| Filter by multiple FinancialFilings Filing Type codes. Comma-separated (e.g., 10-K,IR). An unrecognised code is rejected with a 400. These are FinancialFilings taxonomy codes, not regulator form names -- a regulator&#39;s own form name belongs on the source_filing_type filter. See GET /filing-types/. | [optional] 
 **updated_date_from** | **datetime**| Filter by the date a filing was last updated on the platform (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **updated_date_to** | **datetime**| Filter by the date a filing was last updated on the platform (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **view** | **str**| Controls the level of detail. Omit for a default &#39;summary&#39; view, or use &#39;full&#39; to include all details for each filing. | [optional] [default to &#39;summary&#39;]

### Return type

[**PaginatedFilingSummaryList**](PaginatedFilingSummaryList.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

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
> str filings_markdown_retrieve(id, format=format)

Retrieve Filing Markdown

**Access Level Required:** Requires **Processed Filings (Level 2)** access to view full converted content.

---
Retrieve the raw processed content of a single filing in Markdown format.

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
    api_instance = financial_reports_generated_client.FilingsApi(api_client)
    id = 56 # int | A unique integer value identifying this filing.
    format = 'format_example' # str |  (optional)

    try:
        # Retrieve Filing Markdown
        api_response = await api_instance.filings_markdown_retrieve(id, format=format)
        print("The response of FilingsApi->filings_markdown_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_markdown_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filing. | 
 **format** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/markdown, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Markdown content of the filing. |  -  |
**403** | Forbidden. Your plan does not include access to this endpoint. |  -  |
**404** | Not Found. The filing has no markdown to serve. &#x60;reason&#x60; says why: &#x60;not_processed&#x60; (no processed record yet), &#x60;no_narrative_content&#x60; (the source genuinely carries no narrative text), or &#x60;content_missing&#x60; (the record exists but its content is unavailable). &#x60;retryable&#x60; is &#x60;true&#x60; only while a conversion is scheduled or running; the response then also carries a &#x60;Retry-After&#x60; header (seconds). When &#x60;retryable&#x60; is &#x60;false&#x60;, do not poll: wait for the filing&#39;s &#x60;markdown_url&#x60; to become non-null. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_retrieve**
> Filing filings_retrieve(id)

Retrieve Filing Details

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve detailed information for a single filing by its ID.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
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

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

