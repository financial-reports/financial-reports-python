# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_id** | **int** |  | [optional] 
**filing_type** | **str** |  | [optional] 
**release_datetime** | **datetime** |  | [optional] 
**is_selected** | **bool** | Exactly one entry per statement is the selected one. | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_sources_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_sources_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_sources_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_sources_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_sources_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


