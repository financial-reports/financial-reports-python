# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerVintagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_id** | **int** |  | 
**filing_type** | **str** |  | 
**release_datetime** | **datetime** |  | 
**is_comparative** | **bool** | The filing reported this period as a prior-year column, not as its own period. | 
**line_items** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner.md) |  | 
**is_selected** | **bool** | The filing this statement is served from. | 
**is_first_reported** | **bool** | The filing &#x60;first_reported&#x60; names. | 
**is_own_report** | **bool** | The filing reports the period as its own and counts as the company&#39;s own report, the filings &#x60;first_reported&#x60; is picked from. False for a prior-year column, a fragment, a filing in another currency than the company reports in, the parent&#39;s separate accounts where the group&#39;s exist, a non-report document or an amendment. | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_vintages_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerVintagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerVintagesInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_vintages_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerVintagesInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerVintagesInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_vintages_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_vintages_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerVintagesInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_vintages_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerVintagesInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_vintages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


