# ISICSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISIC Section code. | [readonly] 
**name** | **str** | ISIC Section name. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.isic_section import ISICSection

# TODO update the JSON string below
json = "{}"
# create an instance of ISICSection from a JSON string
isic_section_instance = ISICSection.from_json(json)
# print the JSON string representation of the object
print(ISICSection.to_json())

# convert the object into a dict
isic_section_dict = isic_section_instance.to_dict()
# create an instance of ISICSection from a dict
isic_section_from_dict = ISICSection.from_dict(isic_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


