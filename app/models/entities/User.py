"""User entity with type hints and improved structure."""

from datetime import datetime
from typing import Optional
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    """Represents a user in the Everkind system.
    
    Attributes:
        id: Unique identifier for the user
        username: User's login username
        password: Hashed password
        role_id: Role identifier (1=pending, 2=admin, 3+=occupant/guest)
        created_at: Timestamp when user was created
        updated_at: Timestamp of last update
    """
    
    def __init__(
        self,
        id: int,
        username: str,
        password: str,
        role_id: Optional[int],
        created_at: Optional[datetime],
        updated_at: Optional[datetime]
    ) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.role_id = role_id
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def validate_password(encrypted_password: str, password: str) -> bool:
        """Validate a password against its hash.
        
        Args:
            encrypted_password: The hashed password to check against
            password: The plain text password to validate
            
        Returns:
            True if password matches, False otherwise
        """
        return check_password_hash(encrypted_password, password)
    
    # Backwards compatibility alias
    @classmethod
    def validatePassword(cls, encrypted_password: str, password: str) -> bool:
        """Deprecated: Use validate_password instead."""
        return cls.validate_password(encrypted_password, password)
    
    @property
    def is_admin(self) -> bool:
        """Check if user has admin privileges."""
        return self.role_id == 2
    
    @property
    def is_pending(self) -> bool:
        """Check if user is pending onboarding."""
        return self.role_id == 1
    
    @property
    def is_occupant(self) -> bool:
        """Check if user is an occupant."""
        return self.role_id is not None and self.role_id >= 3
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', role_id={self.role_id})>"
