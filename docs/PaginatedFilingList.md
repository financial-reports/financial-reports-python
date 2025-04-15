# PaginatedFilingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Filing]**](Filing.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_filing_list import PaginatedFilingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilingList from a JSON string
paginated_filing_list_instance = PaginatedFilingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilingList.to_json())

# convert the object into a dict
paginated_filing_list_dict = paginated_filing_list_instance.to_dict()
# create an instance of PaginatedFilingList from a dict
paginated_filing_list_from_dict = PaginatedFilingList.from_dict(paginated_filing_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


