# FilingSearchMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[FilingSearchHit]**](FilingSearchHit.md) |  | 
**query** | **str** |  | 
**total_hits** | **int** |  | 
**truncated** | **bool** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.filing_search_match import FilingSearchMatch

# TODO update the JSON string below
json = "{}"
# create an instance of FilingSearchMatch from a JSON string
filing_search_match_instance = FilingSearchMatch.from_json(json)
# print the JSON string representation of the object
print(FilingSearchMatch.to_json())

# convert the object into a dict
filing_search_match_dict = filing_search_match_instance.to_dict()
# create an instance of FilingSearchMatch from a dict
filing_search_match_from_dict = FilingSearchMatch.from_dict(filing_search_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


