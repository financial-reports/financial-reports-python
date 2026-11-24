# PaginatedSavedSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total matching results. Exact for cheap queries, an estimate on broad or expensive ones. Do not use it to decide when to stop: follow &#x60;next&#x60; until it is null. | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SavedSearch]**](SavedSearch.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_saved_search_list import PaginatedSavedSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSavedSearchList from a JSON string
paginated_saved_search_list_instance = PaginatedSavedSearchList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSavedSearchList.to_json())

# convert the object into a dict
paginated_saved_search_list_dict = paginated_saved_search_list_instance.to_dict()
# create an instance of PaginatedSavedSearchList from a dict
paginated_saved_search_list_from_dict = PaginatedSavedSearchList.from_dict(paginated_saved_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


