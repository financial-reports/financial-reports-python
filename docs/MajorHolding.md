# MajorHolding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**filing_id** | **int** |  | [readonly] 
**release_datetime** | **datetime** | When the filing was published; join to GET /filings/{filing_id}/. | [readonly] 
**company_id** | **int** | The issuer: the filing&#39;s company. | [readonly] 
**company_name** | **str** |  | [readonly] 
**seq** | **int** |  | [readonly] 
**regime** | **str** | Rulebook the notice was filed under. Open list: new values are added as markets are added, so treat an unknown value as valid. | 
**form_type_raw** | **str** |  | [readonly] 
**is_amendment** | **bool** |  | [readonly] 
**amendment_no** | **str** |  | [readonly] 
**holder_name** | **str** |  | [readonly] 
**holder_ref** | **str** |  | [readonly] 
**holder_type_raw** | **str** |  | [readonly] 
**citizenship_or_place** | **str** |  | [readonly] 
**member_of_group_raw** | **str** |  | [readonly] 
**event_date** | **date** |  | [readonly] 
**sole_voting** | **decimal.Decimal** |  | [readonly] 
**shared_voting** | **decimal.Decimal** |  | [readonly] 
**sole_dispositive** | **decimal.Decimal** |  | [readonly] 
**shared_dispositive** | **decimal.Decimal** |  | [readonly] 
**aggregate_owned** | **decimal.Decimal** |  | [readonly] 
**percent_of_class** | **decimal.Decimal** |  | [readonly] 
**security_title** | **str** |  | [readonly] 
**cusip** | **str** | The first of &#x60;cusips&#x60;. | [readonly] 
**cusips** | **object** | Every CUSIP the notice names, in its order. | [readonly] 
**isin** | **str** |  | [readonly] 
**comment** | **str** |  | [readonly] 
**extractor** | **str** |  | [readonly] 
**extractor_version** | **int** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.major_holding import MajorHolding

# TODO update the JSON string below
json = "{}"
# create an instance of MajorHolding from a JSON string
major_holding_instance = MajorHolding.from_json(json)
# print the JSON string representation of the object
print(MajorHolding.to_json())

# convert the object into a dict
major_holding_dict = major_holding_instance.to_dict()
# create an instance of MajorHolding from a dict
major_holding_from_dict = MajorHolding.from_dict(major_holding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


