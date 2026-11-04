# MarkdownBatchSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **List[str]** | 1-3 non-empty strings, each at most 200 characters. | 
**filing_ids** | **List[int]** | 1-50 filing ids. | 
**max_hits_per_filing** | **int** | Snippets returned per (filing, query) pair, 1-10 (default 3). | [optional] [default to 3]

## Example

```python
from financial_reports_generated_client.models.markdown_batch_search_request import MarkdownBatchSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownBatchSearchRequest from a JSON string
markdown_batch_search_request_instance = MarkdownBatchSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MarkdownBatchSearchRequest.to_json())

# convert the object into a dict
markdown_batch_search_request_dict = markdown_batch_search_request_instance.to_dict()
# create an instance of MarkdownBatchSearchRequest from a dict
markdown_batch_search_request_from_dict = MarkdownBatchSearchRequest.from_dict(markdown_batch_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


