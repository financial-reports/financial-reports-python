# financial_reports_generated_client.CompaniesApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_financials_retrieve**](CompaniesApi.md#companies_financials_retrieve) | **GET** /companies/{id}/financials/ | Retrieve Company Financials
[**companies_list**](CompaniesApi.md#companies_list) | **GET** /companies/ | List Companies
[**companies_merges_retrieve**](CompaniesApi.md#companies_merges_retrieve) | **GET** /companies/merges/ | List Company Merges
[**companies_next_annual_report_retrieve**](CompaniesApi.md#companies_next_annual_report_retrieve) | **GET** /companies/{id}/next-annual-report/ | Predict Next Annual Report
[**companies_resolve_create**](CompaniesApi.md#companies_resolve_create) | **POST** /companies/resolve/ | Resolve Companies by Identifier (Batch)
[**companies_retrieve**](CompaniesApi.md#companies_retrieve) | **GET** /companies/{id}/ | Retrieve Company Details


# **companies_financials_retrieve**
> CompaniesFinancialsRetrieve200Response companies_financials_retrieve(id, as_of=as_of, fiscal_period=fiscal_period, fiscal_year=fiscal_year, fiscal_year_from=fiscal_year_from, fiscal_year_to=fiscal_year_to, line_items=line_items, statement_type=statement_type)

Retrieve Company Financials

**Experimental endpoint — the response schema may change without an API version bump.**

Returns standardized financial KPIs for a company as a structured document: a company envelope containing `periods`, each holding its Income Statement, Balance Sheet and Cash Flow `statements`, each holding `line_items`.

When several filings report the same period, the most recently published filing is selected; every contributing filing is listed in the statement's `sources` array. `source_filing` and `sources` are returned only for accounts with source unmasking enabled (`sources_masked` reports which applies). Use `as_of=YYYY-MM-DD` for a point-in-time view.

Use the `depth` and `parent_code` fields on each line item to render the Capital IQ-style statement hierarchy.

**Access Level Required:** Requires **Financial KPIs (Level 3)**.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.companies_financials_retrieve200_response import CompaniesFinancialsRetrieve200Response
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
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    id = 56 # int | A unique integer value identifying this company.
    as_of = 'as_of_example' # str | Point-in-time query (`YYYY-MM-DD`). Returns the financials as they were known on that date — only filings released on or before `as_of` are considered when picking the statement for each period. (optional)
    fiscal_period = 'fiscal_period_example' # str | Filter by fiscal period. (optional)
    fiscal_year = 56 # int | Filter by exact fiscal year (e.g. `2024`). (optional)
    fiscal_year_from = 56 # int | Fiscal year range start (inclusive). (optional)
    fiscal_year_to = 56 # int | Fiscal year range end (inclusive). (optional)
    line_items = 'line_items_example' # str | Comma-separated KPI codes to include (e.g. `revenue,ebitda,net_income_loss`). Omit to return all extracted line items. Statements with none of the requested codes are dropped. Unknown codes return `400` — see `/api/line-item-definitions/`. (optional)
    statement_type = 'statement_type_example' # str | Filter to a single statement type. (optional)

    try:
        # Retrieve Company Financials
        api_response = await api_instance.companies_financials_retrieve(id, as_of=as_of, fiscal_period=fiscal_period, fiscal_year=fiscal_year, fiscal_year_from=fiscal_year_from, fiscal_year_to=fiscal_year_to, line_items=line_items, statement_type=statement_type)
        print("The response of CompaniesApi->companies_financials_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_financials_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 
 **as_of** | **str**| Point-in-time query (&#x60;YYYY-MM-DD&#x60;). Returns the financials as they were known on that date — only filings released on or before &#x60;as_of&#x60; are considered when picking the statement for each period. | [optional] 
 **fiscal_period** | **str**| Filter by fiscal period. | [optional] 
 **fiscal_year** | **int**| Filter by exact fiscal year (e.g. &#x60;2024&#x60;). | [optional] 
 **fiscal_year_from** | **int**| Fiscal year range start (inclusive). | [optional] 
 **fiscal_year_to** | **int**| Fiscal year range end (inclusive). | [optional] 
 **line_items** | **str**| Comma-separated KPI codes to include (e.g. &#x60;revenue,ebitda,net_income_loss&#x60;). Omit to return all extracted line items. Statements with none of the requested codes are dropped. Unknown codes return &#x60;400&#x60; — see &#x60;/api/line-item-definitions/&#x60;. | [optional] 
 **statement_type** | **str**| Filter to a single statement type. | [optional] 

### Return type

[**CompaniesFinancialsRetrieve200Response**](CompaniesFinancialsRetrieve200Response.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Structured company financials document. |  -  |
**400** | Invalid query parameter. |  -  |
**404** | Company not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_list**
> PaginatedCompanyMinimalList companies_list(cik=cik, countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, listing_status=listing_status, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker, view=view)

List Companies

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve a paginated list of companies.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_company_minimal_list import PaginatedCompanyMinimalList
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
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    cik = 'cik_example' # str | Filter by SEC Central Index Key (CIK). Accepts padded or bare (`CIK0000320193`, `0000320193` and `320193` are equivalent). The CIK is assigned by the SEC and survives corporate renames, mergers and ticker changes, so it is the stable key for reconciling a securities universe against our coverage. (optional)
    countries = 'countries_example' # str | Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values. (optional)
    industry = 'industry_example' # str | Filter by ISIC Group code. (optional)
    industry_group = 'industry_group_example' # str | Filter by ISIC Division code. (optional)
    isin = 'isin_example' # str | Filter by Company ISIN. Case-insensitive. (optional)
    lei = 'lei_example' # str | Filter by Company Legal Entity Identifier (LEI). Case-insensitive. (optional)
    listing_status = 'listing_status_example' # str | Filter by exchange-listing state (LISTED, DELISTED, SUSPENDED, UNKNOWN).  * `LISTED` - Listed * `DELISTED` - Delisted * `SUSPENDED` - Suspended * `UNKNOWN` - Unknown (optional)
    on_watchlist = True # bool | Filter by companies on the user's watchlist. Use 'true' to see only watchlist companies, 'false' to exclude them. Omitting the parameter returns all companies. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. Available fields: `id`, `name`, `date_ipo`, `year_founded`, `country_iso__name`, `relevance`. Prefix with '-' for descending order (e.g., `-name`).  When `search` or `ticker` is supplied and `ordering` is omitted, results are relevance-ranked (exact ticker match, then exact name, then name prefix, then fuzzy similarity, with filing volume as the tiebreak). `relevance` is only orderable alongside a `search` or `ticker` term; without one it is ignored. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | Search across company name, LEI, ticker symbol, and associated ISIN codes. Case-insensitive, and accent-insensitive on the company name (`Hermes` matches the accented spelling). Multiple whitespace-separated terms are AND-combined (each term must match at least one of the searched fields). Results are relevance-ranked unless an explicit `ordering` is supplied. (optional)
    sector = 'sector_example' # str | Filter by ISIC Section code. (optional)
    sub_industry = 'sub_industry_example' # str | Filter by ISIC Class code. (optional)
    ticker = 'ticker_example' # str | Filter by stock Ticker symbol. Case-insensitive and separator-insensitive (`BRK.B`, `BRK-B` and `BRK B` are equivalent). Matches the company's primary ticker; when no primary ticker matches, falls back to venue listings, so a secondary share class such as `GOOG` resolves to its issuer. (optional)
    view = 'summary' # str | Controls the level of detail. Omit for a default 'summary' view, or use 'full' to include all details for each company. (optional) (default to 'summary')

    try:
        # List Companies
        api_response = await api_instance.companies_list(cik=cik, countries=countries, industry=industry, industry_group=industry_group, isin=isin, lei=lei, listing_status=listing_status, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker, view=view)
        print("The response of CompaniesApi->companies_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**| Filter by SEC Central Index Key (CIK). Accepts padded or bare (&#x60;CIK0000320193&#x60;, &#x60;0000320193&#x60; and &#x60;320193&#x60; are equivalent). The CIK is assigned by the SEC and survives corporate renames, mergers and ticker changes, so it is the stable key for reconciling a securities universe against our coverage. | [optional] 
 **countries** | **str**| Filter by Company country ISO Alpha-2 code(s). Comma-separated for multiple values. | [optional] 
 **industry** | **str**| Filter by ISIC Group code. | [optional] 
 **industry_group** | **str**| Filter by ISIC Division code. | [optional] 
 **isin** | **str**| Filter by Company ISIN. Case-insensitive. | [optional] 
 **lei** | **str**| Filter by Company Legal Entity Identifier (LEI). Case-insensitive. | [optional] 
 **listing_status** | **str**| Filter by exchange-listing state (LISTED, DELISTED, SUSPENDED, UNKNOWN).  * &#x60;LISTED&#x60; - Listed * &#x60;DELISTED&#x60; - Delisted * &#x60;SUSPENDED&#x60; - Suspended * &#x60;UNKNOWN&#x60; - Unknown | [optional] 
 **on_watchlist** | **bool**| Filter by companies on the user&#39;s watchlist. Use &#39;true&#39; to see only watchlist companies, &#39;false&#39; to exclude them. Omitting the parameter returns all companies. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. Available fields: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;date_ipo&#x60;, &#x60;year_founded&#x60;, &#x60;country_iso__name&#x60;, &#x60;relevance&#x60;. Prefix with &#39;-&#39; for descending order (e.g., &#x60;-name&#x60;).  When &#x60;search&#x60; or &#x60;ticker&#x60; is supplied and &#x60;ordering&#x60; is omitted, results are relevance-ranked (exact ticker match, then exact name, then name prefix, then fuzzy similarity, with filing volume as the tiebreak). &#x60;relevance&#x60; is only orderable alongside a &#x60;search&#x60; or &#x60;ticker&#x60; term; without one it is ignored. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| Search across company name, LEI, ticker symbol, and associated ISIN codes. Case-insensitive, and accent-insensitive on the company name (&#x60;Hermes&#x60; matches the accented spelling). Multiple whitespace-separated terms are AND-combined (each term must match at least one of the searched fields). Results are relevance-ranked unless an explicit &#x60;ordering&#x60; is supplied. | [optional] 
 **sector** | **str**| Filter by ISIC Section code. | [optional] 
 **sub_industry** | **str**| Filter by ISIC Class code. | [optional] 
 **ticker** | **str**| Filter by stock Ticker symbol. Case-insensitive and separator-insensitive (&#x60;BRK.B&#x60;, &#x60;BRK-B&#x60; and &#x60;BRK B&#x60; are equivalent). Matches the company&#39;s primary ticker; when no primary ticker matches, falls back to venue listings, so a secondary share class such as &#x60;GOOG&#x60; resolves to its issuer. | [optional] 
 **view** | **str**| Controls the level of detail. Omit for a default &#39;summary&#39; view, or use &#39;full&#39; to include all details for each company. | [optional] [default to &#39;summary&#39;]

### Return type

[**PaginatedCompanyMinimalList**](PaginatedCompanyMinimalList.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The response structure will be the full Company object if &#x60;view&#x3D;full&#x60; is used. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_merges_retrieve**
> PaginatedCompanyMergeList companies_merges_retrieve()

List Company Merges

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Duplicate-company merges, oldest first.

When two records turn out to describe the same issuer we retire one and keep the other. The retired id disappears from the company list, so a warehouse built by incremental sync would otherwise keep the stale row forever. Poll this feed to reconcile.

**Poll `updated_at_from`, not `merged_at_from`.** Merges can be reversed, and a reversal edits the existing record in place rather than adding a new one — it moves `updated_at` but never `merged_at`. A `reversed_at` on a record you already ingested means the merge no longer holds and `shell_id` is a live company again.

Results are ordered by `merged_at` then `id`, so paging is stable even when a bulk merge writes several records in the same instant. Records are never deleted from this feed.

Covers merges recorded since 2026-06-29. Earlier cleanups predate this log and are not represented; companies removed by hard deletion rather than merge do not appear here either.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_company_merge_list import PaginatedCompanyMergeList
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
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)

    try:
        # List Company Merges
        api_response = await api_instance.companies_merges_retrieve()
        print("The response of CompaniesApi->companies_merges_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_merges_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginatedCompanyMergeList**](PaginatedCompanyMergeList.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_next_annual_report_retrieve**
> NextAnnualReport companies_next_annual_report_retrieve(id)

Predict Next Annual Report

Calculates the expected release window for the next annual report based on historical filing patterns.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.next_annual_report import NextAnnualReport
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
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    id = 56 # int | A unique integer value identifying this company.

    try:
        # Predict Next Annual Report
        api_response = await api_instance.companies_next_annual_report_retrieve(id)
        print("The response of CompaniesApi->companies_next_annual_report_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_next_annual_report_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 

### Return type

[**NextAnnualReport**](NextAnnualReport.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns the predicted date window and confidence score. |  -  |
**404** | Not Found. Not enough historical data to make a confident prediction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_resolve_create**
> CompanyResolveResponse companies_resolve_create(company_resolve_request)

Resolve Companies by Identifier (Batch)

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Reconcile a list of your identifiers against our coverage in one request.

Each row may carry any mix of `isin`, `lei`, `cik`, `ticker` and `name`, plus an optional opaque `ref` echoed back so you can join results to your source rows. Results are returned in input order.

**Resolution order** — ISIN, LEI, CIK, ticker, venue ticker, name. First hit wins, but every identifier you supply is evaluated: if two of them resolve to different companies the row comes back `ambiguous` with `identifier_conflict` and both in `candidates`, rather than us silently picking one.

**A name alone never returns `matched`.** No matter how close the match, a name-only row caps at `ambiguous` and hands you candidates to choose from. Names are not identifiers, and asserting a match on one is how filings end up attached to the wrong issuer.

**Venue-ticker matches are qualified, not asserted.** A ticker that only resolves through our security-listing data is cross-checked against the `name` you supplied. If they disagree you get `ambiguous` + `name_disagrees`; if you supplied no name we cannot corroborate at all, so you get `matched` carrying `security_listing_unverified` — trust that bucket accordingly.

**Billing** — one request is one call against your quota, whatever the row count. Rows we do not cover are not billed differently from rows we do.

Maximum 500 rows per request. Up to 50 rows per request reach the name lookup; beyond that a row carrying only a name returns `not_covered` with `name_tier_skipped`, so split large name-heavy batches.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.company_resolve_request import CompanyResolveRequest
from financial_reports_generated_client.models.company_resolve_response import CompanyResolveResponse
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
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    company_resolve_request = {"rows":[{"ref":"sheet-row-12","ticker":"GOOG","name":"Alphabet Inc."},{"ref":"sheet-row-13","isin":"US5949181045"},{"ref":"sheet-row-14","cik":"0000320193"},{"ref":"sheet-row-15","name":"A Company We Do Not Cover Ltd"}]} # CompanyResolveRequest | 

    try:
        # Resolve Companies by Identifier (Batch)
        api_response = await api_instance.companies_resolve_create(company_resolve_request)
        print("The response of CompaniesApi->companies_resolve_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_resolve_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_resolve_request** | [**CompanyResolveRequest**](CompanyResolveRequest.md)|  | 

### Return type

[**CompanyResolveResponse**](CompanyResolveResponse.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reconciliation complete. Individual rows may still be unmatched. |  -  |
**400** | Malformed batch — too many rows, no rows, or duplicate &#x60;ref&#x60; values. |  -  |
**401** | Unauthorized |  -  |
**403** | Your API plan does not include access to this endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_retrieve**
> Company companies_retrieve(id)

Retrieve Company Details

**Access Level Required:** Requires **Standard Access (Level 1)**.

---
Retrieve detailed information for a single company by its internal ID.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.company import Company
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
    api_instance = financial_reports_generated_client.CompaniesApi(api_client)
    id = 56 # int | A unique integer value identifying this company.

    try:
        # Retrieve Company Details
        api_response = await api_instance.companies_retrieve(id)
        print("The response of CompaniesApi->companies_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 

### Return type

[**Company**](Company.md)

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

