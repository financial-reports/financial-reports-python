# ResolveRow

One row of a reconciliation batch. Every field is optional, but a row with no identifier at all resolves to `not_covered` + `no_identifiers` rather than failing the whole batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | Opaque client-supplied key, echoed back untouched so results can be joined to source rows. Must be unique within the batch if supplied. Results are also returned in input order. | [optional] 
**isin** | **str** |  | [optional] 
**lei** | **str** |  | [optional] 
**cik** | **str** | Accepted padded or bare: &#x60;CIK0000320193&#x60; and &#x60;320193&#x60; are equivalent. | [optional] 
**ticker** | **str** | Separator-insensitive: &#x60;BRK.B&#x60;, &#x60;BRK-B&#x60; and &#x60;BRK B&#x60; are equivalent. May carry the market as an ISO country suffix (&#x60;01316.HK&#x60;, &#x60;VOLV B.SE&#x60;, &#x60;PETR4.BR&#x60;): the ticker is then matched only against companies listed in that market. | [optional] 
**name** | **str** | Used to corroborate a ticker match, and as a last-resort candidate lookup. A name alone NEVER produces a &#x60;matched&#x60; result. | [optional] 

## Example

```python
from financial_reports_generated_client.models.resolve_row import ResolveRow

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveRow from a JSON string
resolve_row_instance = ResolveRow.from_json(json)
# print the JSON string representation of the object
print(ResolveRow.to_json())

# convert the object into a dict
resolve_row_dict = resolve_row_instance.to_dict()
# create an instance of ResolveRow from a dict
resolve_row_from_dict = ResolveRow.from_dict(resolve_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


