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
[**companies_segments_retrieve**](CompaniesApi.md#companies_segments_retrieve) | **GET** /companies/{id}/segments/ | Retrieve Company Segments


# **companies_financials_retrieve**
> CompaniesFinancialsRetrieve200Response companies_financials_retrieve(id, as_known_at=as_known_at, as_of=as_of, fiscal_period=fiscal_period, fiscal_year=fiscal_year, fiscal_year_from=fiscal_year_from, fiscal_year_to=fiscal_year_to, include=include, line_items=line_items, statement_type=statement_type)

Retrieve Company Financials

**Cost:** 40 credits per request.

---
**Experimental:** the response may change without an API version bump.

Returns a company's standardized income statement, balance sheet and cash flow statement: `periods`, each holding its `statements`, each holding `line_items`. Use `depth` and `parent_code` on each line item to rebuild the statement hierarchy.

**One statement per period.** When several filings report the same fiscal year, period and statement type, one is selected. A filing with the company's own financials beats one without (such as an employee benefit plan's report), the company's reporting currency beats another currency, and a complete statement beats a fragment. Only then does the latest filing win. A selected statement in a currency other than the company's carries `currency_mismatch: true`.

**Currency is never converted.** `currency` is the currency the company presented in. A company that switches currency does not restate earlier years, so compare `currency.code` across periods before aggregating. A line item with its own `currency` comes from a dual-currency filing.

**Values.** `value` and `raw_value` are exact decimal strings: parse them with a decimal type. `raw_value` and `scale` are `null` when a figure was computed rather than read off the page. `confidence` is set only where an independent check re-derived the figure and agreed: `null` means unjudged, not low confidence. `source_page` is reserved and currently `null`.

**Source.** Each statement names its `source_filing`, with `document_url` and `viewer_url` to the document. The full `sources` list, including candidates that were not selected, is only returned to accounts with it enabled; `sources_masked` says which applies.

**Not the bulk dataset.** Comparative statements, restatements, quality flags and stable row ids are only in the S3 `line_items/` delivery. `is_comparative` says whether the selected figures came from a later report's prior-year column.

