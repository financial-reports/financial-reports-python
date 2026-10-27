# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the company. | [readonly] 
**name** | **str** | Company name. | [readonly] 
**tagline** | **str** | A short, one-liner describing the company&#39;s value proposition. | [readonly] 
**description** | **str** | A detailed description or &#39;About Us&#39; text for the company. | [readonly] 
**description_last_updated** | **datetime** | Timestamp of the last update to the company&#39;s description. | [readonly] 
**isins** | **List[str]** | ISINs associated with the company (capped at 100; use the ISIN endpoint for the full list). | [readonly] 
**isin_count** | **int** | Total number of ISINs associated with this company. | [readonly] 
**primary_isin** | **str** | The company&#39;s primary ISIN (ISO 6166), or null when no primary is designated. Equivalent to isins[0] when a primary exists. | [readonly] 
**lei** | **str** | Legal Entity Identifier (ISO 17442). | [readonly] 
**country_code** | **str** | ISO 3166-1 alpha-2 country code of the company&#39;s primary registration or headquarters. | [readonly] 
**address** | **str** | The company&#39;s primary street address. | [readonly] 
**city** | **str** | The city where the company&#39;s headquarters is located. | [readonly] 
**zip_code** | **str** | The postal or ZIP code for the company&#39;s address. | [readonly] 
**sector** | [**ISICSection**](ISICSection.md) | Company&#39;s ISIC Section classification. | [readonly] 
**industry_group** | [**ISICDivision**](ISICDivision.md) | Company&#39;s ISIC Division classification. | [readonly] 
**industry** | [**ISICGroup**](ISICGroup.md) | Company&#39;s ISIC Group classification. | [readonly] 
**sub_industry** | [**ISICClass**](ISICClass.md) | Company&#39;s ISIC Class classification. | [readonly] 
**oics** | [**CompanyOics**](CompanyOics.md) | The company&#39;s label under the Open Industry Classification Standard (OICS), an investor-oriented taxonomy served alongside ISIC. Public preview, OICS v0.3: codes and names can still change before v1.0. Null when the company has no label under the current OICS version. A change to the label (class, entity type, secondaries, basis, contested or alternate) moves the company&#39;s &#x60;date_public&#x60;, so incremental syncs by date see it; &#x60;classified_at&#x60; changing alone does not, and neither does a new OICS release renaming a node. | [readonly] 
**ir_link** | **str** | Link to the company&#39;s Investor Relations page. | [readonly] 
**homepage_link** | **str** | Link to the company&#39;s main homepage. | [readonly] 
**logo** | **str** | URL of the company&#39;s logo file. | [readonly] 
**date_public** | **date** | Date this company record was last updated on the FinancialFilings platform. This is not the IPO date: see &#x60;date_ipo&#x60; for that. | [readonly] 
**date_ipo** | **date** | Date of the company&#39;s Initial Public Offering (IPO). Returns null when the IPO date is unknown. | [readonly] 
**main_stock_exchange** | **str** | URL of the company&#39;s listing page on its main stock exchange, where known; empty for most companies. Not a MIC: exchange codes are in &#x60;listings&#x60;. | [readonly] 
**is_listed** | **bool** | Indicates if the company is currently publicly listed. | [readonly] 
**listing_status** | **str** | Canonical exchange-listing state. One of: LISTED, DELISTED, SUSPENDED, UNKNOWN. The boolean &#x60;is_listed&#x60; is derived from this (False only when DELISTED). | [readonly] 
**delisting_date** | **date** | Date the company was delisted, if known. Null while listed. | [readonly] 
**delisting_reason** | **str** | Reason for delisting when DELISTED: ACQUISITION, BANKRUPTCY, GOING_PRIVATE, REGULATORY, VOLUNTARY, EXCHANGE_TRANSFER, MATURED, OTHER. Empty string while listed. | [readonly] 
**social_facebook** | **str** | Facebook page URL. | [readonly] 
**social_instagram** | **str** | Instagram profile URL. | [readonly] 
**social_twitter** | **str** | X (Twitter) profile URL. | [readonly] 
**social_linkedin** | **str** | LinkedIn company page URL. A few omit the scheme (&#x60;linkedin.com/company/...&#x60;). | [readonly] 
**social_youtube** | **str** | YouTube channel URL. | [readonly] 
**social_tiktok** | **str** | TikTok profile URL. | [readonly] 
**social_pinterest** | **str** | Pinterest profile URL. | [readonly] 
**social_xing** | **str** | Xing company profile URL. | [readonly] 
**social_glassdoor** | **str** | Glassdoor company page URL. | [readonly] 
**year_founded** | **date** | Date the company was founded. | [readonly] 
**corporate_video_id** | **str** | Identifier for a corporate video (e.g., YouTube ID). | [readonly] 
**served_area** | **str** | Geographical area served by the company. | [readonly] 
**headcount** | **int** | Approximate number of employees. | [readonly] 
**contact_email** | **str** | General contact email address. | [readonly] 
**ticker** | **str** | Primary stock ticker symbol. | [readonly] 
**local_company_id** | **str** | Local registration or jurisdiction-specific ID (e.g., HRB 24902, CIK 123456). | [readonly] 
**shares_outstanding** | **int** | Number of the company&#39;s shares outstanding, as last reported. | [readonly] 
**designated_sponsor** | [**List[DesignatedSponsor]**](DesignatedSponsor.md) | Financial institutions that act as market makers for the company&#39;s stock. | [readonly] 
**listed_stock_exchange** | [**List[ListedStockExchange]**](ListedStockExchange.md) | A list of stock exchanges where the company is listed. | [readonly] 
**stock_index** | [**List[StockIndex]**](StockIndex.md) | A list of stock indices the company is a component of. | [readonly] 
**listings** | [**List[CompanyListing]**](CompanyListing.md) | Equity venue listings for this company (exchange + ticker), deduplicated by (MIC, ticker). Excludes warrants/options/futures/rights. Populated from per-venue identifier data; coverage expands over time. | [readonly] 
**legal_status** | **str** | The operational and legal registration status sourced from GLEIF (e.g., ACTIVE, INACTIVE). | [readonly] 
**legal_form** | [**EntityLegalForm**](EntityLegalForm.md) | The ISO 20275 Entity Legal Form sourced from GLEIF. | [readonly] 
**jurisdiction** | [**Jurisdiction**](Jurisdiction.md) | The legal jurisdiction of incorporation sourced from GLEIF. | [readonly] 
**legal_address** | **str** | The official registered legal address of the company sourced from GLEIF. | [readonly] 
**legal_city** | **str** | The city of the registered legal address sourced from GLEIF. | [readonly] 
**legal_zip_code** | **str** | The postal code of the registered legal address sourced from GLEIF. | [readonly] 
**is_merged** | **bool** | True when this company record has been retired as a duplicate and replaced by the company in &#x60;merged_into&#x60;. Retired records are excluded from the company list but remain retrievable by id so an existing integration can discover the replacement rather than receiving a bare 404. See the merges feed at /companies/merges/. | [readonly] 
**merged_into** | [**CompanyMergedInto**](CompanyMergedInto.md) | The canonical company that replaced this one, or null when this record is live. Repoint stored references to this id. | [readonly] 
**predecessors** | [**List[CompanySuccessionLink]**](CompanySuccessionLink.md) | Earlier issuers this company succeeded, e.g. the old parent before a holding-company reorganization. Each keeps the filings it issued, so the history before the change is under the predecessor&#39;s id. Empty when none is recorded. | [readonly] 
**successors** | [**List[CompanySuccessionLink]**](CompanySuccessionLink.md) | Issuers that took over from this company, e.g. a new holding company that now carries the ticker. Filings after the change are under the successor&#39;s id. Empty when none is recorded. | [readonly] 

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


