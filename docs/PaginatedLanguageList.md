# PaginatedLanguageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total matching results. Exact for cheap queries, an estimate on broad or expensive ones, which can be far too low: &#x60;count_is_estimate&#x60; says which. Do not use it to decide when to stop: follow &#x60;next&#x60; until it is null. | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Language]**](Language.md) |  | 
**count_is_estimate** | **bool** | True when &#x60;count&#x60; is an estimate rather than an exact count. An estimate can be off by a factor of ten or more. For an exact count, narrow the query (a shorter release_datetime window, fewer types or countries) until this is false, then add up the parts. | [optional] 

## Example

```python
from financial_reports_generated_client.models.paginated_language_list import PaginatedLanguageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLanguageList from a JSON string
paginated_language_list_instance = PaginatedLanguageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLanguageList.to_json())

# convert the object into a dict
paginated_language_list_dict = paginated_language_list_instance.to_dict()
# create an instance of PaginatedLanguageList from a dict
paginated_language_list_from_dict = PaginatedLanguageList.from_dict(paginated_language_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


