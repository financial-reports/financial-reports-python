# coding: utf-8

"""
    Financial Reports API

    API for accessing company filings, financial data, industry classifications, and related information.

    The version of the OpenAPI document: 1.0.0
    Contact: api@financialreports.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from financial_reports_generated_client.models.paginated_sub_industry_list import PaginatedSubIndustryList
from financial_reports_generated_client.models.sub_industry import SubIndustry

from financial_reports_generated_client.api_client import ApiClient, RequestSerialized
from financial_reports_generated_client.api_response import ApiResponse
from financial_reports_generated_client.rest import RESTResponseType


class SubIndustriesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def sub_industries_list(
        self,
        code: Optional[StrictStr] = None,
        code__iexact: Optional[StrictStr] = None,
        code__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        industry_code: Annotated[Optional[StrictStr], Field(description="Filter by parent Industry GICS code (e.g., 101010)")] = None,
        industry_code_in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        industry_group_code: Annotated[Optional[StrictStr], Field(description="Filter by grandparent Industry Group GICS code (e.g., 1010)")] = None,
        name__icontains: Optional[StrictStr] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="A search term.")] = None,
        sector_code: Annotated[Optional[StrictStr], Field(description="Filter by great-grandparent Sector GICS code (e.g., 10)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedSubIndustryList:
        """sub_industries_list

        Retrieve a list of all available GICS Sub-Industries. Can be filtered by parent industry ID.

        :param code:
        :type code: str
        :param code__iexact:
        :type code__iexact: str
        :param code__in: Multiple values may be separated by commas.
        :type code__in: List[str]
        :param industry_code: Filter by parent Industry GICS code (e.g., 101010)
        :type industry_code: str
        :param industry_code_in: Multiple values may be separated by commas.
        :type industry_code_in: List[str]
        :param industry_group_code: Filter by grandparent Industry Group GICS code (e.g., 1010)
        :type industry_group_code: str
        :param name__icontains:
        :type name__icontains: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param search: A search term.
        :type search: str
        :param sector_code: Filter by great-grandparent Sector GICS code (e.g., 10)
        :type sector_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._sub_industries_list_serialize(
            code=code,
            code__iexact=code__iexact,
            code__in=code__in,
            industry_code=industry_code,
            industry_code_in=industry_code_in,
            industry_group_code=industry_group_code,
            name__icontains=name__icontains,
            page=page,
            page_size=page_size,
            search=search,
            sector_code=sector_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedSubIndustryList",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def sub_industries_list_with_http_info(
        self,
        code: Optional[StrictStr] = None,
        code__iexact: Optional[StrictStr] = None,
        code__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        industry_code: Annotated[Optional[StrictStr], Field(description="Filter by parent Industry GICS code (e.g., 101010)")] = None,
        industry_code_in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        industry_group_code: Annotated[Optional[StrictStr], Field(description="Filter by grandparent Industry Group GICS code (e.g., 1010)")] = None,
        name__icontains: Optional[StrictStr] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="A search term.")] = None,
        sector_code: Annotated[Optional[StrictStr], Field(description="Filter by great-grandparent Sector GICS code (e.g., 10)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedSubIndustryList]:
        """sub_industries_list

        Retrieve a list of all available GICS Sub-Industries. Can be filtered by parent industry ID.

        :param code:
        :type code: str
        :param code__iexact:
        :type code__iexact: str
        :param code__in: Multiple values may be separated by commas.
        :type code__in: List[str]
        :param industry_code: Filter by parent Industry GICS code (e.g., 101010)
        :type industry_code: str
        :param industry_code_in: Multiple values may be separated by commas.
        :type industry_code_in: List[str]
        :param industry_group_code: Filter by grandparent Industry Group GICS code (e.g., 1010)
        :type industry_group_code: str
        :param name__icontains:
        :type name__icontains: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param search: A search term.
        :type search: str
        :param sector_code: Filter by great-grandparent Sector GICS code (e.g., 10)
        :type sector_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._sub_industries_list_serialize(
            code=code,
            code__iexact=code__iexact,
            code__in=code__in,
            industry_code=industry_code,
            industry_code_in=industry_code_in,
            industry_group_code=industry_group_code,
            name__icontains=name__icontains,
            page=page,
            page_size=page_size,
            search=search,
            sector_code=sector_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedSubIndustryList",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def sub_industries_list_without_preload_content(
        self,
        code: Optional[StrictStr] = None,
        code__iexact: Optional[StrictStr] = None,
        code__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        industry_code: Annotated[Optional[StrictStr], Field(description="Filter by parent Industry GICS code (e.g., 101010)")] = None,
        industry_code_in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        industry_group_code: Annotated[Optional[StrictStr], Field(description="Filter by grandparent Industry Group GICS code (e.g., 1010)")] = None,
        name__icontains: Optional[StrictStr] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="A search term.")] = None,
        sector_code: Annotated[Optional[StrictStr], Field(description="Filter by great-grandparent Sector GICS code (e.g., 10)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """sub_industries_list

        Retrieve a list of all available GICS Sub-Industries. Can be filtered by parent industry ID.

        :param code:
        :type code: str
        :param code__iexact:
        :type code__iexact: str
        :param code__in: Multiple values may be separated by commas.
        :type code__in: List[str]
        :param industry_code: Filter by parent Industry GICS code (e.g., 101010)
        :type industry_code: str
        :param industry_code_in: Multiple values may be separated by commas.
        :type industry_code_in: List[str]
        :param industry_group_code: Filter by grandparent Industry Group GICS code (e.g., 1010)
        :type industry_group_code: str
        :param name__icontains:
        :type name__icontains: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param search: A search term.
        :type search: str
        :param sector_code: Filter by great-grandparent Sector GICS code (e.g., 10)
        :type sector_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._sub_industries_list_serialize(
            code=code,
            code__iexact=code__iexact,
            code__in=code__in,
            industry_code=industry_code,
            industry_code_in=industry_code_in,
            industry_group_code=industry_group_code,
            name__icontains=name__icontains,
            page=page,
            page_size=page_size,
            search=search,
            sector_code=sector_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedSubIndustryList",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _sub_industries_list_serialize(
        self,
        code,
        code__iexact,
        code__in,
        industry_code,
        industry_code_in,
        industry_group_code,
        name__icontains,
        page,
        page_size,
        search,
        sector_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'code__in': 'csv',
            'industry_code_in': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if code is not None:
            
            _query_params.append(('code', code))
            
        if code__iexact is not None:
            
            _query_params.append(('code__iexact', code__iexact))
            
        if code__in is not None:
            
            _query_params.append(('code__in', code__in))
            
        if industry_code is not None:
            
            _query_params.append(('industry_code', industry_code))
            
        if industry_code_in is not None:
            
            _query_params.append(('industry_code_in', industry_code_in))
            
        if industry_group_code is not None:
            
            _query_params.append(('industry_group_code', industry_group_code))
            
        if name__icontains is not None:
            
            _query_params.append(('name__icontains', name__icontains))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('page_size', page_size))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if sector_code is not None:
            
            _query_params.append(('sector_code', sector_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/sub-industries/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    async def sub_industries_retrieve(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubIndustry:
        """sub_industries_retrieve

        Retrieve details for a single GICS Sub-Industry by its primary key.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._sub_industries_retrieve_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubIndustry",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def sub_industries_retrieve_with_http_info(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubIndustry]:
        """sub_industries_retrieve

        Retrieve details for a single GICS Sub-Industry by its primary key.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._sub_industries_retrieve_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubIndustry",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def sub_industries_retrieve_without_preload_content(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """sub_industries_retrieve

        Retrieve details for a single GICS Sub-Industry by its primary key.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._sub_industries_retrieve_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubIndustry",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _sub_industries_retrieve_serialize(
        self,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/sub-industries/{id}/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


