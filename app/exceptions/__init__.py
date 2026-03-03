"""Custom exception classes for Everkind application."""

from typing import Optional


class EverkindException(Exception):
    """Base exception for all Everkind errors."""
    
    def __init__(self, message: str, details: Optional[str] = None) -> None:
        self.message = message
        self.details = details
        super().__init__(self.message)
    
    def __str__(self) -> str:
        if self.details:
            return f"{self.message}: {self.details}"
        return self.message


class DatabaseError(EverkindException):
    """Raised when a database operation fails."""
    pass


class UserNotFoundError(EverkindException):
    """Raised when a user cannot be found."""
    
    def __init__(self, identifier: str) -> None:
        super().__init__(
            message="User not found",
            details=f"No user exists with identifier: {identifier}"
        )


class DuplicateUserError(EverkindException):
    """Raised when attempting to create a user that already exists."""
    
    def __init__(self, username: str) -> None:
        super().__init__(
            message="User already exists",
            details=f"A user with username '{username}' already exists"
        )


class AuthenticationError(EverkindException):
    """Raised when authentication fails."""
    pass


class InvalidPasswordError(AuthenticationError):
    """Raised when password validation fails."""
    
    def __init__(self) -> None:
        super().__init__(message="Invalid password")


class PasswordMismatchError(AuthenticationError):
    """Raised when password confirmation doesn't match."""
    
    def __init__(self) -> None:
        super().__init__(message="Passwords do not match")


class RoomNotFoundError(EverkindException):
    """Raised when a room cannot be found."""
    
    def __init__(self, room_id: int) -> None:
        super().__init__(
            message="Room not found",
            details=f"No room exists with ID: {room_id}"
        )


class RoomUnavailableError(EverkindException):
    """Raised when attempting to book an unavailable room."""
    
    def __init__(self, room_id: int) -> None:
        super().__init__(
            message="Room unavailable",
            details=f"Room {room_id} is not available for booking"
        )


class ValidationError(EverkindException):
    """Raised when input validation fails."""
    pass


class PermissionDeniedError(EverkindException):
    """Raised when user lacks required permissions."""
    
    def __init__(self, action: str) -> None:
        super().__init__(
            message="Permission denied",
            details=f"You do not have permission to: {action}"
        )
