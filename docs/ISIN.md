# ISIN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The 12-character International Securities Identification Number. | [readonly] 
**is_primary** | **bool** | Indicates if this is the primary ISIN for the company on this platform. | [readonly] 
**company** | [**CompanyMinimal**](CompanyMinimal.md) | The company associated with this ISIN. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.isin import ISIN

# TODO update the JSON string below
json = "{}"
# create an instance of ISIN from a JSON string
isin_instance = ISIN.from_json(json)
# print the JSON string representation of the object
print(ISIN.to_json())

# convert the object into a dict
isin_dict = isin_instance.to_dict()
# create an instance of ISIN from a dict
isin_from_dict = ISIN.from_dict(isin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


