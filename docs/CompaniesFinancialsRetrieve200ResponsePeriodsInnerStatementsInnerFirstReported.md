# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReported

Present only with `include=first_reported`. The figures for this period and statement as the filing that first reported the period as its own stated them: of the filings presenting the period as their own that count as the company's own report (not a later report's prior-year column, a fragment, another entity's filing, the parent's separate accounts where the group's exist, or an amendment), the one released first. That filing's own values only: no value filled in from another filing. `release_datetime` is when they became public, to the time of day where the regulator gives one. `null` where no filing reported the period as its own.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_id** | **int** |  | 
**filing_type** | **str** |  | 
**release_datetime** | **datetime** |  | 
**is_comparative** | **bool** | The filing reported this period as a prior-year column, not as its own period. | 
**line_items** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReported

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReported from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReported.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReported.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReported from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReported.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


