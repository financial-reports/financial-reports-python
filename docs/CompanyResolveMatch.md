# CompanyResolveMatch

The company payload on a resolve result.  Purpose-built rather than reusing CompanyMinimalSerializer, which has no `ticker` -- unusable for a ticker-reconciliation endpoint. Every field here is already published on /api/companies/, so this adds no new public surface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique company identifier. | [readonly] 
**name** | **str** | Company name. | [readonly] 
**ticker** | **str** | The company&#39;s primary ticker. Secondary share classes live on the security-listings endpoint, not here. | [readonly] 
**isins** | **List[str]** | Primary ISIN(s). Use the company detail endpoint for the full list. | [readonly] 
**lei** | **str** | Legal Entity Identifier (ISO 17442). | [readonly] 
**country_code** | **str** | ISO 3166-1 alpha-2 country code. | [readonly] 
**listing_status** | **str** | LISTED, DELISTED, SUSPENDED or UNKNOWN. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.company_resolve_match import CompanyResolveMatch

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResolveMatch from a JSON string
company_resolve_match_instance = CompanyResolveMatch.from_json(json)
# print the JSON string representation of the object
print(CompanyResolveMatch.to_json())

# convert the object into a dict
company_resolve_match_dict = company_resolve_match_instance.to_dict()
# create an instance of CompanyResolveMatch from a dict
company_resolve_match_from_dict = CompanyResolveMatch.from_dict(company_resolve_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


