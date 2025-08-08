from typing import Optional

from src.utils.client.http import HTTPClient


class HTMLClient(HTTPClient):
    def __init__(
        self, 
        base_url: str, 
        endpoint: str ='', 
        params: Optional[dict] = None,
        payload: Optional[dict] = None
        ):
        super().__init__(
            base_url=base_url,
            endpoint=endpoint,
            params=params,
            payload=payload
        )
        
    async def get(self) -> str:
        response = await super().get()
        data = await response.text()
        return data
        
    async def post(self) -> str:
        response = await super().post()
        data = await response.text()
        return data
