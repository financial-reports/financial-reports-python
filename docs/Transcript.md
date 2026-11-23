# Transcript

A structured call transcript, format `transcript/1`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | &#x60;transcript/1&#x60;. Fields may be added within this version, so ignore fields you do not know; renaming, removing or changing the meaning of a field would be a new version. | 
**filing_id** | **int** | The filing&#39;s id. | 
**company** | [**TranscriptCompany**](TranscriptCompany.md) |  | 
**event** | [**TranscriptEvent**](TranscriptEvent.md) |  | 
**sections** | [**List[TranscriptSection]**](TranscriptSection.md) | The call&#39;s sections in order. Most calls have both; a call without one of them has only the other. | 
**participants** | [**List[TranscriptParticipant]**](TranscriptParticipant.md) |  | 
**turns** | [**List[TranscriptTurn]**](TranscriptTurn.md) | Every turn, in order; &#x60;turns[n].i&#x60; is &#x60;n&#x60;. | 
**quality** | [**TranscriptQuality**](TranscriptQuality.md) | Present only on a call released with a known limitation; absent on every other call. | [optional] 

## Example

```python
from financial_reports_generated_client.models.transcript import Transcript

# TODO update the JSON string below
json = "{}"
# create an instance of Transcript from a JSON string
transcript_instance = Transcript.from_json(json)
# print the JSON string representation of the object
print(Transcript.to_json())

# convert the object into a dict
transcript_dict = transcript_instance.to_dict()
# create an instance of Transcript from a dict
transcript_from_dict = Transcript.from_dict(transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


