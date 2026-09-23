# MarkdownNotFound

404 body of `GET /filings/{id}/markdown/` (#997, #3514).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A human-readable message describing the error. | 
**processing_status** | **str** | The filing&#39;s conversion status, e.g. &#x60;PENDING&#x60;, &#x60;QUEUED&#x60;, &#x60;PROCESSING&#x60;, &#x60;FAILED&#x60;, &#x60;SKIPPED&#x60;. | 
**reason** | [**ReasonEnum**](ReasonEnum.md) | &#x60;not_processed&#x60;: no converted content yet. &#x60;no_narrative_content&#x60;: the source carries no narrative text. &#x60;content_missing&#x60;: a processed record exists but its content is unavailable.  * &#x60;not_processed&#x60; - not_processed * &#x60;no_narrative_content&#x60; - no_narrative_content * &#x60;content_missing&#x60; - content_missing | 
**retryable** | **bool** | &#x60;true&#x60; only while a conversion is scheduled or running; the response then carries a &#x60;Retry-After&#x60; header. When &#x60;false&#x60;, stop polling and wait for the filing&#39;s &#x60;markdown_url&#x60; to become non-null. | 

## Example

```python
from financial_reports_generated_client.models.markdown_not_found import MarkdownNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownNotFound from a JSON string
markdown_not_found_instance = MarkdownNotFound.from_json(json)
# print the JSON string representation of the object
print(MarkdownNotFound.to_json())

# convert the object into a dict
markdown_not_found_dict = markdown_not_found_instance.to_dict()
# create an instance of MarkdownNotFound from a dict
markdown_not_found_from_dict = MarkdownNotFound.from_dict(markdown_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


