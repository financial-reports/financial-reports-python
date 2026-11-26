# CompaniesSeriesRetrieve200ResponseObservationsInner

One value: the same shape as a fact's, without `label` and `statement`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **decimal.Decimal** | Exact decimal string, in &#x60;unit&#x60;, unscaled. | 
**unit** | **str** | ISO currency code, &#x60;shares&#x60;, &#x60;pure&#x60;, or a ratio such as &#x60;EUR/shares&#x60;. | [optional] 
**period** | [**CompaniesSeriesList200ResponseResultsInnerLatestPeriod**](CompaniesSeriesList200ResponseResultsInnerLatestPeriod.md) |  | 
**method** | **str** | Where the value was read: &#x60;xbrl&#x60; and &#x60;structured&#x60; are the company&#39;s own tagged or structured statements; &#x60;llm&#x60; was read from the report&#39;s text and tables. | 
**status** | **str** |  | 
**decimals** | **int** | The precision the company tagged (&#x60;-6&#x60; &#x3D; millions). | [optional] 
**source** | [**CompaniesSeriesList200ResponseResultsInnerLatestSource**](CompaniesSeriesList200ResponseResultsInnerLatestSource.md) |  | 
**as_printed** | [**CompaniesSeriesList200ResponseResultsInnerLatestAsPrinted**](CompaniesSeriesList200ResponseResultsInnerLatestAsPrinted.md) |  | [optional] 
**version** | **int** | 1 for the first value reported for the period, higher once a later filing restated it. | [optional] 
**restated** | **bool** |  | [optional] 
**previous_value** | **decimal.Decimal** |  | [optional] 
**restatement_evidence** | **str** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_series_retrieve200_response_observations_inner import CompaniesSeriesRetrieve200ResponseObservationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSeriesRetrieve200ResponseObservationsInner from a JSON string
companies_series_retrieve200_response_observations_inner_instance = CompaniesSeriesRetrieve200ResponseObservationsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesSeriesRetrieve200ResponseObservationsInner.to_json())

# convert the object into a dict
companies_series_retrieve200_response_observations_inner_dict = companies_series_retrieve200_response_observations_inner_instance.to_dict()
# create an instance of CompaniesSeriesRetrieve200ResponseObservationsInner from a dict
companies_series_retrieve200_response_observations_inner_from_dict = CompaniesSeriesRetrieve200ResponseObservationsInner.from_dict(companies_series_retrieve200_response_observations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


