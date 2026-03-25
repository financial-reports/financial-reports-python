# PaginatedISINList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ISIN]**](ISIN.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_isin_list import PaginatedISINList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedISINList from a JSON string
paginated_isin_list_instance = PaginatedISINList.from_json(json)
# print the JSON string representation of the object
print(PaginatedISINList.to_json())

# convert the object into a dict
paginated_isin_list_dict = paginated_isin_list_instance.to_dict()
# create an instance of PaginatedISINList from a dict
paginated_isin_list_from_dict = PaginatedISINList.from_dict(paginated_isin_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


