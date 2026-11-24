# FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The concept&#39;s label, English first. | 
**label_printed** | **str** | Present where the page prints one caption for this line: that caption, in the language of the report. | [optional] 
**label_doc_lang** | **str** | Present where the report&#39;s language is known and a label exists in it: the label in that language. | [optional] 
**label_doc_lang_source** | **str** | With &#x60;label_doc_lang&#x60;: the company&#39;s own label (&#x60;linkbase&#x60;) or the standard taxonomy&#39;s (&#x60;standard&#x60;). | [optional] 
**concept** | **str** |  | [optional] 
**dims** | **Dict[str, str]** |  | [optional] 
**kind** | **str** | Absent for a plain line. | [optional] 
**unit** | **str** |  | [optional] 
**values** | **List[Optional[decimal.Decimal]]** | One per &#x60;periods&#x60; column, as tagged; &#x60;null&#x60; where the line has no value in it. | [optional] 
**refs** | **List[Optional[str]]** |  | [optional] 
**period_edge** | **str** | Present on an opening (&#x60;start&#x60;) or closing (&#x60;end&#x60;) balance line, such as cash at the beginning or end of the period: each value is the balance at that edge of its column&#39;s period. | [optional] 
**balance_at** | **str** | Present on a balance line read at an edge of its duration columns, like &#x60;period_edge&#x60;, where the line carries no opening or closing label. | [optional] 
**scopes** | **List[Optional[str]]** | Only on a &#x60;mixed&#x60; statement: whose value each cell is, aligned with &#x60;values&#x60;. | [optional] 
**printed_sign_sources** | **List[Optional[str]]** | XBRL only, aligned with &#x60;values&#x60;: where the printed sign came from, the report page itself (&#x60;rendering&#x60;) or the line&#39;s label role (&#x60;label_role&#x60;, a hint). | [optional] 
**negated** | **bool** | Present, &#x60;true&#x60;, when the company prints this line with the opposite sign to the tagged value. | [optional] 
**printed_values** | **List[Optional[decimal.Decimal]]** | With &#x60;negated&#x60;: the values with the sign the company prints. | [optional] 
**folded_member** | **bool** | Present, &#x60;true&#x60;, when the line&#39;s values come from its only breakdown member. | [optional] 
**children** | **List[object]** | Lines under this one in the company&#39;s own presentation, same shape. | [optional] 

## Example

```python
from financial_reports_generated_client.models.filings_statements_retrieve200_response_statements_inner_rows_inner import FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner from a JSON string
filings_statements_retrieve200_response_statements_inner_rows_inner_instance = FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner.from_json(json)
# print the JSON string representation of the object
print(FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner.to_json())

# convert the object into a dict
filings_statements_retrieve200_response_statements_inner_rows_inner_dict = filings_statements_retrieve200_response_statements_inner_rows_inner_instance.to_dict()
# create an instance of FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner from a dict
filings_statements_retrieve200_response_statements_inner_rows_inner_from_dict = FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner.from_dict(filings_statements_retrieve200_response_statements_inner_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


