# ISICDivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISIC Division code. | [readonly] 
**name** | **str** | ISIC Division name. | [readonly] 
**sector** | [**ISICSection**](ISICSection.md) | Parent ISIC Section. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.isic_division import ISICDivision

# TODO update the JSON string below
json = "{}"
# create an instance of ISICDivision from a JSON string
isic_division_instance = ISICDivision.from_json(json)
# print the JSON string representation of the object
print(ISICDivision.to_json())

# convert the object into a dict
isic_division_dict = isic_division_instance.to_dict()
# create an instance of ISICDivision from a dict
isic_division_from_dict = ISICDivision.from_dict(isic_division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


