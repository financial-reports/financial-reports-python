# LineItemDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable machine code, e.g. &#39;revenue&#39;, &#39;total_assets&#39;. Never rename in place — deprecate and add a new code. | 
**name** | **str** | Human display name, e.g. &#39;Total Revenue&#39;. | 
**statement_type** | [**StatementTypeEnum**](StatementTypeEnum.md) |  | 
**statement_type_display** | **str** | Human-readable statement type. | 
**depth** | **int** | Hierarchy depth: 0 &#x3D; top-level total/heading, 1 &#x3D; component of a parent, 2 &#x3D; sub-component. | [optional] 
**parent_code** | **str** | Code of the parent line item in the hierarchy, or null for top-level items. | [optional] 
**sort_order** | **int** | Display order within (statement_type, category). | [optional] 
**category** | **str** | Optional grouping within a statement (e.g. &#39;Operating Expenses&#39;). | [optional] 
**description** | **str** | Definition of the KPI. Used in the extraction prompt. | [optional] 
**aliases** | **object** |  | [optional] 
**is_capital_iq_standard** | **bool** | True if this KPI maps 1:1 to an S&amp;P Capital IQ field. | [optional] 

## Example

```python
from financial_reports_generated_client.models.line_item_definition import LineItemDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemDefinition from a JSON string
line_item_definition_instance = LineItemDefinition.from_json(json)
# print the JSON string representation of the object
print(LineItemDefinition.to_json())

# convert the object into a dict
line_item_definition_dict = line_item_definition_instance.to_dict()
# create an instance of LineItemDefinition from a dict
line_item_definition_from_dict = LineItemDefinition.from_dict(line_item_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


