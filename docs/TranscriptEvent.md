# TranscriptEvent

The call itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;earnings_call&#x60;, &#x60;conference&#x60; (a broker or industry conference appearance), &#x60;investor_day&#x60;, or &#x60;other&#x60;: a company event that is none of those, such as an AGM or EGM, a study result, or an M&amp;A or special announcement. Treat a value you do not recognise as &#x60;other&#x60;. | 
**title** | **str** | The event&#39;s title, e.g. &#x60;Q3 2026 Earnings Call&#x60; or &#x60;AGM 2026&#x60;. | 
**var_date** | **date** | Date of the call. | 
**datetime_utc** | **datetime** | Start time of the call, UTC. | 
**fiscal_year** | **int** | Fiscal year the call reports on, or null when it reports on no fiscal period. In practice it is set on earnings calls and null on conferences, investor days and &#x60;other&#x60; events. | 
**fiscal_quarter** | **int** | Fiscal quarter (1-4) the call reports on, or null when it reports on no single quarter. | 

## Example

```python
from financial_reports_generated_client.models.transcript_event import TranscriptEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptEvent from a JSON string
transcript_event_instance = TranscriptEvent.from_json(json)
# print the JSON string representation of the object
print(TranscriptEvent.to_json())

# convert the object into a dict
transcript_event_dict = transcript_event_instance.to_dict()
# create an instance of TranscriptEvent from a dict
transcript_event_from_dict = TranscriptEvent.from_dict(transcript_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


