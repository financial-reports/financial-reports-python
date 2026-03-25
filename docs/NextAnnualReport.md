# NextAnnualReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | The earliest expected date for the report release. | 
**end_date** | **date** | The latest expected date for the report release. | 
**confidence** | **int** | Confidence score (0-100) based on historical consistency. | 
**is_overdue** | **bool** | True if the current date is past the predicted window. | 

## Example

```python
from financial_reports_generated_client.models.next_annual_report import NextAnnualReport

# TODO update the JSON string below
json = "{}"
# create an instance of NextAnnualReport from a JSON string
next_annual_report_instance = NextAnnualReport.from_json(json)
# print the JSON string representation of the object
print(NextAnnualReport.to_json())

# convert the object into a dict
next_annual_report_dict = next_annual_report_instance.to_dict()
# create an instance of NextAnnualReport from a dict
next_annual_report_from_dict = NextAnnualReport.from_dict(next_annual_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


