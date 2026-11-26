# CompaniesSeriesList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The series key: stable across rebuilds and backfills, and company-scoped (the same line in two companies has the same key). | 
**label** | **str** | The line&#39;s label in the company&#39;s latest filing. | [optional] 
**concept** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**scope** | **str** | Whose figure it is. &#x60;consolidated&#x60;: the group&#39;s, or for a company without subsidiaries its own statements (a breakdown line of the group&#39;s statements, by product or segment, is the group&#39;s). &#x60;separate&#x60;: the reporting company alone, its parent-only or individual statements beside the group&#39;s. &#x60;segment&#x60;: a segment&#39;s or region&#39;s figure. &#x60;other&#x60;: another entity&#39;s (a subsidiary, an associate, an elimination column). &#x60;unknown&#x60;: the filing does not say. | [optional] 
**dims** | **Dict[str, str]** | &#x60;{\&quot;axis\&quot;: \&quot;member\&quot;}&#x60; for a breakdown series; absent when there are none. | [optional] 
**length** | **str** | The period length: a fiscal year, half year, nine months, quarter, or a balance. | 
**key_kind** | **str** | How the series was read. | 
**key_stable** | **bool** |  | 
**duplicate_of** | **str** | Present on a copy of another series filed under a second regime (a 20-F twin of a home filing): that series&#39; key. Copies are not listed. | [optional] 
**periods** | **int** | Periods with a value. | 
**first_period_end** | **date** |  | [optional] 
**last_period_end** | **date** |  | [optional] 
**continuity** | [**CompaniesSeriesList200ResponseResultsInnerContinuity**](CompaniesSeriesList200ResponseResultsInnerContinuity.md) |  | [optional] 
**latest** | [**CompaniesSeriesList200ResponseResultsInnerLatest**](CompaniesSeriesList200ResponseResultsInnerLatest.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_series_list200_response_results_inner import CompaniesSeriesList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSeriesList200ResponseResultsInner from a JSON string
companies_series_list200_response_results_inner_instance = CompaniesSeriesList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesSeriesList200ResponseResultsInner.to_json())

# convert the object into a dict
companies_series_list200_response_results_inner_dict = companies_series_list200_response_results_inner_instance.to_dict()
# create an instance of CompaniesSeriesList200ResponseResultsInner from a dict
companies_series_list200_response_results_inner_from_dict = CompaniesSeriesList200ResponseResultsInner.from_dict(companies_series_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


