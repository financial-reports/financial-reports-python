# financial_reports_generated_client.InsidersHoldingsApi

All URIs are relative to *https://api.financialreports.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insider_transactions_list**](InsidersHoldingsApi.md#insider_transactions_list) | **GET** /insider-transactions/ | List Insider Transactions
[**major_holdings_list**](InsidersHoldingsApi.md#major_holdings_list) | **GET** /major-holdings/ | List Major Holdings


# **insider_transactions_list**
> PaginatedInsiderTransactionList insider_transactions_list(company=company, company_isin=company_isin, countries=countries, filing=filing, insider_ref=insider_ref, lei=lei, nature=nature, ordering=ordering, page=page, page_size=page_size, regime=regime, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, row_kind=row_kind, transaction_date_from=transaction_date_from, transaction_date_to=transaction_date_to)

List Insider Transactions

**Cost:** 40 credits per request.

---
Insider dealings as rows you can query across filings: one row per line of an insider notice. US: every line of Forms 3, 4 and 5 (transactions and holdings, derivative or not) and the proposed sale of each Form 144.

Filter by issuer (`company`, `company_isin`, `lei`, `countries`), by `nature` (`buy`, `sell`, ...), `row_kind`, `regime`, `insider_ref`, the transaction date or the publication date. Example: all Carvana insider sales in 2026 are `?company=30038&nature=sell&transaction_date_from=2026-01-01`.

Each row names `filing_id` and `release_datetime`: GET /filings/{filing_id}/ is the notice it was read from. The issuer is the filing's company. An amendment's rows (`is_amendment`) sit next to the original's, not in place of them, so drop one of the two before adding up. Coverage: US filings published from the endpoint's launch; history is being added. Values are as reported; fields a market does not report are empty.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_insider_transaction_list import PaginatedInsiderTransactionList
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
    api_instance = financial_reports_generated_client.InsidersHoldingsApi(api_client)
    company = 3.4 # float | Issuer company ID. (optional)
    company_isin = 'company_isin_example' # str | Issuer ISIN (any of the company's ISINs). Case-insensitive. (optional)
    countries = 'countries_example' # str | Issuer country ISO alpha-2 code(s), comma-separated (e.g. US,GB). (optional)
    filing = 3.4 # float | Rows of one filing. (optional)
    insider_ref = 'insider_ref_example' # str | Source-native insider id, e.g. `CIK0001210412`. (optional)
    lei = 'lei_example' # str | Issuer LEI. (optional)
    nature = 'nature_example' # str | Nature(s), comma-separated (e.g. buy,sell). (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    regime = 'regime_example' # str | Regime code(s), comma-separated (e.g. US_SEC16,US_RULE144). (optional)
    release_datetime_from = '2013-10-20T19:20:30+01:00' # datetime | Filing published at or after (YYYY-MM-DDTHH:MM:SSZ). (optional)
    release_datetime_to = '2013-10-20T19:20:30+01:00' # datetime | Filing published at or before (YYYY-MM-DDTHH:MM:SSZ). (optional)
    row_kind = 'row_kind_example' # str | Row kind(s), comma-separated: transaction, holding, planned_sale. (optional)
    transaction_date_from = '2013-10-20' # date | Transaction on or after (YYYY-MM-DD). (optional)
    transaction_date_to = '2013-10-20' # date | Transaction on or before (YYYY-MM-DD). (optional)

    try:
        # List Insider Transactions
        api_response = await api_instance.insider_transactions_list(company=company, company_isin=company_isin, countries=countries, filing=filing, insider_ref=insider_ref, lei=lei, nature=nature, ordering=ordering, page=page, page_size=page_size, regime=regime, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to, row_kind=row_kind, transaction_date_from=transaction_date_from, transaction_date_to=transaction_date_to)
        print("The response of InsidersHoldingsApi->insider_transactions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsidersHoldingsApi->insider_transactions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **float**| Issuer company ID. | [optional] 
 **company_isin** | **str**| Issuer ISIN (any of the company&#39;s ISINs). Case-insensitive. | [optional] 
 **countries** | **str**| Issuer country ISO alpha-2 code(s), comma-separated (e.g. US,GB). | [optional] 
 **filing** | **float**| Rows of one filing. | [optional] 
 **insider_ref** | **str**| Source-native insider id, e.g. &#x60;CIK0001210412&#x60;. | [optional] 
 **lei** | **str**| Issuer LEI. | [optional] 
 **nature** | **str**| Nature(s), comma-separated (e.g. buy,sell). | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **regime** | **str**| Regime code(s), comma-separated (e.g. US_SEC16,US_RULE144). | [optional] 
 **release_datetime_from** | **datetime**| Filing published at or after (YYYY-MM-DDTHH:MM:SSZ). | [optional] 
 **release_datetime_to** | **datetime**| Filing published at or before (YYYY-MM-DDTHH:MM:SSZ). | [optional] 
 **row_kind** | **str**| Row kind(s), comma-separated: transaction, holding, planned_sale. | [optional] 
 **transaction_date_from** | **date**| Transaction on or after (YYYY-MM-DD). | [optional] 
 **transaction_date_to** | **date**| Transaction on or before (YYYY-MM-DD). | [optional] 

### Return type

[**PaginatedInsiderTransactionList**](PaginatedInsiderTransactionList.md)

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

# **major_holdings_list**
> PaginatedMajorHoldingList major_holdings_list(company=company, company_isin=company_isin, countries=countries, event_date_from=event_date_from, event_date_to=event_date_to, filing=filing, holder_ref=holder_ref, lei=lei, ordering=ordering, page=page, page_size=page_size, regime=regime, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to)

List Major Holdings

**Cost:** 40 credits per request.

---
Major-shareholding notices as rows: one row per reporting person, with voting and dispositive power, the aggregate owned and the percent of the class. The persons on one notice often count the same shares (a fund and its manager, the members of a group), so do not add one notice's rows up. US: Schedule 13D and 13G and their amendments, in the structured form the SEC has required since 18 December 2024.

Filter by issuer (`company`, `company_isin`, `lei`, `countries`), `regime`, `holder_ref`, the event date or the publication date.

Each row names `filing_id` and `release_datetime`: GET /filings/{filing_id}/ is the notice it was read from. The issuer is the filing's company. An amendment's rows (`is_amendment`) sit next to the original's, not in place of them, so drop one of the two before adding up. Coverage: US filings published from the endpoint's launch; history is being added. Values are as reported; fields a market does not report are empty.

### Example

* Bearer (JWT) Authentication (CognitoJWT):
* Api Key Authentication (ApiKeyAuth):

```python
import financial_reports_generated_client
from financial_reports_generated_client.models.paginated_major_holding_list import PaginatedMajorHoldingList
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
    api_instance = financial_reports_generated_client.InsidersHoldingsApi(api_client)
    company = 3.4 # float | Issuer company ID. (optional)
    company_isin = 'company_isin_example' # str | Issuer ISIN (any of the company's ISINs). Case-insensitive. (optional)
    countries = 'countries_example' # str | Issuer country ISO alpha-2 code(s), comma-separated (e.g. US,GB). (optional)
    event_date_from = '2013-10-20' # date | Event on or after (YYYY-MM-DD). (optional)
    event_date_to = '2013-10-20' # date | Event on or before (YYYY-MM-DD). (optional)
    filing = 3.4 # float | Rows of one filing. (optional)
    holder_ref = 'holder_ref_example' # str | Source-native holder id, e.g. `CIK0001017608`. (optional)
    lei = 'lei_example' # str | Issuer LEI. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    regime = 'regime_example' # str | Regime code(s), comma-separated (e.g. US_SEC16,US_RULE144). (optional)
    release_datetime_from = '2013-10-20T19:20:30+01:00' # datetime | Filing published at or after (YYYY-MM-DDTHH:MM:SSZ). (optional)
    release_datetime_to = '2013-10-20T19:20:30+01:00' # datetime | Filing published at or before (YYYY-MM-DDTHH:MM:SSZ). (optional)

    try:
        # List Major Holdings
        api_response = await api_instance.major_holdings_list(company=company, company_isin=company_isin, countries=countries, event_date_from=event_date_from, event_date_to=event_date_to, filing=filing, holder_ref=holder_ref, lei=lei, ordering=ordering, page=page, page_size=page_size, regime=regime, release_datetime_from=release_datetime_from, release_datetime_to=release_datetime_to)
        print("The response of InsidersHoldingsApi->major_holdings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsidersHoldingsApi->major_holdings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **float**| Issuer company ID. | [optional] 
 **company_isin** | **str**| Issuer ISIN (any of the company&#39;s ISINs). Case-insensitive. | [optional] 
 **countries** | **str**| Issuer country ISO alpha-2 code(s), comma-separated (e.g. US,GB). | [optional] 
 **event_date_from** | **date**| Event on or after (YYYY-MM-DD). | [optional] 
 **event_date_to** | **date**| Event on or before (YYYY-MM-DD). | [optional] 
 **filing** | **float**| Rows of one filing. | [optional] 
 **holder_ref** | **str**| Source-native holder id, e.g. &#x60;CIK0001017608&#x60;. | [optional] 
 **lei** | **str**| Issuer LEI. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **regime** | **str**| Regime code(s), comma-separated (e.g. US_SEC16,US_RULE144). | [optional] 
 **release_datetime_from** | **datetime**| Filing published at or after (YYYY-MM-DDTHH:MM:SSZ). | [optional] 
 **release_datetime_to** | **datetime**| Filing published at or before (YYYY-MM-DDTHH:MM:SSZ). | [optional] 

### Return type

[**PaginatedMajorHoldingList**](PaginatedMajorHoldingList.md)

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

