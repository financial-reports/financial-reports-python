# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | [optional] 
**value** | **str** | A decimal string, as in &#x60;periods&#x60;. | 
**currency** | **str** |  | [optional] 
**trust_tier** | **str** |  | [optional] 
**withheld_reason** | **str** | Present only when &#x60;value&#x60; is null. &#x60;derived_unconfirmed&#x60;: as in &#x60;periods&#x60;. &#x60;scale_conflict&#x60;: the filing&#39;s figure sits a power of ten (10x, 100x, ...) from the figure &#x60;periods&#x60; serves for the line, so one of the two readings is mis-scaled; it is refused, not corrected. Never on per-share figures or share counts. | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_line_items_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_line_items_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_line_items_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_line_items_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_line_items_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerFirstReportedLineItemsInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_first_reported_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


