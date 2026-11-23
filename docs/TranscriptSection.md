# TranscriptSection

One section of the call and the range of turns it holds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;prepared_remarks&#x60; or &#x60;qa&#x60;. | 
**turns** | **List[int]** | &#x60;[first, last]&#x60;: the &#x60;i&#x60; of the section&#39;s first and last turn, inclusive. | 

## Example

```python
from financial_reports_generated_client.models.transcript_section import TranscriptSection

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptSection from a JSON string
transcript_section_instance = TranscriptSection.from_json(json)
# print the JSON string representation of the object
print(TranscriptSection.to_json())

# convert the object into a dict
transcript_section_dict = transcript_section_instance.to_dict()
# create an instance of TranscriptSection from a dict
transcript_section_from_dict = TranscriptSection.from_dict(transcript_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


