# OicsNodeRef

A node of the OICS tree, or an entity type, by code and English name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code. | 
**name** | **str** | Name, in English. | 

## Example

```python
from financial_reports_generated_client.models.oics_node_ref import OicsNodeRef

# TODO update the JSON string below
json = "{}"
# create an instance of OicsNodeRef from a JSON string
oics_node_ref_instance = OicsNodeRef.from_json(json)
# print the JSON string representation of the object
print(OicsNodeRef.to_json())

# convert the object into a dict
oics_node_ref_dict = oics_node_ref_instance.to_dict()
# create an instance of OicsNodeRef from a dict
oics_node_ref_from_dict = OicsNodeRef.from_dict(oics_node_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


