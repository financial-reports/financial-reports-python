# TranscriptQuality

A known limitation of this call's transcript.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** | One or more of: &#x60;speakers_partly_unidentified&#x60; (more than 20% of the Q&amp;A turns are under an unidentified speaker), &#x60;lower_confidence_edits&#x60; (an unusually large share of the words was corrected and the corrections could not all be verified against an independent reference), &#x60;checker_unverified&#x60; (our independent check of the corrections did not complete). | 
**note** | **str** | The limitation in plain English. The markdown carries the same text under its title as &#x60;&gt; Note: ...&#x60;. | 

## Example

```python
from financial_reports_generated_client.models.transcript_quality import TranscriptQuality

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptQuality from a JSON string
transcript_quality_instance = TranscriptQuality.from_json(json)
# print the JSON string representation of the object
print(TranscriptQuality.to_json())

# convert the object into a dict
transcript_quality_dict = transcript_quality_instance.to_dict()
# create an instance of TranscriptQuality from a dict
transcript_quality_from_dict = TranscriptQuality.from_dict(transcript_quality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


