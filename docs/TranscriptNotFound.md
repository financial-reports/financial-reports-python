# TranscriptNotFound

Returned with a 404 when a filing has no structured transcript to serve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A human-readable message describing the error. | 
**reason** | [**TranscriptNotFoundReasonEnum**](TranscriptNotFoundReasonEnum.md) | &#x60;no_structured_transcript&#x60;: the filing has no released structured transcript (only call transcripts we have restructured carry one; read its markdown instead). &#x60;content_missing&#x60;: one was released but its content is unavailable right now.  * &#x60;no_structured_transcript&#x60; - no_structured_transcript * &#x60;content_missing&#x60; - content_missing | 

## Example

```python
from financial_reports_generated_client.models.transcript_not_found import TranscriptNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptNotFound from a JSON string
transcript_not_found_instance = TranscriptNotFound.from_json(json)
# print the JSON string representation of the object
print(TranscriptNotFound.to_json())

# convert the object into a dict
transcript_not_found_dict = transcript_not_found_instance.to_dict()
# create an instance of TranscriptNotFound from a dict
transcript_not_found_from_dict = TranscriptNotFound.from_dict(transcript_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


