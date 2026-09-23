# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**statement_type** | **str** | The KPI&#39;s home statement in the taxonomy, which can differ from the statement it was extracted onto. &#x60;SUP&#x60; appears here but is never a statement type. | 
**depth** | **int** |  | 
**parent_code** | **str** |  | 
**sort_order** | **int** |  | 
**value** | **decimal.Decimal** | Value in absolute units, as an exact DECIMAL STRING - not a number. Parse with a decimal type; float loses precision at financial magnitudes. NULL when the figure was quarantined as unrecoverable. | 
**raw_value** | **decimal.Decimal** | The figure as printed in the document, as an exact decimal string. NULL - together with &#x60;scale&#x60; - when &#x60;value&#x60; is null, or when &#x60;value&#x60; was rebuilt by a repair sweep (the &#x60;balanced_plug&#x60; and &#x60;debt_hierarchy&#x60; derivations), because for those the printed figure was superseded and no &#x60;value &#x3D;&#x3D; raw_value * scale&#x60; relationship holds. Note this does NOT cover every derived value: a &#x60;partial_aggregate&#x60; total is tagged at extraction time, where &#x60;raw_value&#x60; IS the value&#39;s provenance, so it is served normally. | 
**scale** | **str** | Reporting scale of &#x60;raw_value&#x60;. Withheld with it. | 
**currency** | **str** | The value&#39;s own currency code, which may differ from the statement&#39;s reporting currency for per-share figures. NULL for ratios. | 
**confidence** | **float** | RESERVED - currently null on every line item. Nothing in the extraction pipeline writes this field. Do not branch on it. | 
**source_page** | **int** | RESERVED - currently null on every line item. Provenance is filing-level (&#x60;sources&#x60;), not page-level. | 
**updated_at** | **datetime** | When this value was last written. Equal to the extraction time for an untouched value; moves when a later correction pass rewrites the value in place (a re-extraction replaces the whole statement and sets a new one). Compare it with the value from your previous poll to detect a changed figure without diffing. It does not move when a whole statement is withdrawn or when a different filing starts supplying the period - watch &#x60;source_filing&#x60; for that. | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


