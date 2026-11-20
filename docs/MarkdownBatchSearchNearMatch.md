# MarkdownBatchSearchNearMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**snippet** | **str** |  | 
**match** | [**MatchEnum**](MatchEnum.md) |  | 
**matched_words** | **List[str]** |  | 
**missing_words** | **List[str]** |  | 

## Example

```python
from financial_reports_generated_client.models.markdown_batch_search_near_match import MarkdownBatchSearchNearMatch

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownBatchSearchNearMatch from a JSON string
markdown_batch_search_near_match_instance = MarkdownBatchSearchNearMatch.from_json(json)
# print the JSON string representation of the object
print(MarkdownBatchSearchNearMatch.to_json())

# convert the object into a dict
markdown_batch_search_near_match_dict = markdown_batch_search_near_match_instance.to_dict()
# create an instance of MarkdownBatchSearchNearMatch from a dict
markdown_batch_search_near_match_from_dict = MarkdownBatchSearchNearMatch.from_dict(markdown_batch_search_near_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


