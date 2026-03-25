# FilingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history_id** | **int** |  | [readonly] 
**history_date** | **datetime** | The exact date and time the change was recorded. | 
**history_type** | **str** | The type of change: &#39;+&#39; (Created), &#39;~&#39; (Changed), or &#39;-&#39; (Deleted). | 
**changed_by** | **str** |  | [readonly] 
**changes** | **Dict[str, object]** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing_history import FilingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of FilingHistory from a JSON string
filing_history_instance = FilingHistory.from_json(json)
# print the JSON string representation of the object
print(FilingHistory.to_json())

# convert the object into a dict
filing_history_dict = filing_history_instance.to_dict()
# create an instance of FilingHistory from a dict
filing_history_from_dict = FilingHistory.from_dict(filing_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


