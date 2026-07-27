# PaginatedCompanyMergeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CompanyMerge]**](CompanyMerge.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_company_merge_list import PaginatedCompanyMergeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCompanyMergeList from a JSON string
paginated_company_merge_list_instance = PaginatedCompanyMergeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCompanyMergeList.to_json())

# convert the object into a dict
paginated_company_merge_list_dict = paginated_company_merge_list_instance.to_dict()
# create an instance of PaginatedCompanyMergeList from a dict
paginated_company_merge_list_from_dict = PaginatedCompanyMergeList.from_dict(paginated_company_merge_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


