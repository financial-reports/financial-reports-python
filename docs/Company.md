# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the company. | [readonly] 
**name** | **str** | Company name. | [readonly] 
**tagline** | **str** | A short, one-liner describing the company&#39;s value proposition. | [readonly] 
**isins** | **List[str]** | List of International Securities Identification Numbers (ISINs) associated with the company. | [readonly] 
**lei** | **str** | Legal Entity Identifier (ISO 17442). | [readonly] 
**country_code** | **str** | ISO 3166-1 alpha-2 country code of the company&#39;s primary registration or headquarters. | [readonly] 
**sector** | [**ISICSection**](ISICSection.md) | Company&#39;s ISIC Section classification. | [readonly] 
**industry_group** | [**ISICDivision**](ISICDivision.md) | Company&#39;s ISIC Division classification. | [readonly] 
**industry** | [**ISICGroup**](ISICGroup.md) | Company&#39;s ISIC Group classification. | [readonly] 
**sub_industry** | [**ISICClass**](ISICClass.md) | Company&#39;s ISIC Class classification. | [readonly] 
**ir_link** | **str** | Link to the company&#39;s Investor Relations page. | [readonly] 
**homepage_link** | **str** | Link to the company&#39;s main homepage. | [readonly] 
**date_public** | **date** | Date the company first became public. | [readonly] 
**date_ipo** | **date** | Date of the company&#39;s Initial Public Offering. | [readonly] 
**main_stock_exchange** | **str** | Primary stock exchange where the company is listed. | [readonly] 
**social_facebook** | **str** | Facebook profile/page identifier. | [readonly] 
**social_instagram** | **str** | Instagram profile identifier. | [readonly] 
**social_twitter** | **str** | Twitter handle (without @). | [readonly] 
**social_linkedin** | **str** | LinkedIn company page identifier/URL path. | [readonly] 
**social_youtube** | **str** | YouTube channel identifier. | [readonly] 
**social_tiktok** | **str** | TikTok profile identifier. | [readonly] 
**social_pinterest** | **str** | Pinterest profile identifier. | [readonly] 
**social_xing** | **str** | Xing company profile identifier. | [readonly] 
**social_glassdoor** | **str** | Glassdoor company identifier. | [readonly] 
**year_founded** | **date** | Date the company was founded. | [readonly] 
**corporate_video_id** | **str** | Identifier for a corporate video (e.g., YouTube ID). | [readonly] 
**served_area** | **str** | Geographical area served by the company. | [readonly] 
**headcount** | **int** | Approximate number of employees. | [readonly] 
**contact_email** | **str** | General contact email address. | [readonly] 
**ticker** | **str** | Primary stock ticker symbol. | [readonly] 
**is_listed** | **bool** | Indicates if the company is currently publicly listed. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


