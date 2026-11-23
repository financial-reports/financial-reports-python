# TranscriptTurn

One speaker's uninterrupted turn.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i** | **int** | Position of the turn in the call, from 0. | 
**section** | **str** | &#x60;prepared_remarks&#x60; or &#x60;qa&#x60;. | 
**type** | **str** | &#x60;prepared&#x60;, &#x60;operator&#x60;, &#x60;moderator&#x60;, &#x60;question&#x60;, &#x60;answer&#x60; or &#x60;other&#x60;. | 
**answers_turn** | **int** | On an &#x60;answer&#x60;, the &#x60;i&#x60; of the question it responds to, or null when that is not known. Other turns normally carry null. | 
**speaker_ref** | **str** | The speaker&#39;s &#x60;participants[].pid&#x60;, or null when the speaker is not listed in &#x60;participants&#x60; (an unidentified speaker, often the operator, a video or an announcer). | 
**speaker_role** | **str** | &#x60;executive&#x60;, &#x60;analyst&#x60;, &#x60;operator&#x60;, &#x60;moderator&#x60; or &#x60;other&#x60;, or null when it is not known. | 
**speaker_heading** | **str** | The speaker line as the markdown shows it, without the bold and the &#x60;[Q]&#x60;/&#x60;[A]&#x60; tag, e.g. &#x60;Jane Doe - Example Corp - Chief Executive Officer&#x60;. The markdown shows it once for consecutive turns by the same speaker. | 
**paragraphs** | **List[str]** | The turn&#39;s text, one string per paragraph. | 

## Example

```python
from financial_reports_generated_client.models.transcript_turn import TranscriptTurn

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptTurn from a JSON string
transcript_turn_instance = TranscriptTurn.from_json(json)
# print the JSON string representation of the object
print(TranscriptTurn.to_json())

# convert the object into a dict
transcript_turn_dict = transcript_turn_instance.to_dict()
# create an instance of TranscriptTurn from a dict
transcript_turn_from_dict = TranscriptTurn.from_dict(transcript_turn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


