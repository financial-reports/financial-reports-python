# PaginatedCompanyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Company]**](Company.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_company_list import PaginatedCompanyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCompanyList from a JSON string
paginated_company_list_instance = PaginatedCompanyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCompanyList.to_json())

# convert the object into a dict
paginated_company_list_dict = paginated_company_list_instance.to_dict()
# create an instance of PaginatedCompanyList from a dict
paginated_company_list_from_dict = PaginatedCompanyList.from_dict(paginated_company_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


