# CompanyResolveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[ResolveRow]**](ResolveRow.md) | 1-500 rows to reconcile. | 

## Example

```python
from financial_reports_generated_client.models.company_resolve_request import CompanyResolveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResolveRequest from a JSON string
company_resolve_request_instance = CompanyResolveRequest.from_json(json)
# print the JSON string representation of the object
print(CompanyResolveRequest.to_json())

# convert the object into a dict
company_resolve_request_dict = company_resolve_request_instance.to_dict()
# create an instance of CompanyResolveRequest from a dict
company_resolve_request_from_dict = CompanyResolveRequest.from_dict(company_resolve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


