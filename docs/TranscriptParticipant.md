# TranscriptParticipant

A person who speaks on the call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **str** | Participant id within this call, referenced by &#x60;turns[].speaker_ref&#x60;. | 
**name** | **str** | Full name, or null when the speaker was not named. | 
**title** | **str** | Job title, or null. | 
**firm** | **str** | Employer, or null. | 
**role** | **str** | &#x60;executive&#x60;, &#x60;analyst&#x60;, &#x60;operator&#x60;, &#x60;moderator&#x60; or &#x60;other&#x60;. | 

## Example

```python
from financial_reports_generated_client.models.transcript_participant import TranscriptParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptParticipant from a JSON string
transcript_participant_instance = TranscriptParticipant.from_json(json)
# print the JSON string representation of the object
print(TranscriptParticipant.to_json())

# convert the object into a dict
transcript_participant_dict = transcript_participant_instance.to_dict()
# create an instance of TranscriptParticipant from a dict
transcript_participant_from_dict = TranscriptParticipant.from_dict(transcript_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


