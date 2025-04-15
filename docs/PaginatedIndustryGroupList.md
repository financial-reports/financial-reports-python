# PaginatedIndustryGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[IndustryGroup]**](IndustryGroup.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_industry_group_list import PaginatedIndustryGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedIndustryGroupList from a JSON string
paginated_industry_group_list_instance = PaginatedIndustryGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedIndustryGroupList.to_json())

# convert the object into a dict
paginated_industry_group_list_dict = paginated_industry_group_list_instance.to_dict()
# create an instance of PaginatedIndustryGroupList from a dict
paginated_industry_group_list_from_dict = PaginatedIndustryGroupList.from_dict(paginated_industry_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


