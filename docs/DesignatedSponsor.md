# DesignatedSponsor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.designated_sponsor import DesignatedSponsor

# TODO update the JSON string below
json = "{}"
# create an instance of DesignatedSponsor from a JSON string
designated_sponsor_instance = DesignatedSponsor.from_json(json)
# print the JSON string representation of the object
print(DesignatedSponsor.to_json())

# convert the object into a dict
designated_sponsor_dict = designated_sponsor_instance.to_dict()
# create an instance of DesignatedSponsor from a dict
designated_sponsor_from_dict = DesignatedSponsor.from_dict(designated_sponsor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


