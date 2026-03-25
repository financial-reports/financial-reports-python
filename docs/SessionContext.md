# SessionContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | 
**company_name** | **str** |  | 
**filing_ids** | **List[int]** |  | 

## Example

```python
from financial_reports_generated_client.models.session_context import SessionContext

# TODO update the JSON string below
json = "{}"
# create an instance of SessionContext from a JSON string
session_context_instance = SessionContext.from_json(json)
# print the JSON string representation of the object
print(SessionContext.to_json())

# convert the object into a dict
session_context_dict = session_context_instance.to_dict()
# create an instance of SessionContext from a dict
session_context_from_dict = SessionContext.from_dict(session_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


