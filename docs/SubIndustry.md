# SubIndustry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | GICS Sub-Industry code. | [readonly] 
**name** | **str** | GICS Sub-Industry name. | [readonly] 
**industry** | [**Industry**](Industry.md) | Parent GICS Industry. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.sub_industry import SubIndustry

# TODO update the JSON string below
json = "{}"
# create an instance of SubIndustry from a JSON string
sub_industry_instance = SubIndustry.from_json(json)
# print the JSON string representation of the object
print(SubIndustry.to_json())

# convert the object into a dict
sub_industry_dict = sub_industry_instance.to_dict()
# create an instance of SubIndustry from a dict
sub_industry_from_dict = SubIndustry.from_dict(sub_industry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


