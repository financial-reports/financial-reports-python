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
        
        # Get company details
        companies = await client.list_companies(countries="de")
        print(f"Found {companies['count']} German companies")
        
    finally:
        await client.close()

asyncio.run(main())
```

## Features

- Full async/await support
- Type hints for better IDE integration
- Automatic pagination handling
- Comprehensive error handling
- Support for all API endpoints

## Documentation

For full API documentation, visit [docs.financialreports.eu](https://docs.financialreports.eu)