**Price and history.** One call costs the same however many periods or line items come back. An account limited to a rolling history window gets a `history_window` object; its `max_history_days` is the limit.

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
    as_known_at = 'as_known_at_example' # str | Values as we held them at this time (ISO-8601 datetime, e.g. `2026-10-20T12:00:00Z`; a datetime without an offset is UTC; a bare date `YYYY-MM-DD` means the end of that day in UTC). Each value we corrected or deleted since is served as it was then, a value first written since is left out, and each period's statement is then selected from those values under today's selection rules. Filings not yet released at that time are left out. Combines with `as_of`. History starts at 2026-10-19T17:05:18Z: an earlier time returns `400`; a future time is read as now. Statements are judged and ranked on what we held about them then (company, primary period, currency, filing type, title, release time): a statement moved to another company since is served and flagged `withdrawn_reason`; one moved to this company since is left out. Not reconstructed: period relabels, statements from filings removed since, and the `extraction` block, which is served as it is today. `updated_at` is capped at this time. (optional)
    as_of = 'as_of_example' # str | Filing-date cutoff (`YYYY-MM-DD`): only filings released on or before `as_of` are considered when picking the statement for each period. This is NOT a snapshot of the values we served on that date - figures are corrected in place, and a request with `as_of` returns today's version of each value from those filings. Use each line item's `updated_at` to see when a value last changed, and `as_known_at` for the values as we held them at a past time. (optional)
    fiscal_period = 'fiscal_period_example' # str | Filter by fiscal period. (optional)
    fiscal_year = 56 # int | Filter by exact fiscal year (e.g. `2024`). (optional)
    fiscal_year_from = 56 # int | Fiscal year range start (inclusive). (optional)
    fiscal_year_to = 56 # int | Fiscal year range end (inclusive). (optional)
    include = 'include_example' # str | Comma-separated. `revisions` adds a `revisions` list to every line item: each recorded change to that value, oldest first, with `old_value` -> `new_value` and a reason category. With `as_known_at`, only the changes up to that time. `preliminary` adds `preliminary_results`: the company's own preliminary figures, published before the report and labelled preliminary, never merged into `periods`. `as_reported` adds `as_reported` to a standardised total read straight from the filer's XBRL whose calculation tree ties: the face lines it is made of, as the filer tagged them. Not served with `as_known_at`. (optional)
    line_items = 'line_items_example' # str | Comma-separated KPI codes to include (e.g. `revenue,ebitda,net_income_loss`). Omit to return all extracted line items. Statements with none of the requested codes are dropped. Unknown codes return `400`; see `/line-item-definitions/`. (optional)
    statement_type = 'statement_type_example' # str | Filter to a single statement type. (optional)

    try:
        # Retrieve Company Financials
        api_response = await api_instance.companies_financials_retrieve(id, as_known_at=as_known_at, as_of=as_of, fiscal_period=fiscal_period, fiscal_year=fiscal_year, fiscal_year_from=fiscal_year_from, fiscal_year_to=fiscal_year_to, include=include, line_items=line_items, statement_type=statement_type)
        print("The response of CompaniesApi->companies_financials_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_financials_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 
 **as_known_at** | **str**| Values as we held them at this time (ISO-8601 datetime, e.g. &#x60;2026-10-20T12:00:00Z&#x60;; a datetime without an offset is UTC; a bare date &#x60;YYYY-MM-DD&#x60; means the end of that day in UTC). Each value we corrected or deleted since is served as it was then, a value first written since is left out, and each period&#39;s statement is then selected from those values under today&#39;s selection rules. Filings not yet released at that time are left out. Combines with &#x60;as_of&#x60;. History starts at 2026-10-19T17:05:18Z: an earlier time returns &#x60;400&#x60;; a future time is read as now. Statements are judged and ranked on what we held about them then (company, primary period, currency, filing type, title, release time): a statement moved to another company since is served and flagged &#x60;withdrawn_reason&#x60;; one moved to this company since is left out. Not reconstructed: period relabels, statements from filings removed since, and the &#x60;extraction&#x60; block, which is served as it is today. &#x60;updated_at&#x60; is capped at this time. | [optional] 
 **as_of** | **str**| Filing-date cutoff (&#x60;YYYY-MM-DD&#x60;): only filings released on or before &#x60;as_of&#x60; are considered when picking the statement for each period. This is NOT a snapshot of the values we served on that date - figures are corrected in place, and a request with &#x60;as_of&#x60; returns today&#39;s version of each value from those filings. Use each line item&#39;s &#x60;updated_at&#x60; to see when a value last changed, and &#x60;as_known_at&#x60; for the values as we held them at a past time. | [optional] 
 **fiscal_period** | **str**| Filter by fiscal period. | [optional] 
 **fiscal_year** | **int**| Filter by exact fiscal year (e.g. &#x60;2024&#x60;). | [optional] 
 **fiscal_year_from** | **int**| Fiscal year range start (inclusive). | [optional] 
 **fiscal_year_to** | **int**| Fiscal year range end (inclusive). | [optional] 
 **include** | **str**| Comma-separated. &#x60;revisions&#x60; adds a &#x60;revisions&#x60; list to every line item: each recorded change to that value, oldest first, with &#x60;old_value&#x60; -&gt; &#x60;new_value&#x60; and a reason category. With &#x60;as_known_at&#x60;, only the changes up to that time. &#x60;preliminary&#x60; adds &#x60;preliminary_results&#x60;: the company&#39;s own preliminary figures, published before the report and labelled preliminary, never merged into &#x60;periods&#x60;. &#x60;as_reported&#x60; adds &#x60;as_reported&#x60; to a standardised total read straight from the filer&#39;s XBRL whose calculation tree ties: the face lines it is made of, as the filer tagged them. Not served with &#x60;as_known_at&#x60;. | [optional] 
 **line_items** | **str**| Comma-separated KPI codes to include (e.g. &#x60;revenue,ebitda,net_income_loss&#x60;). Omit to return all extracted line items. Statements with none of the requested codes are dropped. Unknown codes return &#x60;400&#x60;; see &#x60;/line-item-definitions/&#x60;. | [optional] 
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
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_list**
> PaginatedCompanyMinimalList companies_list(cik=cik, countries=countries, date_public_after=date_public_after, date_public_before=date_public_before, date_public_cursor=date_public_cursor, industry=industry, industry_group=industry_group, isin=isin, lei=lei, listing_status=listing_status, oics_class=oics_class, oics_entity_type=oics_entity_type, oics_group=oics_group, oics_industry=oics_industry, oics_sector=oics_sector, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker, view=view)

List Companies

**Cost:** 1 credit per request.

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
    date_public_after = '2013-10-20' # date | Companies last updated on or after this date (YYYY-MM-DD). Granularity is one day (a Europe/Berlin date). For a full sync, seed the catalogue once first and partition that pass (by `countries=`, say), because offset paging stops at 50,000 rows, well short of the full catalogue. The few companies with no `date_public` yet are never returned by a date filter. A company updated while you page is re-dated, so following `next` can miss it; `date_public_cursor` cannot. De-duplicate by `id` and overlap windows by a day. (optional)
    date_public_before = '2013-10-20' # date | Companies last updated on or before this date (YYYY-MM-DD). Granularity is one day (a Europe/Berlin date). For a full sync, seed the catalogue once first and partition that pass (by `countries=`, say), because offset paging stops at 50,000 rows, well short of the full catalogue. The few companies with no `date_public` yet are never returned by a date filter. A company updated while you page is re-dated, so following `next` can miss it; `date_public_cursor` cannot. De-duplicate by `id` and overlap windows by a day. (optional)
    date_public_cursor = 'date_public_cursor_example' # str | Resume a sync after the last company you received: `YYYY-MM-DD,<id>`, its `date_public` and `id`. Returns the companies after it in (`date_public`, `id`) order, up to and including yesterday, so today's changes arrive tomorrow. Requires `ordering=date_public`. Don't follow `next`: request page 1 again with the cursor set to the last company of each page, until a page comes back empty. Start with `<first date>,0`. A company updated mid-walk is re-dated to today and returned by a later walk, never skipped. Companies with no `date_public` are never returned. (optional)
    industry = 'industry_example' # str | Filter by ISIC Group code. (optional)
    industry_group = 'industry_group_example' # str | Filter by ISIC Division code. (optional)
    isin = 'isin_example' # str | Filter by Company ISIN. Case-insensitive. (optional)
    lei = 'lei_example' # str | Filter by Company Legal Entity Identifier (LEI). Case-insensitive. (optional)
    listing_status = 'listing_status_example' # str | Filter by exchange-listing state (LISTED, DELISTED, SUSPENDED, UNKNOWN).  * `LISTED` - Listed * `DELISTED` - Delisted * `SUSPENDED` - Suspended * `UNKNOWN` - Unknown (optional)
    oics_class = 'oics_class_example' # str | Filter by OICS class code (e.g. `TC.SC.SEM.CHP`). Matches the company's primary class, not its secondaries. Public preview, OICS v0.3. (optional)
    oics_entity_type = 'oics_entity_type_example' # str | Filter by OICS entity type: OPERATING, HOLDING, FUND, SPAC_SHELL, FINANCING_VEHICLE or PUBLIC_SECTOR. Public preview, OICS v0.3. (optional)
    oics_group = 'oics_group_example' # str | Filter by OICS industry group code (e.g. `TC.SC`). Matches the company's primary class. Public preview, OICS v0.3. (optional)
    oics_industry = 'oics_industry_example' # str | Filter by OICS industry code (e.g. `TC.SC.SEM`). Matches the company's primary class. Public preview, OICS v0.3. (optional)
    oics_sector = 'oics_sector_example' # str | Filter by OICS sector code (e.g. `TC`). Matches the company's primary class. Public preview, OICS v0.3. (optional)
    on_watchlist = True # bool | Filter by companies on the user's watchlist. Use 'true' to see only watchlist companies, 'false' to exclude them. Omitting the parameter returns all companies. (optional)
    ordering = 'ordering_example' # str | Sort field: `id`, `name`, `date_ipo`, `year_founded`, `country_iso__name`, `date_public` or `relevance`. Prefix with `-` for descending (e.g. `-name`).  `date_public` is the date the record last changed (Europe/Berlin). `-date_public` lists companies without one first; add `date_public_after` to leave those out.  With `search` or `ticker` and no `ordering`, results are ranked by relevance: exact ticker, exact name, name prefix, then fuzzy match, ties broken by filing volume. `relevance` only works with one of those two. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | Search across company name, LEI, ticker symbol, and associated ISIN codes. Case-insensitive, and accent-insensitive on the company name (`Hermes` matches the accented spelling). Multiple whitespace-separated terms are AND-combined (each term must match at least one of the searched fields). Results are relevance-ranked unless an explicit `ordering` is supplied. (optional)
    sector = 'sector_example' # str | Filter by ISIC Section code. (optional)
    sub_industry = 'sub_industry_example' # str | Filter by ISIC Class code. (optional)
    ticker = 'ticker_example' # str | Filter by stock Ticker symbol. Case-insensitive and separator-insensitive (`BRK.B`, `BRK-B` and `BRK B` are equivalent). Matches the company's primary ticker and its venue listings, so a secondary share class such as `GOOG` resolves to its issuer. A ticker held by several companies on different exchanges returns all of them (`count` above 1). To pin the exchange, append its ISO country code: `WDI.DE`, `1316.HK`. ISO codes, not Yahoo suffixes: `.PA`, `.SG`, `.L` and other Yahoo exchange codes are not read as a market. (optional)
    view = 'summary' # str | Controls the level of detail. Omit for a default 'summary' view, or use 'full' to include all details for each company. (optional) (default to 'summary')

    try:
        # List Companies
        api_response = await api_instance.companies_list(cik=cik, countries=countries, date_public_after=date_public_after, date_public_before=date_public_before, date_public_cursor=date_public_cursor, industry=industry, industry_group=industry_group, isin=isin, lei=lei, listing_status=listing_status, oics_class=oics_class, oics_entity_type=oics_entity_type, oics_group=oics_group, oics_industry=oics_industry, oics_sector=oics_sector, on_watchlist=on_watchlist, ordering=ordering, page=page, page_size=page_size, search=search, sector=sector, sub_industry=sub_industry, ticker=ticker, view=view)
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
 **date_public_after** | **date**| Companies last updated on or after this date (YYYY-MM-DD). Granularity is one day (a Europe/Berlin date). For a full sync, seed the catalogue once first and partition that pass (by &#x60;countries&#x3D;&#x60;, say), because offset paging stops at 50,000 rows, well short of the full catalogue. The few companies with no &#x60;date_public&#x60; yet are never returned by a date filter. A company updated while you page is re-dated, so following &#x60;next&#x60; can miss it; &#x60;date_public_cursor&#x60; cannot. De-duplicate by &#x60;id&#x60; and overlap windows by a day. | [optional] 
 **date_public_before** | **date**| Companies last updated on or before this date (YYYY-MM-DD). Granularity is one day (a Europe/Berlin date). For a full sync, seed the catalogue once first and partition that pass (by &#x60;countries&#x3D;&#x60;, say), because offset paging stops at 50,000 rows, well short of the full catalogue. The few companies with no &#x60;date_public&#x60; yet are never returned by a date filter. A company updated while you page is re-dated, so following &#x60;next&#x60; can miss it; &#x60;date_public_cursor&#x60; cannot. De-duplicate by &#x60;id&#x60; and overlap windows by a day. | [optional] 
 **date_public_cursor** | **str**| Resume a sync after the last company you received: &#x60;YYYY-MM-DD,&lt;id&gt;&#x60;, its &#x60;date_public&#x60; and &#x60;id&#x60;. Returns the companies after it in (&#x60;date_public&#x60;, &#x60;id&#x60;) order, up to and including yesterday, so today&#39;s changes arrive tomorrow. Requires &#x60;ordering&#x3D;date_public&#x60;. Don&#39;t follow &#x60;next&#x60;: request page 1 again with the cursor set to the last company of each page, until a page comes back empty. Start with &#x60;&lt;first date&gt;,0&#x60;. A company updated mid-walk is re-dated to today and returned by a later walk, never skipped. Companies with no &#x60;date_public&#x60; are never returned. | [optional] 
 **industry** | **str**| Filter by ISIC Group code. | [optional] 
 **industry_group** | **str**| Filter by ISIC Division code. | [optional] 
 **isin** | **str**| Filter by Company ISIN. Case-insensitive. | [optional] 
 **lei** | **str**| Filter by Company Legal Entity Identifier (LEI). Case-insensitive. | [optional] 
 **listing_status** | **str**| Filter by exchange-listing state (LISTED, DELISTED, SUSPENDED, UNKNOWN).  * &#x60;LISTED&#x60; - Listed * &#x60;DELISTED&#x60; - Delisted * &#x60;SUSPENDED&#x60; - Suspended * &#x60;UNKNOWN&#x60; - Unknown | [optional] 
 **oics_class** | **str**| Filter by OICS class code (e.g. &#x60;TC.SC.SEM.CHP&#x60;). Matches the company&#39;s primary class, not its secondaries. Public preview, OICS v0.3. | [optional] 
 **oics_entity_type** | **str**| Filter by OICS entity type: OPERATING, HOLDING, FUND, SPAC_SHELL, FINANCING_VEHICLE or PUBLIC_SECTOR. Public preview, OICS v0.3. | [optional] 
 **oics_group** | **str**| Filter by OICS industry group code (e.g. &#x60;TC.SC&#x60;). Matches the company&#39;s primary class. Public preview, OICS v0.3. | [optional] 
 **oics_industry** | **str**| Filter by OICS industry code (e.g. &#x60;TC.SC.SEM&#x60;). Matches the company&#39;s primary class. Public preview, OICS v0.3. | [optional] 
 **oics_sector** | **str**| Filter by OICS sector code (e.g. &#x60;TC&#x60;). Matches the company&#39;s primary class. Public preview, OICS v0.3. | [optional] 
 **on_watchlist** | **bool**| Filter by companies on the user&#39;s watchlist. Use &#39;true&#39; to see only watchlist companies, &#39;false&#39; to exclude them. Omitting the parameter returns all companies. | [optional] 
 **ordering** | **str**| Sort field: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;date_ipo&#x60;, &#x60;year_founded&#x60;, &#x60;country_iso__name&#x60;, &#x60;date_public&#x60; or &#x60;relevance&#x60;. Prefix with &#x60;-&#x60; for descending (e.g. &#x60;-name&#x60;).  &#x60;date_public&#x60; is the date the record last changed (Europe/Berlin). &#x60;-date_public&#x60; lists companies without one first; add &#x60;date_public_after&#x60; to leave those out.  With &#x60;search&#x60; or &#x60;ticker&#x60; and no &#x60;ordering&#x60;, results are ranked by relevance: exact ticker, exact name, name prefix, then fuzzy match, ties broken by filing volume. &#x60;relevance&#x60; only works with one of those two. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| Search across company name, LEI, ticker symbol, and associated ISIN codes. Case-insensitive, and accent-insensitive on the company name (&#x60;Hermes&#x60; matches the accented spelling). Multiple whitespace-separated terms are AND-combined (each term must match at least one of the searched fields). Results are relevance-ranked unless an explicit &#x60;ordering&#x60; is supplied. | [optional] 
 **sector** | **str**| Filter by ISIC Section code. | [optional] 
 **sub_industry** | **str**| Filter by ISIC Class code. | [optional] 
 **ticker** | **str**| Filter by stock Ticker symbol. Case-insensitive and separator-insensitive (&#x60;BRK.B&#x60;, &#x60;BRK-B&#x60; and &#x60;BRK B&#x60; are equivalent). Matches the company&#39;s primary ticker and its venue listings, so a secondary share class such as &#x60;GOOG&#x60; resolves to its issuer. A ticker held by several companies on different exchanges returns all of them (&#x60;count&#x60; above 1). To pin the exchange, append its ISO country code: &#x60;WDI.DE&#x60;, &#x60;1316.HK&#x60;. ISO codes, not Yahoo suffixes: &#x60;.PA&#x60;, &#x60;.SG&#x60;, &#x60;.L&#x60; and other Yahoo exchange codes are not read as a market. | [optional] 
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
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_merges_retrieve**
> PaginatedCompanyMergeList companies_merges_retrieve()

List Company Merges

**Cost:** 1 credit per request.

---
Duplicate-company merges, oldest first.

When two records turn out to describe the same issuer we retire one and keep the other. The retired id disappears from the company list, so a warehouse built by incremental sync would otherwise keep the stale row forever. Poll this feed to reconcile.

**Poll `updated_at_from`, not `merged_at_from`.** Merges can be reversed, and a reversal edits the existing record in place rather than adding a new one: it moves `updated_at` but never `merged_at`. A `reversed_at` on a record you already ingested means the merge no longer holds and `shell_id` is a live company again.

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
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_next_annual_report_retrieve**
> NextAnnualReport companies_next_annual_report_retrieve(id)

Predict Next Annual Report

Calculates the expected release window for the next annual report from when the company published its last five annual reports. `confidence` is the share of those reports released within the predicted window (0-100), not a probability.

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
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_resolve_create**
> CompanyResolveResponse companies_resolve_create(company_resolve_request)

Resolve Companies by Identifier (Batch)

**Cost:** 1 credit per request.

---
Match a list of your identifiers to our companies in one request.

Each row can carry any mix of `isin`, `lei`, `cik`, `ticker` and `name`, plus an optional `ref` that is echoed back so you can join results to your rows. Results come back in input order.

**Resolution order:** ISIN, LEI, CIK, ticker, venue ticker, name. The first hit wins, but every identifier you send is checked: if two point to different companies, the row is `ambiguous` with `identifier_conflict` and both in `candidates`.

**A name alone never returns `matched`.** A name-only row is at best `ambiguous`, with candidates to choose from.

**Tickers are checked against your `name`.** Tickers are reused across exchanges, so your name can pick the company that holds the ticker on another venue. A row matched only through a venue ticker is `ambiguous` + `name_disagrees` when the name disagrees, and `matched` + `security_listing_unverified` when you sent no name. If other companies hold the same ticker elsewhere, the row carries `multiple_tickers` and lists them in `candidates`. Add a country code (`WDI.DE`) to pin the exchange.

**Billing:** one request is one call, whatever the row count.

Up to 500 rows per request. Up to 50 rows that need a name lookup get one, within 25 seconds; rows resolved by an identifier don't count. Past either limit, a name-only row returns `not_covered` with `name_tier_skipped`, so split large name-heavy batches.

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
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_retrieve**
> Company companies_retrieve(id)

Retrieve Company Details

**Cost:** 1 credit per request.

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
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_segments_retrieve**
> CompaniesSegmentsRetrieve200Response companies_segments_retrieve(id, axis=axis, metric=metric, period=period)

Retrieve Company Segments

**Cost:** 40 credits per request.

---
**Experimental:** the response may change without an API version bump.

Returns a company's business-segment and geographic figures: revenue, operating profit and assets per segment and period, as the company tagged them in its XBRL filings. Available where companies tag their segment note in XBRL: US, Japan, Korea, Chile and India, and the few European companies that tag theirs.

**As reported.** Names, segment definitions and currencies are the company's own; nothing is mapped to a standard taxonomy or converted. `operating_profit` is the company's segment profit measure, which may differ from its consolidated operating income. Revenue is the measure the company tags for most of its segments, external-customer revenue where it tags that, otherwise segment revenue as it totals it. Geographic areas may overlap (a region and a country within it). `concept` and `member` say which tag each figure came from.

**One filing per period and metric.** When several filings report the same metric for the same period, every segment's figure for it comes from the latest of them, so a restated or recast period replaces the original for that metric. Each value names its `source_filing`. Totals, eliminations and reconciling items are left out, and so are figures that also cut a segment by product or another dimension.

**Values** are exact decimal strings: parse them with a decimal type.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.companies_segments_retrieve200_response import CompaniesSegmentsRetrieve200Response
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
    axis = 'axis_example' # str | Only business segments or only geographic areas. (optional)
    metric = 'metric_example' # str | Only this metric. (optional)
    period = 'period_example' # str | Only periods of this length (`FY`, `9M`, `H`, `Q`). A balance (assets) has no length, so this leaves balances out. (optional)

    try:
        # Retrieve Company Segments
        api_response = await api_instance.companies_segments_retrieve(id, axis=axis, metric=metric, period=period)
        print("The response of CompaniesApi->companies_segments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_segments_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 
 **axis** | **str**| Only business segments or only geographic areas. | [optional] 
 **metric** | **str**| Only this metric. | [optional] 
 **period** | **str**| Only periods of this length (&#x60;FY&#x60;, &#x60;9M&#x60;, &#x60;H&#x60;, &#x60;Q&#x60;). A balance (assets) has no length, so this leaves balances out. | [optional] 

### Return type

[**CompaniesSegmentsRetrieve200Response**](CompaniesSegmentsRetrieve200Response.md)

### Authorization

[CognitoJWT](../README.md#CognitoJWT), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment figures. |  -  |
**400** | Invalid query parameter. |  -  |
**404** | Company not found. |  -  |
**403** | Missing or invalid API key, or the plan does not include this endpoint. |  -  |
**429** | Rate limit, plan quota or spend cap reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

