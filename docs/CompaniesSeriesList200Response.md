# CompaniesSeriesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | 
**previous** | **str** |  | 
**results** | [**List[CompaniesSeriesList200ResponseResultsInner]**](CompaniesSeriesList200ResponseResultsInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_series_list200_response import CompaniesSeriesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSeriesList200Response from a JSON string
companies_series_list200_response_instance = CompaniesSeriesList200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesSeriesList200Response.to_json())

# convert the object into a dict
companies_series_list200_response_dict = companies_series_list200_response_instance.to_dict()
# create an instance of CompaniesSeriesList200Response from a dict
companies_series_list200_response_from_dict = CompaniesSeriesList200Response.from_dict(companies_series_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


