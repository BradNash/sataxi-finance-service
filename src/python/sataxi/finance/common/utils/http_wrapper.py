import logging
from enum import IntEnum
from typing import Dict

from tornado.httpclient import HTTPRequest, AsyncHTTPClient, HTTPError


class ReturnType(IntEnum):
    FULL = 0
    BODY = 1


class HttpWrapper:
    def __init__(self, headers: Dict[str, str]):
        super().__init__()
        self.headers = headers

    async def send_http_request(
        self, method: str, url: str, body: str, timeout: int, return_type: ReturnType
    ):
        try:
            client = AsyncHTTPClient()
            req = HTTPRequest(
                method=method,
                url=url,
                body=body,
                headers=self.headers,
                connect_timeout=timeout,
            )
            response = await client.fetch(req)
            if return_type == ReturnType.BODY:
                return response.body
            return response
        except HTTPError as http_error:
            log_string = f"Http request to [{req.url}] failed with [{http_error}]"
            log_string += f" using payload [{req.body}]" if req.method != "GET" else ""
            logging.error(log_string)
            raise http_error
