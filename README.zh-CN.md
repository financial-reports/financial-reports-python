[English](README.md) | 简体中文

# FinancialFilings Python SDK

[FinancialFilings API](https://financialfilings.com) 的官方 Python 客户端。

通过代码访问一个全面的数据库，涵盖上市公司公告、公司信息和行业分类。

本文是英文 [README.md](README.md) 的中文版。两者如有出入，以英文版为准。

## 安装

```bash
pip install financial-reports-generated-client
```

## 快速开始

SDK 的设计力求简单直观，基于 `asyncio` 实现高性能的数据获取。

### 1. 初始化客户端

可以直接传入 API 密钥，也可以设置环境变量 `FR_API_KEY`。

```python
import asyncio
from financial_reports_generated_client import FinancialReports

async def main():
    # Context manager automatically handles cleanup
    async with FinancialReports(api_key="YOUR_API_KEY") as client:
        
        # --- Example 1: List Filings ---
        # Get the latest filings, searching for "Volkswagen"
        filings = await client.filings.list(
            search="Volkswagen", 
            ordering="-release_datetime",
            page_size=5
        )
        
        for filing in filings.results:
            print(f"{filing.release_datetime}: {filing.title} ({filing.company.name})")

        # --- Example 2: Get Company Details ---
        # Fetch detailed profile for a specific company ID
        company = await client.companies.retrieve(id=123)
        print(f"Company: {company.name}, Country: {company.country_code}")

if __name__ == "__main__":
    asyncio.run(main())
```

上面的示例做了两件事：

- **示例 1：列出公告。** 搜索 “Volkswagen”，按发布时间倒序获取最新的 5 份公告。
- **示例 2：获取公司详情。** 按公司 ID 获取该公司的详细资料。

`async with` 上下文管理器会在结束时自动清理连接。

## 点数

一个 API 密钥即可访问所有端点，每次调用按点数计费：元数据和搜索、公告 Markdown 正文、标准化财务数据各有不同的点数消耗，每月提供免费点数。各端点的点数消耗：[https://financialfilings.com/developers/](https://financialfilings.com/developers/)

## 文档

* **开发者文档：** [https://financialfilings.com/developers/](https://financialfilings.com/developers/)（中文版：[https://financialfilings.com/zh-hans/developers/](https://financialfilings.com/zh-hans/developers/)）
* **完整 API 参考：** [https://financialfilings.com/developers/reference/](https://financialfilings.com/developers/reference/)
* **技术支持：** [support@financialfilings.com](mailto:support@financialfilings.com)

---
*由 FinancialFilings 工程团队生成。*
