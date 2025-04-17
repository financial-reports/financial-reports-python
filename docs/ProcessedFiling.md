# ProcessedFiling

Serializer for the ProcessedFiling model, providing access to the processed content (e.g., markdown).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**filing_id** | **int** | ID of the original Filing. | [readonly] 
**content_markdown** | **str** | The processed filing content in Markdown format. | [readonly] 
**content_json** | **object** | Optional structured JSON representation of the content. | [readonly] 
**processor** | **str** | Identifier for the tool/method used to process the filing. | [readonly] 
**added_at** | **datetime** | Timestamp when the processed content was added. | [readonly] 
**updated_at** | **datetime** | Timestamp when the processed content was last updated. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.processed_filing import ProcessedFiling

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedFiling from a JSON string
processed_filing_instance = ProcessedFiling.from_json(json)
# print the JSON string representation of the object
print(ProcessedFiling.to_json())

# convert the object into a dict
processed_filing_dict = processed_filing_instance.to_dict()
# create an instance of ProcessedFiling from a dict
processed_filing_from_dict = ProcessedFiling.from_dict(processed_filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


