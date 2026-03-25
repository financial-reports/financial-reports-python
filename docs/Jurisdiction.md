# Jurisdiction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISO 3166-1 or ISO 3166-2 jurisdiction code (e.g., GB, US-DE). | [readonly] 
**name** | **str** | Human-readable name of the jurisdiction. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.jurisdiction import Jurisdiction

# TODO update the JSON string below
json = "{}"
# create an instance of Jurisdiction from a JSON string
jurisdiction_instance = Jurisdiction.from_json(json)
# print the JSON string representation of the object
print(Jurisdiction.to_json())

# convert the object into a dict
jurisdiction_dict = jurisdiction_instance.to_dict()
# create an instance of Jurisdiction from a dict
jurisdiction_from_dict = Jurisdiction.from_dict(jurisdiction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


