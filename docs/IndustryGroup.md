# IndustryGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | GICS Industry Group code. | [readonly] 
**name** | **str** | GICS Industry Group name. | [readonly] 
**sector** | [**Sector**](Sector.md) | Parent GICS Sector. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.industry_group import IndustryGroup

# TODO update the JSON string below
json = "{}"
# create an instance of IndustryGroup from a JSON string
industry_group_instance = IndustryGroup.from_json(json)
# print the JSON string representation of the object
print(IndustryGroup.to_json())

# convert the object into a dict
industry_group_dict = industry_group_instance.to_dict()
# create an instance of IndustryGroup from a dict
industry_group_from_dict = IndustryGroup.from_dict(industry_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


