# PaginatedSubIndustryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SubIndustry]**](SubIndustry.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_sub_industry_list import PaginatedSubIndustryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSubIndustryList from a JSON string
paginated_sub_industry_list_instance = PaginatedSubIndustryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSubIndustryList.to_json())

# convert the object into a dict
paginated_sub_industry_list_dict = paginated_sub_industry_list_instance.to_dict()
# create an instance of PaginatedSubIndustryList from a dict
paginated_sub_industry_list_from_dict = PaginatedSubIndustryList.from_dict(paginated_sub_industry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


