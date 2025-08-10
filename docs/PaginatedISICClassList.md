# PaginatedISICClassList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ISICClass]**](ISICClass.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_isic_class_list import PaginatedISICClassList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedISICClassList from a JSON string
paginated_isic_class_list_instance = PaginatedISICClassList.from_json(json)
# print the JSON string representation of the object
print(PaginatedISICClassList.to_json())

# convert the object into a dict
paginated_isic_class_list_dict = paginated_isic_class_list_instance.to_dict()
# create an instance of PaginatedISICClassList from a dict
paginated_isic_class_list_from_dict = PaginatedISICClassList.from_dict(paginated_isic_class_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


