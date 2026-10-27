# CompaniesSplitsRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | 
**filters** | [**CompaniesDividendsRetrieve200ResponseFilters**](CompaniesDividendsRetrieve200ResponseFilters.md) |  | 
**splits** | [**List[CompaniesSplitsRetrieve200ResponseSplitsInner]**](CompaniesSplitsRetrieve200ResponseSplitsInner.md) |  | 
**history_window** | [**CompaniesFinancialsRetrieve200ResponseHistoryWindow**](CompaniesFinancialsRetrieve200ResponseHistoryWindow.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_splits_retrieve200_response import CompaniesSplitsRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSplitsRetrieve200Response from a JSON string
companies_splits_retrieve200_response_instance = CompaniesSplitsRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesSplitsRetrieve200Response.to_json())

# convert the object into a dict
companies_splits_retrieve200_response_dict = companies_splits_retrieve200_response_instance.to_dict()
# create an instance of CompaniesSplitsRetrieve200Response from a dict
companies_splits_retrieve200_response_from_dict = CompaniesSplitsRetrieve200Response.from_dict(companies_splits_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


