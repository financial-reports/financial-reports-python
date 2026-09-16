# CompaniesFinancialsRetrieve200ResponseHistoryWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited** | **bool** |  | [optional] 
**max_history_days** | **int** |  | [optional] 
**cutoff** | **datetime** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_history_window import CompaniesFinancialsRetrieve200ResponseHistoryWindow

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponseHistoryWindow from a JSON string
companies_financials_retrieve200_response_history_window_instance = CompaniesFinancialsRetrieve200ResponseHistoryWindow.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponseHistoryWindow.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_history_window_dict = companies_financials_retrieve200_response_history_window_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponseHistoryWindow from a dict
companies_financials_retrieve200_response_history_window_from_dict = CompaniesFinancialsRetrieve200ResponseHistoryWindow.from_dict(companies_financials_retrieve200_response_history_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


