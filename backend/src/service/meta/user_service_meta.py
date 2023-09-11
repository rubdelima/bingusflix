from abc import ABC, abstractmethod

from src.schemas.user import UserGet


class UserServiceMeta(ABC):
    @abstractmethod
    def get_item(self, item_id: str) -> UserGet:
        """Get user by id method definition"""
        pass
