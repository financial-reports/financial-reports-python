# PaginatedSectorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Sector]**](Sector.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_sector_list import PaginatedSectorList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSectorList from a JSON string
paginated_sector_list_instance = PaginatedSectorList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSectorList.to_json())

# convert the object into a dict
paginated_sector_list_dict = paginated_sector_list_instance.to_dict()
# create an instance of PaginatedSectorList from a dict
paginated_sector_list_from_dict = PaginatedSectorList.from_dict(paginated_sector_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


