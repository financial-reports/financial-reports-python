# FilingsFactsRetrieve200ResponseResultsInnerPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **date** | Absent for a balance (an instant). | [optional] 
**end** | **date** |  | 
**fiscal_label** | **str** | e.g. &#x60;FY2025&#x60;, &#x60;Q3 2025&#x60;, &#x60;9M 2025&#x60;. | [optional] 

## Example

```python
from financial_reports_generated_client.models.filings_facts_retrieve200_response_results_inner_period import FilingsFactsRetrieve200ResponseResultsInnerPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of FilingsFactsRetrieve200ResponseResultsInnerPeriod from a JSON string
filings_facts_retrieve200_response_results_inner_period_instance = FilingsFactsRetrieve200ResponseResultsInnerPeriod.from_json(json)
# print the JSON string representation of the object
print(FilingsFactsRetrieve200ResponseResultsInnerPeriod.to_json())

# convert the object into a dict
filings_facts_retrieve200_response_results_inner_period_dict = filings_facts_retrieve200_response_results_inner_period_instance.to_dict()
# create an instance of FilingsFactsRetrieve200ResponseResultsInnerPeriod from a dict
filings_facts_retrieve200_response_results_inner_period_from_dict = FilingsFactsRetrieve200ResponseResultsInnerPeriod.from_dict(filings_facts_retrieve200_response_results_inner_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


