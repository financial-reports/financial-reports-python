# WebhookCompanyPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal FinancialFilings Company ID. | [readonly] 
**name** | **str** | Company name. | [readonly] 
**ticker** | **str** | Primary stock ticker. | [readonly] 
**lei** | **str** | Legal Entity Identifier. | [readonly] 
**website** | **str** | Company&#39;s official website. | [readonly] 
**company_page** | **str** | URL to the company&#39;s page on FinancialFilings. | [readonly] 
**country_name** | **str** | Name of the company&#39;s country of incorporation. | [readonly] 
**country_code_alpha2** | **str** | ISO 3166-1 alpha-2 country code. | [readonly] 
**isins** | **List[str]** | List of ISIN codes (strings) associated with the company, at most 1,000. The Primary ISIN is always at index 0; the rest are in ascending code order. Only included if your webhook is configured with &#39;include_isins: true&#39;. When the company has more than 1,000 ISINs the list is cut and isins_url is set. | [readonly] 
**isin_count** | **int** | Total number of ISINs on the company, which can exceed len(isins). Only included with &#39;include_isins: true&#39;. | [readonly] 
**isins_url** | **str** | Only present when isins was cut at 1,000: the company&#39;s paginated REST listing, e.g. https://api.financialreports.eu/isins/?company&#x3D;35612. Offset pagination stops at 50,000 rows; above that, narrow with &amp;search&#x3D;&lt;code prefix&gt;. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook_company_payload import WebhookCompanyPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCompanyPayload from a JSON string
webhook_company_payload_instance = WebhookCompanyPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookCompanyPayload.to_json())

# convert the object into a dict
webhook_company_payload_dict = webhook_company_payload_instance.to_dict()
# create an instance of WebhookCompanyPayload from a dict
webhook_company_payload_from_dict = WebhookCompanyPayload.from_dict(webhook_company_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


