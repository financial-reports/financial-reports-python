# CompanyResolveSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched** | **int** |  | 
**matched_via_alias** | **int** | Always 0 in this version; reserved for alias-based matching. | 
**ambiguous** | **int** |  | 
**not_covered** | **int** |  | 

## Example

```python
from financial_reports_generated_client.models.company_resolve_summary import CompanyResolveSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResolveSummary from a JSON string
company_resolve_summary_instance = CompanyResolveSummary.from_json(json)
# print the JSON string representation of the object
print(CompanyResolveSummary.to_json())

# convert the object into a dict
company_resolve_summary_dict = company_resolve_summary_instance.to_dict()
# create an instance of CompanyResolveSummary from a dict
company_resolve_summary_from_dict = CompanyResolveSummary.from_dict(company_resolve_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


