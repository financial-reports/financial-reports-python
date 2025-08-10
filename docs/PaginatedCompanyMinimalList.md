# PaginatedCompanyMinimalList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CompanyMinimal]**](CompanyMinimal.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_company_minimal_list import PaginatedCompanyMinimalList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCompanyMinimalList from a JSON string
paginated_company_minimal_list_instance = PaginatedCompanyMinimalList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCompanyMinimalList.to_json())

# convert the object into a dict
paginated_company_minimal_list_dict = paginated_company_minimal_list_instance.to_dict()
# create an instance of PaginatedCompanyMinimalList from a dict
paginated_company_minimal_list_from_dict = PaginatedCompanyMinimalList.from_dict(paginated_company_minimal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


