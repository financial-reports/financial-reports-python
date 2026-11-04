# MarkdownBatchSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MarkdownBatchSearchResult]**](MarkdownBatchSearchResult.md) |  | 
**pairs** | **int** |  | 
**searched** | **int** |  | 
**hit** | **int** |  | 
**no_match** | **int** |  | 
**unavailable** | **int** |  | 
**skipped** | **int** |  | 
**truncated** | **bool** |  | 
**billed_credits** | **int** |  | 

## Example

```python
from financial_reports_generated_client.models.markdown_batch_search_response import MarkdownBatchSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownBatchSearchResponse from a JSON string
markdown_batch_search_response_instance = MarkdownBatchSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MarkdownBatchSearchResponse.to_json())

# convert the object into a dict
markdown_batch_search_response_dict = markdown_batch_search_response_instance.to_dict()
# create an instance of MarkdownBatchSearchResponse from a dict
markdown_batch_search_response_from_dict = MarkdownBatchSearchResponse.from_dict(markdown_batch_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


