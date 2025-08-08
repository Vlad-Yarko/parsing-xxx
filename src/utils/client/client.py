from abc import ABC, abstractmethod
from functools import wraps


class Client(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError
    
    
def client_session(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        session_was_already_open = self.client.session is not None and not self.client.session.closed
        if not session_was_already_open:
            await self.client.open_session()
        try:
            return await func(self, *args, **kwargs)
        finally:
            if not session_was_already_open:
                await self.client.close_session()
    return wrapper
