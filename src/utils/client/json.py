from typing import Optional, Union

from src.utils.client.http import HTTPClient



class JSONClient(HTTPClient):
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
            payload=payload,
        )
        
    async def get(self) -> Union[list, dict, None]:
        response = await super().get()
        if response.status == 200:
            return await response.json()
        return None
        
    async def post(self) -> Union[list, dict, None]:
        response = await super().get()
        if response.status == 200:
            return await response.json()
        return None
