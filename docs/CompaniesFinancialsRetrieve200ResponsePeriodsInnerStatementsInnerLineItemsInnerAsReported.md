# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported

Present only with `include=as_reported`, and only on a total read straight from one fact of the filer's XBRL (not derived, not adjusted) whose own calculation tree adds up beneath it, at the statement's primary period: the face lines the total is made of, as the filer tagged them. `value` = sum(`weight` x line `value`) + `other` over the lines that have `codes`; the lines without codes add up to `other` within the filer's rounding. Not the `raw_value` / `scale` pair, which is this value as printed. Absent on comparative-period values, derived or adjusted values, filings whose tree does not add up, and with `as_known_at`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**other** | **decimal.Decimal** | The part of &#x60;value&#x60; the lines with &#x60;codes&#x60; do not explain: &#x60;value&#x60; - sum(&#x60;weight&#x60; x their &#x60;value&#x60;). | 
**lines** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReportedLinesInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_as_reported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


