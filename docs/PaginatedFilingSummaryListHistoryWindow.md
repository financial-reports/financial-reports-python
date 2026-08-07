# PaginatedFilingSummaryListHistoryWindow

Present when the caller's plan applies a rolling history window AND this request reached past its cutoff. Absent for callers with unrestricted history. It means the PLAN bounds how far back this account can see — filings older than the cutoff exist in the FinancialFilings archive. It is never a statement about catalog coverage, and it does not by itself prove that this particular result set lost rows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited** | **bool** |  | [optional] 
**max_history_days** | **int** |  | [optional] 
**cutoff** | **datetime** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.paginated_filing_summary_list_history_window import PaginatedFilingSummaryListHistoryWindow

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilingSummaryListHistoryWindow from a JSON string
paginated_filing_summary_list_history_window_instance = PaginatedFilingSummaryListHistoryWindow.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilingSummaryListHistoryWindow.to_json())

# convert the object into a dict
paginated_filing_summary_list_history_window_dict = paginated_filing_summary_list_history_window_instance.to_dict()
# create an instance of PaginatedFilingSummaryListHistoryWindow from a dict
paginated_filing_summary_list_history_window_from_dict = PaginatedFilingSummaryListHistoryWindow.from_dict(paginated_filing_summary_list_history_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


