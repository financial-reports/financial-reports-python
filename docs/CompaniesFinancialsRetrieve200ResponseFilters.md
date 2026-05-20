# CompaniesFinancialsRetrieve200ResponseFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_type** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**fiscal_year_from** | **int** |  | [optional] 
**fiscal_year_to** | **int** |  | [optional] 
**fiscal_period** | **str** |  | [optional] 
**line_items** | **List[str]** |  | [optional] 
**as_of** | **date** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_filters import CompaniesFinancialsRetrieve200ResponseFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponseFilters from a JSON string
companies_financials_retrieve200_response_filters_instance = CompaniesFinancialsRetrieve200ResponseFilters.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponseFilters.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_filters_dict = companies_financials_retrieve200_response_filters_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponseFilters from a dict
companies_financials_retrieve200_response_filters_from_dict = CompaniesFinancialsRetrieve200ResponseFilters.from_dict(companies_financials_retrieve200_response_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


