# InsiderTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**filing_id** | **int** |  | [readonly] 
**release_datetime** | **datetime** | When the filing was published; join to GET /filings/{filing_id}/. | [readonly] 
**company_id** | **int** | The issuer: the filing&#39;s company. | [readonly] 
**company_name** | **str** |  | [readonly] 
**seq** | **int** | Position of the line within its filing. | [readonly] 
**regime** | **str** | Rulebook the notice was filed under. Open list: new values are added as markets are added, so treat an unknown value as valid. | 
**row_kind** | **str** | &#x60;transaction&#x60; is a deal, &#x60;holding&#x60; a position the notice reports without a deal, &#x60;planned_sale&#x60; an advance notice of a sale (US Form 144). Open list: new values are added as markets are added, so treat an unknown value as valid. | 
**form_type_raw** | **str** |  | [readonly] 
**is_amendment** | **bool** |  | [readonly] 
**insider_name** | **str** |  | [readonly] 
**insider_ref** | **str** | Source-native person id, e.g. the SEC CIK. | [readonly] 
**insider_roles** | **List[str]** | The insider&#39;s roles at the issuer. Open list: new values are added as markets are added, so treat an unknown value as valid. | 
**insider_title_raw** | **str** |  | [readonly] 
**associated_with_name** | **str** | For a closely associated person: the PDMR they are associated with. | [readonly] 
**reporting_persons** | **object** | Every person on a joint notice: &#x60;[{name, ref, roles, title_raw}]&#x60;. The first is the row&#39;s insider. | 
**security_title** | **str** |  | [readonly] 
**instrument_type_raw** | **str** |  | [readonly] 
**isin** | **str** |  | [readonly] 
**is_derivative** | **bool** |  | [readonly] 
**transaction_date** | **date** |  | [readonly] 
**nature** | **str** | The deal, normalised across markets; the source&#39;s own code is &#x60;nature_code_raw&#x60;. Empty on a holding and on a planned sale. Open list: new values are added as markets are added, so treat an unknown value as valid. | 
**nature_code_raw** | **str** |  | [readonly] 
**nature_raw** | **str** |  | [readonly] 
**quantity** | **decimal.Decimal** |  | [readonly] 
**quantity_unit_raw** | **str** |  | [readonly] 
**price** | **decimal.Decimal** |  | [readonly] 
**currency** | **str** |  | [readonly] 
**value** | **decimal.Decimal** | As reported, else quantity x price. | [readonly] 
**acquired_disposed** | **str** | Direction of the deal; empty on a holding. Open list: new values are added as markets are added, so treat an unknown value as valid. | 
**holdings_after** | **decimal.Decimal** |  | [readonly] 
**voting_rights_after** | **decimal.Decimal** |  | [readonly] 
**ownership** | **str** | Direct or indirect ownership. Open list: new values are added as markets are added, so treat an unknown value as valid. | 
**ownership_nature_raw** | **str** |  | [readonly] 
**venue** | **str** |  | [readonly] 
**under_trading_plan** | **bool** | This line was dealt under a pre-arranged trading plan; null when the source does not say so per line (a US Form 4&#39;s 10b5-1 box covers the whole notice). | [readonly] 
**linked_to_share_option_programme** | **bool** |  | [readonly] 
**discretionary** | **bool** | Dealt under discretionary management (Wft 5:48). | [readonly] 
**exercise_price** | **decimal.Decimal** |  | [readonly] 
**exercisable_date** | **date** |  | [readonly] 
**expiration_date** | **date** |  | [readonly] 
**underlying_security** | **str** |  | [readonly] 
**underlying_quantity** | **decimal.Decimal** |  | [readonly] 
**footnotes** | **object** | The footnotes this line cites: &#x60;[{id, text}]&#x60;. | 
**extractor** | **str** |  | [readonly] 
**extractor_version** | **int** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.insider_transaction import InsiderTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of InsiderTransaction from a JSON string
insider_transaction_instance = InsiderTransaction.from_json(json)
# print the JSON string representation of the object
print(InsiderTransaction.to_json())

# convert the object into a dict
insider_transaction_dict = insider_transaction_instance.to_dict()
# create an instance of InsiderTransaction from a dict
insider_transaction_from_dict = InsiderTransaction.from_dict(insider_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


