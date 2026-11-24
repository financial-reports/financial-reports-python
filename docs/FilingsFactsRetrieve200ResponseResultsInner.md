# FilingsFactsRetrieve200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The line&#39;s label as the company prints it. | 
**concept** | **str** | The XBRL concept, for an &#x60;xbrl&#x60; or &#x60;structured&#x60; fact. | [optional] 
**statement** | **str** |  | 
**scope** | **str** | Whose figure it is. &#x60;consolidated&#x60;: the group&#39;s, or for a company without subsidiaries its own statements (a breakdown line of the group&#39;s statements, by product or segment, is the group&#39;s). &#x60;separate&#x60;: the reporting company alone, its parent-only or individual statements beside the group&#39;s. &#x60;segment&#x60;: a segment&#39;s or region&#39;s figure. &#x60;other&#x60;: another entity&#39;s (a subsidiary, an associate, an elimination column). &#x60;unknown&#x60;: the filing does not say. | [optional] 
**dims** | **Dict[str, str]** | &#x60;{\&quot;axis\&quot;: \&quot;member\&quot;}&#x60; for a breakdown fact; absent when there are none. | [optional] 
**value** | **decimal.Decimal** | Exact decimal string, in &#x60;unit&#x60;, unscaled. | 
**unit** | **str** | ISO currency code, &#x60;shares&#x60;, &#x60;pure&#x60;, or a ratio such as &#x60;EUR/shares&#x60;. | [optional] 
**period** | [**FilingsFactsRetrieve200ResponseResultsInnerPeriod**](FilingsFactsRetrieve200ResponseResultsInnerPeriod.md) |  | 
**method** | **str** | Where the value was read: &#x60;xbrl&#x60; and &#x60;structured&#x60; are the company&#39;s own tagged or structured statements; &#x60;llm&#x60; was read from the report&#39;s text and tables. | 
**status** | **str** |  | 
**confidence** | **float** | For an &#x60;llm&#x60; value. | [optional] 
**decimals** | **int** | The precision the company tagged (&#x60;-6&#x60; &#x3D; millions). | [optional] 
**source** | [**FilingsFactsRetrieve200ResponseResultsInnerSource**](FilingsFactsRetrieve200ResponseResultsInnerSource.md) |  | 
**as_printed** | [**FilingsFactsRetrieve200ResponseResultsInnerAsPrinted**](FilingsFactsRetrieve200ResponseResultsInnerAsPrinted.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.filings_facts_retrieve200_response_results_inner import FilingsFactsRetrieve200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingsFactsRetrieve200ResponseResultsInner from a JSON string
filings_facts_retrieve200_response_results_inner_instance = FilingsFactsRetrieve200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(FilingsFactsRetrieve200ResponseResultsInner.to_json())

# convert the object into a dict
filings_facts_retrieve200_response_results_inner_dict = filings_facts_retrieve200_response_results_inner_instance.to_dict()
# create an instance of FilingsFactsRetrieve200ResponseResultsInner from a dict
filings_facts_retrieve200_response_results_inner_from_dict = FilingsFactsRetrieve200ResponseResultsInner.from_dict(filings_facts_retrieve200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


