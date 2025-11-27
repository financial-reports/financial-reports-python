# FilingType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**code** | **str** | Unique code identifying the filing type. | [readonly] 
**name** | **str** | Human-readable name of the filing type. | [readonly] 
**description** | **str** | Detailed description of the filing type. | [readonly] 
**category** | [**FilingCategory**](FilingCategory.md) |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing_type import FilingType

# TODO update the JSON string below
json = "{}"
# create an instance of FilingType from a JSON string
filing_type_instance = FilingType.from_json(json)
# print the JSON string representation of the object
print(FilingType.to_json())

# convert the object into a dict
filing_type_dict = filing_type_instance.to_dict()
# create an instance of FilingType from a dict
filing_type_from_dict = FilingType.from_dict(filing_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


