# PaginatedSecurityListingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SecurityListing]**](SecurityListing.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_security_listing_list import PaginatedSecurityListingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSecurityListingList from a JSON string
paginated_security_listing_list_instance = PaginatedSecurityListingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSecurityListingList.to_json())

# convert the object into a dict
paginated_security_listing_list_dict = paginated_security_listing_list_instance.to_dict()
# create an instance of PaginatedSecurityListingList from a dict
paginated_security_listing_list_from_dict = PaginatedSecurityListingList.from_dict(paginated_security_listing_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


