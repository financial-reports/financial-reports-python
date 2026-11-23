# TranscriptCompany

The company that held the call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Company name. | 
**ticker** | **str** | Ticker symbol. | 
**isin** | **str** | ISIN, or null when we have none for the issuer. | 
**lei** | **str** | Legal Entity Identifier, or null. | 
**cik** | **str** | SEC CIK, zero-padded to 10 digits, or null. | 

## Example

```python
from financial_reports_generated_client.models.transcript_company import TranscriptCompany

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptCompany from a JSON string
transcript_company_instance = TranscriptCompany.from_json(json)
# print the JSON string representation of the object
print(TranscriptCompany.to_json())

# convert the object into a dict
transcript_company_dict = transcript_company_instance.to_dict()
# create an instance of TranscriptCompany from a dict
transcript_company_from_dict = TranscriptCompany.from_dict(transcript_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


