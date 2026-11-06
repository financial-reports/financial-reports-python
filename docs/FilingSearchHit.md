# FilingSearchHit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**snippet** | **str** |  | 

## Example

```python
from financial_reports_generated_client.models.filing_search_hit import FilingSearchHit

# TODO update the JSON string below
json = "{}"
# create an instance of FilingSearchHit from a JSON string
filing_search_hit_instance = FilingSearchHit.from_json(json)
# print the JSON string representation of the object
print(FilingSearchHit.to_json())

# convert the object into a dict
filing_search_hit_dict = filing_search_hit_instance.to_dict()
# create an instance of FilingSearchHit from a dict
filing_search_hit_from_dict = FilingSearchHit.from_dict(filing_search_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


