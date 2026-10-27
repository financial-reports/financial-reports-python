# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_at** | **datetime** |  | 
**op** | **str** | &#x60;insert&#x60;: first written. &#x60;update&#x60;: corrected. &#x60;delete&#x60;: removed (it may be written again by a later &#x60;insert&#x60;). &#x60;pre_recording&#x60;: a correction from before recording started, approximate time. | 
**old_value** | **decimal.Decimal** | &#x60;value&#x60; before the change; null on insert. | 
**new_value** | **decimal.Decimal** | &#x60;value&#x60; after the change; null on delete. A change to another field of the value (its as-reported figure, currency or statement) has old_value &#x3D;&#x3D; new_value. | 
**reason** | **str** | &#x60;extraction&#x60;: (re-)extraction from the document. &#x60;cleanup&#x60;: an automated rule-based correction. &#x60;repair&#x60;: a correction pass run by our team. &#x60;manual&#x60;: a hand edit. &#x60;unknown&#x60;: not recorded. | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_revisions_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_revisions_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_revisions_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_revisions_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_revisions_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_revisions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


