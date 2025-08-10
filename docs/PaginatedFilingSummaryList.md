# PaginatedFilingSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FilingSummary]**](FilingSummary.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_filing_summary_list import PaginatedFilingSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilingSummaryList from a JSON string
paginated_filing_summary_list_instance = PaginatedFilingSummaryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilingSummaryList.to_json())

# convert the object into a dict
paginated_filing_summary_list_dict = paginated_filing_summary_list_instance.to_dict()
# create an instance of PaginatedFilingSummaryList from a dict
paginated_filing_summary_list_from_dict = PaginatedFilingSummaryList.from_dict(paginated_filing_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


