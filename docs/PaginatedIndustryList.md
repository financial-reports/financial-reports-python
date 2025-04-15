# PaginatedIndustryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Industry]**](Industry.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_industry_list import PaginatedIndustryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedIndustryList from a JSON string
paginated_industry_list_instance = PaginatedIndustryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedIndustryList.to_json())

# convert the object into a dict
paginated_industry_list_dict = paginated_industry_list_instance.to_dict()
# create an instance of PaginatedIndustryList from a dict
paginated_industry_list_from_dict = PaginatedIndustryList.from_dict(paginated_industry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


