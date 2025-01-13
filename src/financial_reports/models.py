from typing import Any, TypedDict

class Filing(TypedDict):
    id: int
    company: dict[str, Any]
    filing_type: dict[str, str]
    language: dict[str, str]
    title: str
    added_to_platform: str
    updated_date: str
    dissemination_datetime: str
    release_datetime: str
    source: dict[str, str]
    document: str

class Sector(TypedDict):
    code: str
    name: str

class IndustryGroup(TypedDict):
    code: str
    name: str
    sector: Sector

class Industry(TypedDict):
    code: str
    name: str
    industry_group: IndustryGroup

class SubIndustry(TypedDict):
    code: str
    name: str
    industry: Industry

class Company(TypedDict):
    id: int
    name: str
    isins: list[str]
    lei: str
    country: str
    sector: Sector
    industry_group: IndustryGroup
    industry: Industry
    sub_industry: SubIndustry
    ir_link: str
    homepage_link: str
    date_public: str
    date_ipo: str
    main_stock_exchange: str
    social_facebook: str | None
    social_instagram: str | None
    social_twitter: str | None
    social_linkedin: str | None
    social_youtube: str | None
    social_tiktok: str | None
    social_pinterest: str | None
