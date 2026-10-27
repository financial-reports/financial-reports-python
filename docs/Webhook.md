# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the webhook. | [readonly] 
**url** | **str** | Your HTTPS endpoint that receives the payloads. | 
**is_active** | **bool** | &#x60;false&#x60; pauses the webhook without deleting it. Default &#x60;true&#x60;. | [optional] [default to True]
**include_markdown** | **bool** | Include the filing&#39;s &#x60;markdown_content&#x60; in the payload. Default &#x60;true&#x60;. | [optional] [default to True]
**include_isins** | **bool** | Include the company&#39;s ISINs in the payload. Large companies can have thousands. Default &#x60;false&#x60;. | [optional] [default to False]
**track_all_companies** | **bool** | &#x60;true&#x60;: filings from every company. &#x60;false&#x60; (default): only companies on your watchlist. | [optional] [default to False]
**trigger_on_filing_received** | **bool** | Send &#x60;filing.received&#x60; as soon as a filing arrives (fastest). Filing type and other metadata may still be null, and there is no Markdown. Default &#x60;false&#x60;. | [optional] [default to False]
**trigger_on_filing_processed** | **bool** | Send &#x60;filing.processed&#x60; once a filing is classified and converted, with full metadata (and Markdown if &#x60;include_markdown&#x60; is on). Default &#x60;true&#x60;. | [optional] [default to True]
**trigger_on_filing_updated** | **bool** | Also send &#x60;filing.updated&#x60; when a filing you received is re-typed or moved to another company, and &#x60;filing.removed&#x60; when it leaves this webhook&#39;s scope, within 30 days of delivery or while it is held back. &#x60;filing.removed&#x60; for a withdrawn or deleted filing is sent without this flag. Not billed. Default &#x60;false&#x60;. | [optional] [default to False]
**trigger_on_dividend_events** | **bool** | Also send &#x60;dividend.created&#x60; when a company in this webhook&#39;s scope announces a cash dividend, and &#x60;dividend.updated&#x60; when a later notice changes its dates, stage or cancellation. Requires a plan that includes structured financials. Not billed. Default &#x60;false&#x60;. | [optional] [default to False]
**deliver_late_filings** | **bool** | Also deliver filings that reached us more than 48 hours (and at most 30 days) after publication, marked &#x60;late: true&#x60;. Default &#x60;false&#x60;: late arrivals are mostly backfills. | [optional] [default to False]
**subscribed_filing_types** | **List[str]** | Filing type codes to subscribe to (e.g. &#x60;[&#39;10-K&#39;, &#39;IR&#39;]&#x60;). Empty or omitted: all types. | [optional] 
**created_at** | **datetime** | Timestamp when the webhook was created. | [readonly] 
**updated_at** | **datetime** | Timestamp when the webhook was last updated. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


