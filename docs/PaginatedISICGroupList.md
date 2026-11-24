# PaginatedISICGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total matching results. Exact for cheap queries, an estimate on broad or expensive ones, which can be far too low: &#x60;count_is_estimate&#x60; says which. Do not use it to decide when to stop: follow &#x60;next&#x60; until it is null. | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ISICGroup]**](ISICGroup.md) |  | 
**count_is_estimate** | **bool** | True when &#x60;count&#x60; is an estimate rather than an exact count. An estimate can be off by a factor of ten or more. For an exact count, narrow the query (a shorter release_datetime window, fewer types or countries) until this is false, then add up the parts. | [optional] 

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


