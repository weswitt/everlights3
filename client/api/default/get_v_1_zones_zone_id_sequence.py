from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.program import Program
from ...types import Response


def _get_kwargs(
    zone_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v1/zones/{zoneId}/sequence".format(
            zoneId=zone_id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Program]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Program.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Program]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Program]:
    """
    Args:
        zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Program]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Program]:
    """
    Args:
        zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Program
    """

    return sync_detailed(
        zone_id=zone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Program]:
    """
    Args:
        zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Program]
    """

    kwargs = _get_kwargs(
        zone_id=zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Program]:
    """
    Args:
        zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Program
    """

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            client=client,
        )
    ).parsed
