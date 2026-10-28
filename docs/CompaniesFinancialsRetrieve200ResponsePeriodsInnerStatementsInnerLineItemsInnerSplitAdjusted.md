# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted

The value on today's share basis: divided (per-share figures) or multiplied (share counts) by `adjustment_factor`, the product of `ratio_new / ratio_old` of every split, reverse split and bonus issue in `/companies/{id}/splits/` that took effect after the filing the value was read from was published. A filing published after a split already states the new basis, so it is not adjusted again. `adjustment_factor` `1` and no `split_event_ids`: nothing to adjust. Rights issues and spin-offs are not adjusted. `value` is null, with `null_reason`, when the filing predates our split history (2015), when two events that cannot both be right would apply, when a split that applies is not served to you, for a period-end share count or book value per share with a split between the period end and the publication, or for a standalone quarter derived from filings published either side of a split.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **decimal.Decimal** |  | 
**adjustment_factor** | **decimal.Decimal** |  | 
**split_event_ids** | **List[int]** |  | 
**null_reason** | **str** |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_split_adjusted import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_split_adjusted_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_split_adjusted_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_split_adjusted_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_split_adjusted_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_split_adjusted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


