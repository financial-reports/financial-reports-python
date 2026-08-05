# CompanyResolveResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | Echoed from the request row. | 
**input** | **Dict[str, Optional[object]]** | The identifiers supplied for this row, echoed back. | 
**status** | [**CompanyResolveStatusEnum**](CompanyResolveStatusEnum.md) | &#x60;matched&#x60; - resolved to exactly one company. &#x60;matched_via_alias&#x60; - reserved; never returned in this version. &#x60;ambiguous&#x60; - several plausible companies, see &#x60;candidates&#x60;. &#x60;not_covered&#x60; - no company found.  * &#x60;matched&#x60; - Resolved to exactly one company * &#x60;matched_via_alias&#x60; - Reserved; never returned in this version * &#x60;ambiguous&#x60; - Several plausible companies — see candidates * &#x60;not_covered&#x60; - No company found | 
**resolved_via** | [**CompanyResolveViaEnum**](CompanyResolveViaEnum.md) | Which identifier produced the match. Null unless &#x60;status&#x60; is &#x60;matched&#x60;.  * &#x60;isin&#x60; - ISIN * &#x60;lei&#x60; - Legal Entity Identifier * &#x60;cik&#x60; - SEC Central Index Key * &#x60;ticker&#x60; - Primary ticker * &#x60;security_listing&#x60; - Venue ticker via security listing | 
**company** | [**CompanyResolveMatch**](CompanyResolveMatch.md) |  | 
**candidates** | [**List[CompanyResolveMatch]**](CompanyResolveMatch.md) |  | 
**warnings** | **List[str]** | Stable codes qualifying the result. &#x60;no_identifiers&#x60; - the row carried nothing to match on. &#x60;identifier_conflict&#x60; - two identifiers on this row resolved to different companies; both are in &#x60;candidates&#x60;. &#x60;name_disagrees&#x60; - a ticker matched but the supplied name shares no distinguishing token with ours, so the match is not asserted. &#x60;multiple_tickers&#x60; - the ticker maps to more than one company. &#x60;security_listing_unverified&#x60; - matched on a venue ticker with no name supplied, so the match could not be corroborated. This code covers TWO distinct situations that cannot currently be told apart: the listing row may be one of the known ticker collisions, OR the ticker may since have been reassigned to a different issuer (security listings are not retired today). Supplying &#x60;name&#x60; resolves the first but not the second. &#x60;name_tier_skipped&#x60; - the per-request name-lookup budget was exhausted before this row; re-send it in a smaller batch. | 

## Example

```python
from financial_reports_generated_client.models.company_resolve_result import CompanyResolveResult

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResolveResult from a JSON string
company_resolve_result_instance = CompanyResolveResult.from_json(json)
# print the JSON string representation of the object
print(CompanyResolveResult.to_json())

# convert the object into a dict
company_resolve_result_dict = company_resolve_result_instance.to_dict()
# create an instance of CompanyResolveResult from a dict
company_resolve_result_from_dict = CompanyResolveResult.from_dict(company_resolve_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


