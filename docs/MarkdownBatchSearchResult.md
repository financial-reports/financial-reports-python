# MarkdownBatchSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_id** | **int** |  | 
**query** | **str** |  | 
**status** | [**MarkdownBatchSearchResultStatusEnum**](MarkdownBatchSearchResultStatusEnum.md) |  | 
**reason** | **str** |  | [optional] 
**total_hits** | **int** |  | [optional] 
**hits** | [**List[MarkdownBatchSearchHit]**](MarkdownBatchSearchHit.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.markdown_batch_search_result import MarkdownBatchSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownBatchSearchResult from a JSON string
markdown_batch_search_result_instance = MarkdownBatchSearchResult.from_json(json)
# print the JSON string representation of the object
print(MarkdownBatchSearchResult.to_json())

# convert the object into a dict
markdown_batch_search_result_dict = markdown_batch_search_result_instance.to_dict()
# create an instance of MarkdownBatchSearchResult from a dict
markdown_batch_search_result_from_dict = MarkdownBatchSearchResult.from_dict(markdown_batch_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


