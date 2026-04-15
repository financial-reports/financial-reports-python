# FinancialLineItemCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**statement_type** | **str** | Statement type of the KPI definition (IS, BS, CFS, SUP). May differ from the parent statement — e.g. SUP items appear on whichever statement they were extracted from. | 
**depth** | **int** |  | 
**parent_code** | **str** |  | [readonly] 
**sort_order** | **int** |  | 
**value** | **decimal.Decimal** | Value scaled to units (e.g. thousands * 1000). Use for cross-company comparison. | 
**raw_value** | **decimal.Decimal** | Value as reported in the document, before scaling. | 
**scale** | **str** | Reporting scale of raw_value: units, thousands, millions, billions. | 

## Example

```python
from financial_reports_generated_client.models.financial_line_item_compact import FinancialLineItemCompact

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialLineItemCompact from a JSON string
financial_line_item_compact_instance = FinancialLineItemCompact.from_json(json)
# print the JSON string representation of the object
print(FinancialLineItemCompact.to_json())

# convert the object into a dict
financial_line_item_compact_dict = financial_line_item_compact_instance.to_dict()
# create an instance of FinancialLineItemCompact from a dict
financial_line_item_compact_from_dict = FinancialLineItemCompact.from_dict(financial_line_item_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


