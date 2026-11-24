# FilingsFactsRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Facts across all pages: what paging through costs, up front. | 
**count_is_estimate** | **bool** | Always false here: &#x60;count&#x60; is exact. | [optional] 
**next** | **str** |  | 
**previous** | **str** |  | 
**results** | [**List[FilingsFactsRetrieve200ResponseResultsInner]**](FilingsFactsRetrieve200ResponseResultsInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.filings_facts_retrieve200_response import FilingsFactsRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FilingsFactsRetrieve200Response from a JSON string
filings_facts_retrieve200_response_instance = FilingsFactsRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(FilingsFactsRetrieve200Response.to_json())

# convert the object into a dict
filings_facts_retrieve200_response_dict = filings_facts_retrieve200_response_instance.to_dict()
# create an instance of FilingsFactsRetrieve200Response from a dict
filings_facts_retrieve200_response_from_dict = FilingsFactsRetrieve200Response.from_dict(filings_facts_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


