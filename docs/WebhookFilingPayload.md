# WebhookFilingPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal FinancialFilings Filing ID. | [readonly] 
**processing_status** | **str** | The current processing status of the filing (e.g., &#39;PENDING&#39;, &#39;COMPLETED&#39;). | [readonly] 
**filing_type_code** | **str** | Short code for the filing type (e.g., &#39;10-K&#39;). May be null for &#39;filing.received&#39; events. | [readonly] 
**filing_type_name** | **str** | Human-readable filing type (e.g., &#39;Annual Report&#39;). May be null for &#39;filing.received&#39; events. | [readonly] 
**language_code** | **str** | ISO 639-1 language code (e.g., &#39;en&#39;). May be null for &#39;filing.received&#39; events. | [readonly] 
**language_name** | **str** | Human-readable language name (e.g., &#39;English&#39;). May be null for &#39;filing.received&#39; events. | [readonly] 
**title** | **str** | The title of the filing. | [readonly] 
**dissemination_datetime** | **datetime** | The exact time the filing was disseminated by the source. | [readonly] 
**release_datetime** | **datetime** | The official release time of the filing (e.g., the period end). | [readonly] 
**ingestion_mode** | **str** | Whether the filing was added to the platform promptly after publication. &#x60;REALTIME&#x60;: added within the source&#39;s normal publication delay (5 to 48 hours after &#x60;release_datetime&#x60;, depending on the source). &#x60;BACKFILLED&#x60;: everything else, including historical imports and new filings that reached the platform late, for example after a source outage. Set once when the filing is added and not recalculated afterwards. Webhooks are not sent for filings added more than 48 hours after &#x60;release_datetime&#x60; (for FSMA, after &#x60;dissemination_datetime&#x60;; outside authorised recovery windows) unless the webhook has &#x60;deliver_late_filings&#x60; enabled, so most deliveries are REALTIME. A delivery can still carry BACKFILLED when the filing arrived after its source&#39;s normal delay but inside those 48 hours, has no &#x60;release_datetime&#x60;, falls in an authorised recovery window, or is a late delivery (&#x60;late: true&#x60;).  * &#x60;REALTIME&#x60; - Realtime * &#x60;BACKFILLED&#x60; - Backfilled | [readonly] 
**late** | **bool** | True when the filing reached the platform more than 48 hours after publication. Such filings are sent only to webhooks with &#x60;deliver_late_filings&#x60; enabled, and only up to 30 days late; the one exception is a deliberate re-send after an outage on our side, which can reach every webhook at any lag. Always present. | [readonly] 
**ingest_lag_hours** | **float** | Hours between publication (&#x60;release_datetime&#x60;; for FSMA, &#x60;dissemination_datetime&#x60;) and the filing reaching the platform, to one decimal. Null when the filing has no &#x60;release_datetime&#x60;. Negative when the source dates the filing in the future. | [readonly] 
**document_url** | **str** | A direct, temporary link to download the original filing document (e.g., PDF). | [readonly] 
**source_url** | **str** | Original public link for the filing at the source authority. Null unless the webhook owner&#39;s account has source identities unlocked, the source is anonymised, or no stable link exists. | [readonly] 
**source_filing_type** | **str** | The source authority&#39;s own classification label, verbatim. Null when the source publishes no label, it was not captured, or the source is anonymised. Not gated on source identities. | [readonly] 
**markdown_content** | **str** | The full, processed content of the filing in Markdown format. This field is only included if your webhook is configured with &#39;include_markdown: true&#39; AND the event type is &#39;filing.processed&#39;. It is null for &#39;filing.received&#39;. Even with &#39;include_markdown: true&#39; on a &#39;filing.processed&#39; event, this field is null unless the webhook owner&#39;s account has Level 2 (Processed Filings) access -- the same tier gate applied to the REST /markdown/ endpoint. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook_filing_payload import WebhookFilingPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFilingPayload from a JSON string
webhook_filing_payload_instance = WebhookFilingPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookFilingPayload.to_json())

# convert the object into a dict
webhook_filing_payload_dict = webhook_filing_payload_instance.to_dict()
# create an instance of WebhookFilingPayload from a dict
webhook_filing_payload_from_dict = WebhookFilingPayload.from_dict(webhook_filing_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


