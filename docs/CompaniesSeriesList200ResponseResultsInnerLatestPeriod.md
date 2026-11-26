# CompaniesSeriesList200ResponseResultsInnerLatestPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **date** | Absent for a balance (an instant). | [optional] 
**end** | **date** |  | 
**fiscal_label** | **str** | e.g. &#x60;FY2025&#x60;, &#x60;Q3 2025&#x60;, &#x60;9M 2025&#x60;. | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_series_list200_response_results_inner_latest_period import CompaniesSeriesList200ResponseResultsInnerLatestPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSeriesList200ResponseResultsInnerLatestPeriod from a JSON string
companies_series_list200_response_results_inner_latest_period_instance = CompaniesSeriesList200ResponseResultsInnerLatestPeriod.from_json(json)
# print the JSON string representation of the object
print(CompaniesSeriesList200ResponseResultsInnerLatestPeriod.to_json())

# convert the object into a dict
companies_series_list200_response_results_inner_latest_period_dict = companies_series_list200_response_results_inner_latest_period_instance.to_dict()
# create an instance of CompaniesSeriesList200ResponseResultsInnerLatestPeriod from a dict
companies_series_list200_response_results_inner_latest_period_from_dict = CompaniesSeriesList200ResponseResultsInnerLatestPeriod.from_dict(companies_series_list200_response_results_inner_latest_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


