# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The line&#39;s label as the filer presents it. | 
**concept** | **str** | The XBRL concept, prefixed (&#x60;us-gaap:InventoryNet&#x60;). | 
**value** | **decimal.Decimal** | The line&#39;s value in the filing, in the sign the filer tagged it. | 
**weight** | **int** | +1 or -1: how the line enters this value as served. The filer&#39;s calculation weight, flipped when the value is served in the opposite sign to its tag (an outflow tagged positive, served negative). | 
**codes** | **List[str]** | The line item codes this line is read into; empty when it is part of &#x60;other&#x60;. | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_lines_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_lines_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_lines_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_lines_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_lines_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


