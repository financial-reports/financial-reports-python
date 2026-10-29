# CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted

The amount on today's share basis: divided (per-share figures) or multiplied (share counts) by `adjustment_factor`, the product of `ratio_new / ratio_old` of every split, reverse split and bonus issue in `/companies/{id}/splits/` that took effect after the filing the value was read from was published. A filing published after a split already states the new basis, so it is not adjusted again. `adjustment_factor` `1` and no `split_event_ids`: nothing to adjust. Rights issues and spin-offs are not adjusted. `value` is null, with `null_reason`, when the filing predates our split history (1990), when two events that cannot both be right would apply, when a split that applies is not served to you, near the record date of a split whose ex-date no notice states, for a period-end share count or book value per share with a split between the period end and the publication, or for a standalone quarter derived from filings published either side of a split.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **decimal.Decimal** |  | 
**adjustment_factor** | **decimal.Decimal** |  | 
**split_event_ids** | **List[int]** |  | 
**null_reason** | **str** |  | 

## Example

```python
from financial_reports_generated_client.models.companies_dividends_retrieve200_response_dividends_inner_split_adjusted import CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted from a JSON string
companies_dividends_retrieve200_response_dividends_inner_split_adjusted_instance = CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted.from_json(json)
# print the JSON string representation of the object
print(CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted.to_json())

# convert the object into a dict
companies_dividends_retrieve200_response_dividends_inner_split_adjusted_dict = companies_dividends_retrieve200_response_dividends_inner_split_adjusted_instance.to_dict()
# create an instance of CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted from a dict
companies_dividends_retrieve200_response_dividends_inner_split_adjusted_from_dict = CompaniesDividendsRetrieve200ResponseDividendsInnerSplitAdjusted.from_dict(companies_dividends_retrieve200_response_dividends_inner_split_adjusted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


