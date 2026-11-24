# FilingsStatementsRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_id** | **int** |  | 
**method** | **str** | Where the value was read: &#x60;xbrl&#x60; and &#x60;structured&#x60; are the company&#39;s own tagged or structured statements; &#x60;llm&#x60; was read from the report&#39;s text and tables. | 
**statements** | [**List[FilingsStatementsRetrieve200ResponseStatementsInner]**](FilingsStatementsRetrieve200ResponseStatementsInner.md) |  | 
**scope** | **str** | Whose statements were served: the &#x60;scope&#x60; asked for, else the group&#39;s (&#x60;consolidated&#x60;) where the filing has any, else the company&#39;s own (&#x60;separate&#x60;, a company without subsidiaries); null when the filing has neither. | 
**scopes_available** | **List[str]** | The entities the filing&#39;s statements are printed for, notes and other tables included: ask for another with &#x60;scope&#x60; (and &#x60;statement&#x60; for a note). | 

## Example

```python
from financial_reports_generated_client.models.filings_statements_retrieve200_response import FilingsStatementsRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FilingsStatementsRetrieve200Response from a JSON string
filings_statements_retrieve200_response_instance = FilingsStatementsRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(FilingsStatementsRetrieve200Response.to_json())

# convert the object into a dict
filings_statements_retrieve200_response_dict = filings_statements_retrieve200_response_instance.to_dict()
# create an instance of FilingsStatementsRetrieve200Response from a dict
filings_statements_retrieve200_response_from_dict = FilingsStatementsRetrieve200Response.from_dict(filings_statements_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


