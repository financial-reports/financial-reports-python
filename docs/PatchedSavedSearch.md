# PatchedSavedSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** | Your label for the search. | [optional] 
**params** | **object** | The search, as the query parameters of &#x60;GET /filings/search/&#x60;: &#x60;q&#x60; (a string or a list of up to 5 alternatives) and any filter that endpoint takes, e.g. &#x60;{\&quot;q\&quot;: [\&quot;going concern\&quot;, \&quot;material uncertainty\&quot;], \&quot;countries\&quot;: \&quot;DE,FR\&quot;}&#x60;. Checked exactly as that endpoint checks them. &#x60;added_to_platform_from&#x60;/&#x60;_to&#x60;, &#x60;ordering&#x60;, &#x60;page&#x60;, &#x60;page_size&#x60; and &#x60;view&#x60; are set by each run and cannot be saved. | [optional] 
**webhook** | **int** | The id of your webhook that receives each run&#39;s &#x60;saved_search.hits&#x60; event. Leave it out (or null) to pull the new hits yourself with &#x60;POST /filings/search/saved/{id}/new/&#x60; instead; such a search is never run on a schedule. | [optional] 
**is_active** | **bool** | &#x60;false&#x60; pauses the search. At most 20 active per account. | [optional] [default to True]
**max_hits_per_run** | **int** | Hits per delivery or pull, 1-200 (default 50). Further new hits are counted in &#x60;more&#x60; and delivered by the next runs (or pulls), oldest first. | [optional] [default to 50]
**cursor** | **datetime** | Filings added to FinancialFilings at or after this time (minus a short lookback for filings whose text arrived late) are searched by the next run or pull. It moves only after a delivery succeeds, or a pull returns hits. | [optional] [readonly] 
**last_run_at** | **datetime** |  | [optional] [readonly] 
**last_status** | **str** | How the last run ended; empty before the first run.  * &#x60;&#x60; - Never run * &#x60;delivered&#x60; - Delivered * &#x60;no_new_hits&#x60; - No new hits * &#x60;delivery_failed&#x60; - Delivery failed * &#x60;search_unavailable&#x60; - Search unavailable * &#x60;deferred&#x60; - Deferred: the search node was busy or slow * &#x60;not_entitled&#x60; - Not entitled * &#x60;no_webhook&#x60; - No active webhook * &#x60;spend_ceiling&#x60; - Spend ceiling reached * &#x60;invalid_params&#x60; - Invalid params * &#x60;disabled_after_failures&#x60; - Disabled after delivery failures * &#x60;capped&#x60; - Over the result cap: nothing new among the first matches * &#x60;error&#x60; - Error | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from financial_reports_generated_client.models.patched_saved_search import PatchedSavedSearch

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSavedSearch from a JSON string
patched_saved_search_instance = PatchedSavedSearch.from_json(json)
# print the JSON string representation of the object
print(PatchedSavedSearch.to_json())

# convert the object into a dict
patched_saved_search_dict = patched_saved_search_instance.to_dict()
# create an instance of PatchedSavedSearch from a dict
patched_saved_search_from_dict = PatchedSavedSearch.from_dict(patched_saved_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


