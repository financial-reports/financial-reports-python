# CompanyMergedInto

Inline schema type for `merged_into` on CompanySerializer (#1118).  Deliberately two fields: the pointer exists so a consumer can repoint its own row, not so it can avoid a second request. Fetch the canonical id for the full record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal id of the canonical company that replaced this one. | 
**name** | **str** | Name of the canonical company. | 

## Example

```python
from financial_reports_generated_client.models.company_merged_into import CompanyMergedInto

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyMergedInto from a JSON string
company_merged_into_instance = CompanyMergedInto.from_json(json)
# print the JSON string representation of the object
print(CompanyMergedInto.to_json())

# convert the object into a dict
company_merged_into_dict = company_merged_into_instance.to_dict()
# create an instance of CompanyMergedInto from a dict
company_merged_into_from_dict = CompanyMergedInto.from_dict(company_merged_into_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


