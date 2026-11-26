# CompaniesSeriesList200ResponseResultsInnerContinuity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **bool** | The series has the company&#39;s latest period of this length. | [optional] 
**gaps** | **int** | Periods missing between the first and the last. | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_series_list200_response_results_inner_continuity import CompaniesSeriesList200ResponseResultsInnerContinuity

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSeriesList200ResponseResultsInnerContinuity from a JSON string
companies_series_list200_response_results_inner_continuity_instance = CompaniesSeriesList200ResponseResultsInnerContinuity.from_json(json)
# print the JSON string representation of the object
print(CompaniesSeriesList200ResponseResultsInnerContinuity.to_json())

# convert the object into a dict
companies_series_list200_response_results_inner_continuity_dict = companies_series_list200_response_results_inner_continuity_instance.to_dict()
# create an instance of CompaniesSeriesList200ResponseResultsInnerContinuity from a dict
companies_series_list200_response_results_inner_continuity_from_dict = CompaniesSeriesList200ResponseResultsInnerContinuity.from_dict(companies_series_list200_response_results_inner_continuity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


