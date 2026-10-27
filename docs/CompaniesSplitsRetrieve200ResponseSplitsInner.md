# CompaniesSplitsRetrieve200ResponseSplitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Stable id of the split event. | 
**split_type** | **str** | &#x60;split&#x60; (incl. face-value splits), &#x60;reverse&#x60; (share consolidation) or &#x60;bonus&#x60; (bonus / capitalisation issue, stock dividend). | 
**ratio_new** | **decimal.Decimal** | Shares held after the split for every &#x60;ratio_old&#x60; shares held before. | 
**ratio_old** | **decimal.Decimal** |  | 
**factor** | **decimal.Decimal** | &#x60;ratio_new / ratio_old&#x60;: 4 for a 4-for-1 split, 0.1 for a 1-for-10 reverse split, 2 for a 1:1 bonus issue. Divide per-share values before the ex-date by it to restate them on the post-split basis. | 
**status** | **str** | &#x60;announced&#x60; until the split takes effect, then &#x60;effective&#x60;; &#x60;cancelled&#x60; when the company withdrew it. | 
**announcement_date** | **date** |  | 
**record_date** | **date** |  | 
**ex_date** | **date** | First trading day on the post-split basis. | 
**effective_date** | **date** | Date the split takes effect, where the company states that rather than an ex-date. | 
**announcement_filing_id** | **int** | The filing that announced the split, when we hold it. | 
**updated_at** | **datetime** |  | 

## Example

```python
from financial_reports_generated_client.models.companies_splits_retrieve200_response_splits_inner import CompaniesSplitsRetrieve200ResponseSplitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSplitsRetrieve200ResponseSplitsInner from a JSON string
companies_splits_retrieve200_response_splits_inner_instance = CompaniesSplitsRetrieve200ResponseSplitsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesSplitsRetrieve200ResponseSplitsInner.to_json())

# convert the object into a dict
companies_splits_retrieve200_response_splits_inner_dict = companies_splits_retrieve200_response_splits_inner_instance.to_dict()
# create an instance of CompaniesSplitsRetrieve200ResponseSplitsInner from a dict
companies_splits_retrieve200_response_splits_inner_from_dict = CompaniesSplitsRetrieve200ResponseSplitsInner.from_dict(companies_splits_retrieve200_response_splits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


