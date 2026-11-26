# FilingsStatementsRetrieve200ResponseStatementsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | **str** |  | 
**scope** | **str** | Whose statement this is (see &#x60;scope&#x60; above). &#x60;mixed&#x60; only with &#x60;scope&#x3D;all&#x60;, for a table printing both: each row then has &#x60;scopes&#x60;, aligned with &#x60;values&#x60;. | 
**title** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**doc_lang** | **str** | Present where known: the report&#39;s language (a language code such as &#x60;de&#x60;), the language of &#x60;label_doc_lang&#x60;. | [optional] 
**periods** | [**List[CompaniesSeriesList200ResponseResultsInnerLatestPeriod]**](CompaniesSeriesList200ResponseResultsInnerLatestPeriod.md) |  | 
**rows** | [**List[FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner]**](FilingsStatementsRetrieve200ResponseStatementsInnerRowsInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.filings_statements_retrieve200_response_statements_inner import FilingsStatementsRetrieve200ResponseStatementsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingsStatementsRetrieve200ResponseStatementsInner from a JSON string
filings_statements_retrieve200_response_statements_inner_instance = FilingsStatementsRetrieve200ResponseStatementsInner.from_json(json)
# print the JSON string representation of the object
print(FilingsStatementsRetrieve200ResponseStatementsInner.to_json())

# convert the object into a dict
filings_statements_retrieve200_response_statements_inner_dict = filings_statements_retrieve200_response_statements_inner_instance.to_dict()
# create an instance of FilingsStatementsRetrieve200ResponseStatementsInner from a dict
filings_statements_retrieve200_response_statements_inner_from_dict = FilingsStatementsRetrieve200ResponseStatementsInner.from_dict(filings_statements_retrieve200_response_statements_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


