# financial_reports_generated_client.FilingsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filings_document_retrieve**](FilingsApi.md#filings_document_retrieve) | **GET** /filings/{id}/document/ | Retrieve Filing Document
[**filings_history_retrieve**](FilingsApi.md#filings_history_retrieve) | **GET** /filings/{id}/history/ | Retrieve Filing History (Audit Trail)
[**filings_list**](FilingsApi.md#filings_list) | **GET** /filings/ | List Filings
[**filings_markdown_retrieve**](FilingsApi.md#filings_markdown_retrieve) | **GET** /filings/{id}/markdown/ | Retrieve Filing Markdown
[**filings_markdown_search_retrieve**](FilingsApi.md#filings_markdown_search_retrieve) | **GET** /filings/{id}/markdown/search/ | Search Within a Filing&#39;s Markdown
[**filings_retrieve**](FilingsApi.md#filings_retrieve) | **GET** /filings/{id}/ | Retrieve Filing Details


# **filings_document_retrieve**
> bytes filings_document_retrieve(id, format=format)

Retrieve Filing Document

**Cost:** 1 credit per request.

---
Download the filing's main document as one readable file.

If the filing is a ZIP package (`file_extension` is `ZIP`), for example a submission with exhibits and XBRL files or an ESEF report package, this returns the main document from inside it: the HTML or PDF report, or the ESEF XHTML. HTML comes with its images embedded, so the saved file opens complete. `X-Package-Member` names the file it came from.

Any other filing, and a main document over 50 MB (HTML) or 100 MB (other files), redirects to the stored file (`document`), which always holds the full package. A 200 is charged at the price shown; a redirect is free.

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
        # Retrieve Filing Document
        api_response = await api_instance.filings_document_retrieve(id, format=format)
        print("The response of FilingsApi->filings_document_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_document_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filing. | 
 **format** | **str**|  | [optional] 

### Return type

**bytes**

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The main document, with its own Content-Type (e.g. text/html, application/xhtml+xml, application/pdf). |  -  |
**302** | The filing is not a package, or its main document is over the size cap: redirect to the stored file. |  -  |
**404** | Not Found. The filing has no document, or its package is unreadable or empty. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_history_retrieve**
> PaginatedFilingHistoryList filings_history_retrieve(id)

Retrieve Filing History (Audit Trail)

**Cost:** 1 credit per request.

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
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_list**
> PaginatedFilingSummaryList filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, categories=categories, category=category, company=company, company_isin=company_isin, countries=countries, extensions=extensions, file_size_max=file_size_max, file_size_min=file_size_min, fiscal_period=fiscal_period, fiscal_year=fiscal_year, include_companions=include_companions, include_predecessors=include_predecessors, ingestion_mode=ingestion_mode, language=language, languages=languages, lei=lei, listing_status=listing_status, max_confidence=max_confidence, min_confidence=min_confidence, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, period_ending_date=period_ending_date, period_ending_date_from=period_ending_date_from, period_ending_date_to=period_ending_date_to, primary_annual_report=primary_annual_report, processing_status=processing_status, processing_statuses=processing_statuses, reasoning_contains=reasoning_contains, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, source_filing_type=source_filing_type, sources=sources, type=type, types=types, updated_date_from=updated_date_from, updated_date_to=updated_date_to, view=view, cursor=cursor)

List Filings

**Cost:** 1 credit per request.

---
List filings. All the filters below can be combined.

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
    fiscal_period = 'fiscal_period_example' # str | Fiscal period of the report (`FY` full year, `H1` first half, and so on). Set only on 10-K, 10-K-ESEF, IR and ER filings. (optional)
    fiscal_year = 56 # int | Fiscal year of the report (e.g. `2024`). Set only on annual reports, interim reports and earnings releases (10-K, 10-K-ESEF, IR, ER). (optional)
    include_companions = True # bool | Include companion data files in type and category filters. Companions are small machine-readable XBRL/XML/JSON files stored beside a report for financial extraction, typed like that report. Most are not converted to markdown and show processing_status SKIPPED; the report beside them carries the text. Default false: type, types, category and categories return the reports only. (optional)
    include_predecessors = True # bool | With `company`, also return the filings of the company's predecessors: the issuers it succeeded by reorganisation or redomicile (its `predecessors` of kind reorganization or other on GET /companies/{id}/, followed back through the chain; merged-in targets and spin-off parents are not included), each up to and including the link's effective date (UTC). Each filing's `company` is still the issuer that filed it. Default false. Requires `company`; `lei` and `company_isin` do not follow predecessors. (optional)
    ingestion_mode = 'ingestion_mode_example' # str | Filter by ingestion mode. Whether the filing was added to the platform promptly after publication. `REALTIME`: added within the source's normal publication delay (5 to 48 hours after `release_datetime`, depending on the source). `BACKFILLED`: everything else, including historical imports and new filings that reached the platform late, for example after a source outage. Set once when the filing is added and not recalculated afterwards. (optional)
    language = 'language_example' # str | Filter by a single filing language ISO 639-1 code (e.g., en). (optional)
    languages = 'languages_example' # str | Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). (optional)
    lei = 'lei_example' # str | Filter by Company Legal Entity Identifier (LEI). (optional)
    listing_status = 'listing_status_example' # str | Filter by the issuing company's listing status, e.g. `LISTED` for listed firms only. This is the company's status **today**, not at the time of the filing. Exact, case-sensitive match; an unknown value returns `400`. (optional)
    max_confidence = 3.4 # float | Maximum classifier confidence for the assigned filing type (0.0-1.0). (optional)
    min_confidence = 3.4 # float | Minimum classifier confidence for the assigned filing type (0.0-1.0). (optional)
    on_watchlist = True # bool | `true`: only companies on your watchlist. `false`: exclude them. Omit for all. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. Available fields: `id`, `release_datetime`, `added_to_platform`, `filing_type_confidence`. Prefix with '-' for descending order (e.g., `-release_datetime`). Rows that tie on the chosen field are ordered by `id` in the same direction, so paging through results with `next` does not repeat or skip a filing as long as the matching filings do not change while you page. `-filing_type_confidence` lists filings without a score first; add `min_confidence=0` to leave those out. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    period_ending_date = 'period_ending_date_example' # str | Exact period end date (YYYY-MM-DD, e.g. `2024-12-31`). Set only on 10-K, 10-K-ESEF, IR and ER filings. (optional)
    period_ending_date_from = 'period_ending_date_from_example' # str | Period end date on or after (YYYY-MM-DD). (optional)
    period_ending_date_to = 'period_ending_date_to_example' # str | Period end date on or before (YYYY-MM-DD). (optional)
    primary_annual_report = True # bool | With `true`, return only annual reports (10-K, 10-K-ESEF) with a fiscal year, one per company and fiscal year, picked from the filings your other filters match: the group (consolidated) report over the parent's separate accounts, a report over an AGM notice or an amendment, English over other languages, PDF over HTML over an ESEF package, then the latest release. Combine with `languages` to pick within a language. Requires at least one of: company, company_isin, lei, countries, source, sources, fiscal_year, or a date or period range; otherwise returns 400. (optional)
    processing_status = 'processing_status_example' # str | Filter by processing status. `COMPLETED` means the document has been processed and is ready to download; the other values are still in, or dropped out of, the processing pipeline. Exact, case-sensitive match; an unknown value returns `400`. (optional)
    processing_statuses = 'processing_statuses_example' # str | Comma-separated processing statuses (e.g. `COMPLETED,FAILED`). Case-insensitive. An unknown value returns `400` naming it. (optional)
    reasoning_contains = 'reasoning_contains_example' # str | Case-insensitive match inside `filing_type_reasoning` (3+ characters). Needs at least one other filter (a date range, company, ISIN, LEI, type, category or source), otherwise 400. That filter is not checked for how much it narrows: a very wide one is accepted, and the request may then hit the statement timeout. The reasoning shows what the model looked at; it is not our classification policy and can cite rules that do not exist. (optional)
    release_datetime_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    release_datetime_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    search = 'search_example' # str | Search across filing title and associated company name. Case-insensitive. Multiple whitespace-separated terms are AND-combined (each term must match either the title or the company name). (optional)
    source = 3.4 # float | Filter by a single data source ID. (optional)
    source_filing_type = 'source_filing_type_example' # str | The form name exactly as the source publishes it (e.g. `10-Q`, `8-K`). Case-sensitive exact match on free text that varies by source. (optional)
    sources = 'sources_example' # str | Filter by data source ID(s). Comma-separated for multiple values (e.g., 38,40,51). (optional)
    type = 'type_example' # str | One FinancialFilings filing type code (e.g. `10-K`). Unknown codes return 400. Codes are listed at GET /filing-types/; for the source's own form name, use `source_filing_type`. (optional)
    types = 'types_example' # str | Several filing type codes, comma-separated (e.g. `10-K,IR`). Unknown codes return 400. Codes are listed at GET /filing-types/; for the source's own form names, use `source_filing_type`. (optional)
    updated_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter by the date a filing was last updated on the platform (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    updated_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter by the date a filing was last updated on the platform (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). (optional)
    view = 'summary' # str | `summary` (default) or `full`, which returns every field of each filing. (optional) (default to 'summary')
    cursor = 'cursor_example' # str | Cursor pagination for walking large result sets, with no offset limit. Send an empty `cursor=` for the first page, then follow `next` until it is null (`previous` is always null). Works with every filter. `ordering` can be `release_datetime`, `added_to_platform` or `id`, in one direction (default: newest `release_datetime` first); ties are ordered by `id`, so nothing repeats or is skipped while the data holds still. Adding `page`, or changing `ordering` mid-walk, returns 400 `invalid_cursor`. On a long history a narrow filter can time out (503) near the end: bound the walk with `release_datetime_from` or `added_to_platform_from`. (optional)

    try:
        # List Filings
        api_response = await api_instance.filings_list(added_to_platform_from=added_to_platform_from, added_to_platform_to=added_to_platform_to, categories=categories, category=category, company=company, company_isin=company_isin, countries=countries, extensions=extensions, file_size_max=file_size_max, file_size_min=file_size_min, fiscal_period=fiscal_period, fiscal_year=fiscal_year, include_companions=include_companions, include_predecessors=include_predecessors, ingestion_mode=ingestion_mode, language=language, languages=languages, lei=lei, listing_status=listing_status, max_confidence=max_confidence, min_confidence=min_confidence, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, period_ending_date=period_ending_date, period_ending_date_from=period_ending_date_from, period_ending_date_to=period_ending_date_to, primary_annual_report=primary_annual_report, processing_status=processing_status, processing_statuses=processing_statuses, reasoning_contains=reasoning_contains, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, search=search, source=source, source_filing_type=source_filing_type, sources=sources, type=type, types=types, updated_date_from=updated_date_from, updated_date_to=updated_date_to, view=view, cursor=cursor)
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
 **fiscal_period** | **str**| Fiscal period of the report (&#x60;FY&#x60; full year, &#x60;H1&#x60; first half, and so on). Set only on 10-K, 10-K-ESEF, IR and ER filings. | [optional] 
 **fiscal_year** | **int**| Fiscal year of the report (e.g. &#x60;2024&#x60;). Set only on annual reports, interim reports and earnings releases (10-K, 10-K-ESEF, IR, ER). | [optional] 
 **include_companions** | **bool**| Include companion data files in type and category filters. Companions are small machine-readable XBRL/XML/JSON files stored beside a report for financial extraction, typed like that report. Most are not converted to markdown and show processing_status SKIPPED; the report beside them carries the text. Default false: type, types, category and categories return the reports only. | [optional] 
 **include_predecessors** | **bool**| With &#x60;company&#x60;, also return the filings of the company&#39;s predecessors: the issuers it succeeded by reorganisation or redomicile (its &#x60;predecessors&#x60; of kind reorganization or other on GET /companies/{id}/, followed back through the chain; merged-in targets and spin-off parents are not included), each up to and including the link&#39;s effective date (UTC). Each filing&#39;s &#x60;company&#x60; is still the issuer that filed it. Default false. Requires &#x60;company&#x60;; &#x60;lei&#x60; and &#x60;company_isin&#x60; do not follow predecessors. | [optional] 
 **ingestion_mode** | **str**| Filter by ingestion mode. Whether the filing was added to the platform promptly after publication. &#x60;REALTIME&#x60;: added within the source&#39;s normal publication delay (5 to 48 hours after &#x60;release_datetime&#x60;, depending on the source). &#x60;BACKFILLED&#x60;: everything else, including historical imports and new filings that reached the platform late, for example after a source outage. Set once when the filing is added and not recalculated afterwards. | [optional] 
 **language** | **str**| Filter by a single filing language ISO 639-1 code (e.g., en). | [optional] 
 **languages** | **str**| Filter by filing language ISO 639-1 code(s). Comma-separated for multiple values (e.g., en,de). | [optional] 
 **lei** | **str**| Filter by Company Legal Entity Identifier (LEI). | [optional] 
 **listing_status** | **str**| Filter by the issuing company&#39;s listing status, e.g. &#x60;LISTED&#x60; for listed firms only. This is the company&#39;s status **today**, not at the time of the filing. Exact, case-sensitive match; an unknown value returns &#x60;400&#x60;. | [optional] 
 **max_confidence** | **float**| Maximum classifier confidence for the assigned filing type (0.0-1.0). | [optional] 
 **min_confidence** | **float**| Minimum classifier confidence for the assigned filing type (0.0-1.0). | [optional] 
 **on_watchlist** | **bool**| &#x60;true&#x60;: only companies on your watchlist. &#x60;false&#x60;: exclude them. Omit for all. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. Available fields: &#x60;id&#x60;, &#x60;release_datetime&#x60;, &#x60;added_to_platform&#x60;, &#x60;filing_type_confidence&#x60;. Prefix with &#39;-&#39; for descending order (e.g., &#x60;-release_datetime&#x60;). Rows that tie on the chosen field are ordered by &#x60;id&#x60; in the same direction, so paging through results with &#x60;next&#x60; does not repeat or skip a filing as long as the matching filings do not change while you page. &#x60;-filing_type_confidence&#x60; lists filings without a score first; add &#x60;min_confidence&#x3D;0&#x60; to leave those out. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **period_ending_date** | **str**| Exact period end date (YYYY-MM-DD, e.g. &#x60;2024-12-31&#x60;). Set only on 10-K, 10-K-ESEF, IR and ER filings. | [optional] 
 **period_ending_date_from** | **str**| Period end date on or after (YYYY-MM-DD). | [optional] 
 **period_ending_date_to** | **str**| Period end date on or before (YYYY-MM-DD). | [optional] 
 **primary_annual_report** | **bool**| With &#x60;true&#x60;, return only annual reports (10-K, 10-K-ESEF) with a fiscal year, one per company and fiscal year, picked from the filings your other filters match: the group (consolidated) report over the parent&#39;s separate accounts, a report over an AGM notice or an amendment, English over other languages, PDF over HTML over an ESEF package, then the latest release. Combine with &#x60;languages&#x60; to pick within a language. Requires at least one of: company, company_isin, lei, countries, source, sources, fiscal_year, or a date or period range; otherwise returns 400. | [optional] 
 **processing_status** | **str**| Filter by processing status. &#x60;COMPLETED&#x60; means the document has been processed and is ready to download; the other values are still in, or dropped out of, the processing pipeline. Exact, case-sensitive match; an unknown value returns &#x60;400&#x60;. | [optional] 
 **processing_statuses** | **str**| Comma-separated processing statuses (e.g. &#x60;COMPLETED,FAILED&#x60;). Case-insensitive. An unknown value returns &#x60;400&#x60; naming it. | [optional] 
 **reasoning_contains** | **str**| Case-insensitive match inside &#x60;filing_type_reasoning&#x60; (3+ characters). Needs at least one other filter (a date range, company, ISIN, LEI, type, category or source), otherwise 400. That filter is not checked for how much it narrows: a very wide one is accepted, and the request may then hit the statement timeout. The reasoning shows what the model looked at; it is not our classification policy and can cite rules that do not exist. | [optional] 
 **release_datetime_from** | **datetime**| Filter by release datetime (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **release_datetime_to** | **datetime**| Filter by release datetime (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **search** | **str**| Search across filing title and associated company name. Case-insensitive. Multiple whitespace-separated terms are AND-combined (each term must match either the title or the company name). | [optional] 
 **source** | **float**| Filter by a single data source ID. | [optional] 
 **source_filing_type** | **str**| The form name exactly as the source publishes it (e.g. &#x60;10-Q&#x60;, &#x60;8-K&#x60;). Case-sensitive exact match on free text that varies by source. | [optional] 
 **sources** | **str**| Filter by data source ID(s). Comma-separated for multiple values (e.g., 38,40,51). | [optional] 
 **type** | **str**| One FinancialFilings filing type code (e.g. &#x60;10-K&#x60;). Unknown codes return 400. Codes are listed at GET /filing-types/; for the source&#39;s own form name, use &#x60;source_filing_type&#x60;. | [optional] 
 **types** | **str**| Several filing type codes, comma-separated (e.g. &#x60;10-K,IR&#x60;). Unknown codes return 400. Codes are listed at GET /filing-types/; for the source&#39;s own form names, use &#x60;source_filing_type&#x60;. | [optional] 
 **updated_date_from** | **datetime**| Filter by the date a filing was last updated on the platform (inclusive start, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **updated_date_to** | **datetime**| Filter by the date a filing was last updated on the platform (inclusive end, YYYY-MM-DDTHH:MM:SSZ format). | [optional] 
 **view** | **str**| &#x60;summary&#x60; (default) or &#x60;full&#x60;, which returns every field of each filing. | [optional] [default to &#39;summary&#39;]
 **cursor** | **str**| Cursor pagination for walking large result sets, with no offset limit. Send an empty &#x60;cursor&#x3D;&#x60; for the first page, then follow &#x60;next&#x60; until it is null (&#x60;previous&#x60; is always null). Works with every filter. &#x60;ordering&#x60; can be &#x60;release_datetime&#x60;, &#x60;added_to_platform&#x60; or &#x60;id&#x60;, in one direction (default: newest &#x60;release_datetime&#x60; first); ties are ordered by &#x60;id&#x60;, so nothing repeats or is skipped while the data holds still. Adding &#x60;page&#x60;, or changing &#x60;ordering&#x60; mid-walk, returns 400 &#x60;invalid_cursor&#x60;. On a long history a narrow filter can time out (503) near the end: bound the walk with &#x60;release_datetime_from&#x60; or &#x60;added_to_platform_from&#x60;. | [optional] 

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
**400** | Invalid query parameter, e.g. an unknown &#x60;types&#x60; code or a page beyond the limits. |  -  |
**401** | Unauthorized |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_markdown_retrieve**
> str filings_markdown_retrieve(id, format=format, limit=limit, offset=offset)

Retrieve Filing Markdown

**Cost:** 6 credits per request (12 for premium filing types).

---
Retrieve the raw processed content of a single filing in Markdown format.

**Large filings.** An annual report can run to several hundred thousand tokens. Every response carries `X-Total-Chars`, the full document's length in characters. Pass `offset` and/or `limit` (characters) to read one window instead of the whole document; while characters remain after the window, the response also carries `X-Next-Offset`. To find the part you need first, use `GET /filings/{id}/markdown/search/?q=`. Each call, whole or windowed, is billed as one Markdown request. Through the MCP server, which pages large filings in chunks, a filing's Markdown is billed once per day.

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
    limit = 56 # int | Characters to return, 1-200,000 (default 200,000 when offset is given). (optional)
    offset = 56 # int | Character offset to start reading at (default 0). Passing offset or limit returns a window instead of the whole document. (optional)

    try:
        # Retrieve Filing Markdown
        api_response = await api_instance.filings_markdown_retrieve(id, format=format, limit=limit, offset=offset)
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
 **limit** | **int**| Characters to return, 1-200,000 (default 200,000 when offset is given). | [optional] 
 **offset** | **int**| Character offset to start reading at (default 0). Passing offset or limit returns a window instead of the whole document. | [optional] 

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
**200** | Markdown content of the filing. Filings converted from PDF since 2026-10-22 carry &#x60;&lt;!-- page N --&gt;&#x60; on its own line before each page (N is the PDF page number), and HTML filings that mark their page breaks carry one per marked page, so a quote sits on the page of the last marker above it. Older conversions have none. |  -  |
**403** | Forbidden. Your plan does not include access to this endpoint. |  -  |
**404** | Not Found. The filing has no markdown to serve. &#x60;reason&#x60; says why: &#x60;not_processed&#x60; (no processed record yet), &#x60;no_narrative_content&#x60; (the source genuinely carries no narrative text), or &#x60;content_missing&#x60; (the record exists but its content is unavailable). &#x60;retryable&#x60; is &#x60;true&#x60; only while a conversion is scheduled or running; the response then also carries a &#x60;Retry-After&#x60; header (seconds). When &#x60;retryable&#x60; is &#x60;false&#x60;, do not poll: wait for the filing&#39;s &#x60;markdown_url&#x60; to become non-null. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_markdown_search_retrieve**
> filings_markdown_search_retrieve(id, q, max_hits=max_hits)

Search Within a Filing's Markdown

**Cost:** 6 credits per request (12 for premium filing types).

---
Find text inside one filing's processed Markdown without downloading all of it. Case-insensitive substring match; hits come back in document order, each with ~440 characters of context and its character `offset`. Pass that offset (minus a margin) to `GET /filings/{id}/markdown/?offset=&limit=` to read the surrounding section. `total_hits` counts every match, so you can tell when `max_hits` was spent on the table of contents. Billed as one Markdown request.

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
    q = 'q_example' # str | Text to find (1-200 characters).
    max_hits = 56 # int | Hits to return, 1-50 (default 10). (optional)

    try:
        # Search Within a Filing's Markdown
        await api_instance.filings_markdown_search_retrieve(id, q, max_hits=max_hits)
    except Exception as e:
        print("Exception when calling FilingsApi->filings_markdown_search_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this filing. | 
 **q** | **str**| Text to find (1-200 characters). | 
 **max_hits** | **int**| Hits to return, 1-50 (default 10). | [optional] 

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
**200** | Matches with their character offsets. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filings_retrieve**
> Filing filings_retrieve(id)

Retrieve Filing Details

**Cost:** 1 credit per request.

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
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

