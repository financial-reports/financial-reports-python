# ISICClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISIC Class code. | [readonly] 
**name** | **str** | ISIC Class name. | [readonly] 
**industry** | [**ISICGroup**](ISICGroup.md) | Parent ISIC Group. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.isic_class import ISICClass

# TODO update the JSON string below
json = "{}"
# create an instance of ISICClass from a JSON string
isic_class_instance = ISICClass.from_json(json)
# print the JSON string representation of the object
print(ISICClass.to_json())

# convert the object into a dict
isic_class_dict = isic_class_instance.to_dict()
# create an instance of ISICClass from a dict
isic_class_from_dict = ISICClass.from_dict(isic_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


