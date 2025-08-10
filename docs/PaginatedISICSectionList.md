# PaginatedISICSectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ISICSection]**](ISICSection.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_isic_section_list import PaginatedISICSectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedISICSectionList from a JSON string
paginated_isic_section_list_instance = PaginatedISICSectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedISICSectionList.to_json())

# convert the object into a dict
paginated_isic_section_list_dict = paginated_isic_section_list_instance.to_dict()
# create an instance of PaginatedISICSectionList from a dict
paginated_isic_section_list_from_dict = PaginatedISICSectionList.from_dict(paginated_isic_section_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


