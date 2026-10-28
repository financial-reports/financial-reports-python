# CompaniesDividendsRetrieve200ResponseDividendsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Stable id of this dividend. | 
**status** | **str** | &#x60;upcoming&#x60; while its ex, record or payment date is today or later (or, with no date announced yet, for a year after it was announced); then &#x60;paid&#x60;. &#x60;cancelled&#x60; when the company withdrew it. | 
**stage** | **str** | &#x60;proposed&#x60; while it awaits shareholder approval. | 
**kind** | **str** |  | 
**is_interest_on_equity** | **bool** | Brazil: interest on equity (juros sobre capital próprio). | [optional] 
**share_class** | **str** | &#x60;common&#x60;, &#x60;preferred&#x60;, or the class as the company names it. | 
**fiscal_period** | **str** |  | [optional] 
**instalment** | **str** | &#x60;1/2&#x60;, &#x60;2/2&#x60; ... when the dividend is paid in instalments, each its own entry. | [optional] 
**amount** | **decimal.Decimal** | Gross amount per share, as declared. Not adjusted for later splits: see &#x60;split_adjusted&#x60;. | 
**currency** | **str** |  | 
**announcement_date** | **date** |  | [optional] 
**agm_date** | **date** |  | [optional] 
**last_cum_date** | **date** |  | [optional] 
**ex_date** | **date** |  | 
**record_date** | **date** |  | 
**payment_date** | **date** |  | 
**ex_date_derived** | **bool** |  | [optional] 
**derived_dates** | **Dict[str, str]** | Dates computed from a market or company rule instead of stated in a notice, each with its rule. | 
**date_changes** | [**List[CompaniesDividendsRetrieve200ResponseDividendsInnerDateChangesInner]**](CompaniesDividendsRetrieve200ResponseDividendsInnerDateChangesInner.md) | Dates (and an amount restated after a split) a later notice changed, with the filing that changed them. | [optional] 
**announcement_filing** | **object** |  | 
**source_filing_ids** | **List[int]** |  | [optional] 
**evidence_quote** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**split_adjusted** | [**CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted**](CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_dividends_retrieve200_response_dividends_inner import CompaniesDividendsRetrieve200ResponseDividendsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesDividendsRetrieve200ResponseDividendsInner from a JSON string
companies_dividends_retrieve200_response_dividends_inner_instance = CompaniesDividendsRetrieve200ResponseDividendsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesDividendsRetrieve200ResponseDividendsInner.to_json())

# convert the object into a dict
companies_dividends_retrieve200_response_dividends_inner_dict = companies_dividends_retrieve200_response_dividends_inner_instance.to_dict()
# create an instance of CompaniesDividendsRetrieve200ResponseDividendsInner from a dict
companies_dividends_retrieve200_response_dividends_inner_from_dict = CompaniesDividendsRetrieve200ResponseDividendsInner.from_dict(companies_dividends_retrieve200_response_dividends_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


