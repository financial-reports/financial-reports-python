# PaginatedRemovedFilingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The next page. Null on the last page: store the last &#x60;removed_at&#x60; and pass it as &#x60;since&#x60; next time. | [readonly] 
**previous** | **str** | Always null. | [readonly] 
**results** | [**List[RemovedFiling]**](RemovedFiling.md) |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.paginated_removed_filing_list import PaginatedRemovedFilingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRemovedFilingList from a JSON string
paginated_removed_filing_list_instance = PaginatedRemovedFilingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRemovedFilingList.to_json())

# convert the object into a dict
paginated_removed_filing_list_dict = paginated_removed_filing_list_instance.to_dict()
# create an instance of PaginatedRemovedFilingList from a dict
paginated_removed_filing_list_from_dict = PaginatedRemovedFilingList.from_dict(paginated_removed_filing_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


