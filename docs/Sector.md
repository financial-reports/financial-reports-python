# Sector

Serializer for GICS Sector classification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | GICS Sector code. | [readonly] 
**name** | **str** | GICS Sector name. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.sector import Sector

# TODO update the JSON string below
json = "{}"
# create an instance of Sector from a JSON string
sector_instance = Sector.from_json(json)
# print the JSON string representation of the object
print(Sector.to_json())

# convert the object into a dict
sector_dict = sector_instance.to_dict()
# create an instance of Sector from a dict
sector_from_dict = Sector.from_dict(sector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


