# CompaniesFinancialsRetrieve200ResponsePeriodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_year** | **int** |  | [optional] 
**fiscal_period** | **str** |  | [optional] 
**period_start_date** | **date** |  | [optional] 
**period_end_date** | **date** |  | [optional] 
**statements** | **List[object]** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInner from a JSON string
companies_financials_retrieve200_response_periods_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_dict = companies_financials_retrieve200_response_periods_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInner from a dict
companies_financials_retrieve200_response_periods_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInner.from_dict(companies_financials_retrieve200_response_periods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


