"""
Input validation utilities for the Passkeys CLI application.
Provides production-level validation for all user inputs.
"""
import re
import uuid
from typing import Optional


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_service(service: str) -> str:
    """
    Validate service name.
    
    Args:
        service: Service name to validate
        
    Returns:
        Sanitized service name
        
    Raises:
        ValidationError: If service name is invalid
    """
    if not service:
        raise ValidationError("Service name cannot be empty")
    
    service = service.strip()
    
    if len(service) < 2:
        raise ValidationError("Service name must be at least 2 characters long")
    
    if len(service) > 100:
        raise ValidationError("Service name must be less than 100 characters")
    
    # Allow alphanumeric, spaces, hyphens, underscores, and common special chars
    if not re.match(r'^[a-zA-Z0-9\s\-_.,!@#$%&*()]+$', service):
        raise ValidationError("Service name contains invalid characters")
    
    return service


def validate_username(username: str) -> str:
    """
    Validate username.
    
    Args:
        username: Username to validate
        
    Returns:
        Sanitized username
        
    Raises:
        ValidationError: If username is invalid
    """
    if not username:
        raise ValidationError("Username cannot be empty")
    
    username = username.strip()
    
    if len(username) < 1:
        raise ValidationError("Username cannot be empty")
    
    if len(username) > 255:
        raise ValidationError("Username must be less than 255 characters")
    
    return username


def validate_password(password: str, min_length: int = 8) -> str:
    """
    Validate password.
    
    Args:
        password: Password to validate
        min_length: Minimum password length (default: 8)
        
    Returns:
        Password string
        
    Raises:
        ValidationError: If password is invalid
    """
    if not password:
        raise ValidationError("Password cannot be empty")
    
    if len(password) < min_length:
        raise ValidationError(f"Password must be at least {min_length} characters long")
    
    if len(password) > 1000:
        raise ValidationError("Password is too long (maximum 1000 characters)")
    
    return password


def validate_entry_id(entry_id: str) -> uuid.UUID:
    """
    Validate entry ID (UUID).
    
    Args:
        entry_id: Entry ID to validate
        
    Returns:
        UUID object
        
    Raises:
        ValidationError: If entry ID is invalid
    """
    if not entry_id:
        raise ValidationError("Entry ID cannot be empty")
    
    entry_id = entry_id.strip()
    
    try:
        return uuid.UUID(entry_id)
    except ValueError:
        raise ValidationError("Invalid entry ID format. Must be a valid UUID.")


def sanitize_input(value: str, max_length: Optional[int] = None) -> str:
    """
    Sanitize user input by stripping whitespace and optionally limiting length.
    
    Args:
        value: Input value to sanitize
        max_length: Optional maximum length
        
    Returns:
        Sanitized string
    """
    if not isinstance(value, str):
        raise ValidationError("Input must be a string")
    
    sanitized = value.strip()
    
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized


def confirm_password_match(password: str, confirm_password: str) -> bool:
    """
    Check if password and confirmation password match.
    
    Args:
        password: Original password
        confirm_password: Confirmation password
        
    Returns:
        True if passwords match
        
    Raises:
        ValidationError: If passwords don't match
    """
    if password != confirm_password:
        raise ValidationError("Passwords do not match")
    return True
