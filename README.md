# Financial Reports Python SDK

Official Python SDK for the Financial Reports API. Access European financial filings and company data programmatically.

## Installation

```bash
pip install financial-reports
```

## Quick Start

```python
import asyncio
from financial_reports import FinancialReportsClient

async def main():
    # Initialize client with API key
    client = FinancialReportsClient(api_key="your-api-key")
    
    try:
        # Get filings for a specific company
        filings = await client.list_filings(company_isin="FR0000073298")
        print(f"Found {filings['count']} filings")
        
        # Get German companies
        companies = await client.list_companies(countries="de")
        print(f"Found {companies['count']} German companies")
        
        # Use utility functions
        sap_isin = await client.get_primary_isin_by_name("SAP")
        print(f"SAP ISIN: {sap_isin}")
        
    finally:
        await client.close()

# Run the async function
asyncio.run(main())
```

## Features

- Full async/await support using aiohttp
- Complete coverage of API endpoints:
  - Filings (list, get)
  - Companies (list, get)
  - Filing Types (list, get)
  - Sources (list, get)
  - Sectors (list, get)
  - Industry Groups (list, get)
  - Industries (list, get)
  - Sub-Industries (list, get)
- Utility functions for company lookup
- Built-in pagination handling
- Proper error handling
- Type hints for better IDE integration

## Authentication

The client requires an API key that can be provided in two ways:

1. Environment variable:
```bash
export FINANCIAL_REPORTS_API_KEY="your-api-key"
```

2. Direct initialization:
```python
client = FinancialReportsClient(api_key="your-api-key")
```

## API Reference

### Filings

```python
# List filings with filters
filings = await client.list_filings(
    company_isin="FR0000073298",
    countries="de",
    language="en",
    added_to_platform_from="2024-01-01",
    page=1,
    page_size=50
)

# Get specific filing
filing = await client.get_filing(filing_id=123)
```

### Companies

```python
# List companies with filters
companies = await client.list_companies(
    countries="de",
    sector=45,  # Technology
    page=1,
    page_size=50
)

# Get specific company
company = await client.get_company(company_id=456)

# Utility functions
isin = await client.get_primary_isin_by_name("SAP")
ticker = await client.get_ticker_by_name("SAP")
```

### Industries & Sectors

```python
# List all sectors
sectors = await client.list_sectors()

# Get industry groups in a sector
groups = await client.list_industry_groups()

# Get specific industry
industry = await client.get_industry(industry_id=789)
```

## Error Handling

The client includes built-in error handling for common scenarios:

```python
try:
    filings = await client.list_filings()
except ValueError as e:
    if "Invalid API key" in str(e):
        print("Authentication failed")
    elif "Insufficient permissions" in str(e):
        print("API key doesn't have required permissions")
    else:
        print(f"API error: {e}")
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/financial-reports/financial-reports-python.git
cd financial-reports-python
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

## License

MIT License. See LICENSE file for details.
