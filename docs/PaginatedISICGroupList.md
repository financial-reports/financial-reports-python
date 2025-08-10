# PaginatedISICGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ISICGroup]**](ISICGroup.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_isic_group_list import PaginatedISICGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedISICGroupList from a JSON string
paginated_isic_group_list_instance = PaginatedISICGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedISICGroupList.to_json())

# convert the object into a dict
paginated_isic_group_list_dict = paginated_isic_group_list_instance.to_dict()
# create an instance of PaginatedISICGroupList from a dict
paginated_isic_group_list_from_dict = PaginatedISICGroupList.from_dict(paginated_isic_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


