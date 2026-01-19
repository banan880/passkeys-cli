"""
Master password authentication and management.
Handles master password setup, verification, and salt management.
"""
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from db import get_conn
import os

ph = PasswordHasher()


def master_password_exists() -> bool:
    """
    Check if a master password has been set.
    
    Returns:
        True if master password exists, False otherwise
    """
    try:
        with get_conn() as conn:
            row = conn.execute(
                "SELECT 1 FROM master_key WHERE id = 1"
            ).fetchone()
        return row is not None
    except Exception as e:
        raise RuntimeError(f"Failed to check master password: {str(e)}")


def setup_master_password(password: str):
    """
    Set up the master password for the vault.
    
    Args:
        password: Master password to set
        
    Raises:
        RuntimeError: If password setup fails or master password already exists
    """
    if not password:
        raise RuntimeError("Master password cannot be empty")
    
    if len(password) < 8:
        raise RuntimeError("Master password must be at least 8 characters long")
    
    if master_password_exists():
        raise RuntimeError("Master password already exists")
    
    try:
        password_hash = ph.hash(password)
        salt = os.urandom(16)

        with get_conn() as conn:
            conn.execute(
                "INSERT INTO master_key (id, password_hash, salt) VALUES (1, %s, %s)",
                (password_hash, salt),
            )
            conn.commit()
    except Exception as e:
        raise RuntimeError(f"Failed to setup master password: {str(e)}")


def verify_master_password(password: str) -> bytes:
    """
    Verify the master password and return the salt.
    
    Args:
        password: Master password to verify
        
    Returns:
        Salt bytes for key derivation
        
    Raises:
        RuntimeError: If master password is not set or verification fails
    """
    if not password:
        raise RuntimeError("Master password cannot be empty")
    
    try:
        with get_conn() as conn:
            row = conn.execute(
                "SELECT password_hash, salt FROM master_key WHERE id = 1"
            ).fetchone()

        if not row:
            raise RuntimeError("MASTER_NOT_SET")

        password_hash, salt = row

        try:
            ph.verify(password_hash, password)
        except VerifyMismatchError:
            raise RuntimeError("MASTER_PASSWORD_MISMATCH")

        return salt
    except RuntimeError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to verify master password: {str(e)}")
