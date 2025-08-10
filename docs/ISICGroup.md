# ISICGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISIC Group code. | [readonly] 
**name** | **str** | ISIC Group name. | [readonly] 
**industry_group** | [**ISICDivision**](ISICDivision.md) | Parent ISIC Division. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.isic_group import ISICGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ISICGroup from a JSON string
isic_group_instance = ISICGroup.from_json(json)
# print the JSON string representation of the object
print(ISICGroup.to_json())

# convert the object into a dict
isic_group_dict = isic_group_instance.to_dict()
# create an instance of ISICGroup from a dict
isic_group_from_dict = ISICGroup.from_dict(isic_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


