from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sequence import Sequence
from ...types import Response


def _get_kwargs(
    sequence_id: str,
    *,
    json_body: Sequence,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/v1/sequences/{sequenceId}".format(
            sequenceId=sequence_id,
        ),
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Sequence]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Sequence.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Sequence]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sequence_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Sequence,
) -> Response[Sequence]:
    """
    Args:
        sequence_id (str):
        json_body (Sequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Sequence]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sequence_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Sequence,
) -> Optional[Sequence]:
    """
    Args:
        sequence_id (str):
        json_body (Sequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Sequence
    """

    return sync_detailed(
        sequence_id=sequence_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    sequence_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Sequence,
) -> Response[Sequence]:
    """
    Args:
        sequence_id (str):
        json_body (Sequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Sequence]
    """

    kwargs = _get_kwargs(
        sequence_id=sequence_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sequence_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Sequence,
) -> Optional[Sequence]:
    """
    Args:
        sequence_id (str):
        json_body (Sequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Sequence
    """

    return (
        await asyncio_detailed(
            sequence_id=sequence_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
