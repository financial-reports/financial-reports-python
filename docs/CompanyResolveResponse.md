# CompanyResolveResponse

Deliberately not the paginated `{count, next, previous, results}` envelope: this is a single non-paginated POST action whose result set is exactly the request's rows, in the same order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**CompanyResolveSummary**](CompanyResolveSummary.md) |  | 
**results** | [**List[CompanyResolveResult]**](CompanyResolveResult.md) |  | 

## Example

```python
from financial_reports_generated_client.models.company_resolve_response import CompanyResolveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResolveResponse from a JSON string
company_resolve_response_instance = CompanyResolveResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyResolveResponse.to_json())

# convert the object into a dict
company_resolve_response_dict = company_resolve_response_instance.to_dict()
# create an instance of CompanyResolveResponse from a dict
company_resolve_response_from_dict = CompanyResolveResponse.from_dict(company_resolve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


