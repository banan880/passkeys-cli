"""
Password generation utilities.
Provides secure password generation with customizable length and character sets.
"""
import secrets
import string


def generate_password(length: int = 16) -> str:
    """
    Generate a cryptographically secure random password.
    
    Args:
        length: Desired password length (default: 16, min: 8, max: 128)
        
    Returns:
        Generated password string
        
    Raises:
        ValueError: If length is out of valid range
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    if length > 128:
        raise ValueError("Password length must be at most 128 characters")
    
    # Use a comprehensive character set
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure password contains at least one character from each category
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"),
    ]
    
    # Fill the rest randomly
    password.extend(secrets.choice(alphabet) for _ in range(length - 4))
    
    # Shuffle to avoid predictable pattern
    secrets.SystemRandom().shuffle(password)
    
    return "".join(password)
