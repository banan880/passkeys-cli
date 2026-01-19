import uuid
from db import get_conn
from crypto import encrypt, decrypt
from validation import validate_service, validate_username, validate_password, validate_entry_id, ValidationError


def create_entry(service, username, secret, key):
    """
    Create a new vault entry with validation.
    
    Args:
        service: Service name (validated)
        username: Username (validated)
        secret: Password/secret (validated)
        key: Encryption key
        
    Raises:
        ValidationError: If validation fails
        RuntimeError: If database operation fails
    """
    # Validate inputs
    service = validate_service(service)
    username = validate_username(username)
    secret = validate_password(secret)
    
    encrypted = encrypt(secret, key)

    try:
        with get_conn() as conn:
            conn.execute(
                """
                INSERT INTO vault (id, service, username, secret)
                VALUES (%s, %s, %s, %s)
                """,
                (uuid.uuid4(), service, username, encrypted),
            )
            conn.commit()
    except Exception as e:
        raise RuntimeError(f"Failed to create entry: {str(e)}")


def list_entries(key):
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT id, service, username, secret FROM vault"
        ).fetchall()

    results = []
    for r in rows:
        results.append({
            "id": r[0],
            "service": r[1],
            "username": r[2],
            "secret": decrypt(r[3], key),
        })

    return results


def delete_entry(entry_id):
    """
    Delete a vault entry by ID.
    
    Args:
        entry_id: Entry ID (validated UUID)
        
    Raises:
        ValidationError: If entry ID is invalid
        RuntimeError: If entry not found or deletion fails
    """
    entry_uuid = validate_entry_id(entry_id)
    
    try:
        with get_conn() as conn:
            result = conn.execute("DELETE FROM vault WHERE id = %s", (entry_uuid,))
            conn.commit()
            
            if result.rowcount == 0:
                raise RuntimeError("ENTRY_NOT_FOUND")
    except RuntimeError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to delete entry: {str(e)}")
        

def list_entries_metadata():
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT id, service, username FROM vault"
        ).fetchall()

    return [
        {"id": r[0], "service": r[1], "username": r[2]}
        for r in rows
    ]

def entry_exists(entry_id: str) -> bool:
    """
    Check if an entry exists in the vault.
    
    Args:
        entry_id: Entry ID to check
        
    Returns:
        True if entry exists, False otherwise
    """
    try:
        entry_uuid = validate_entry_id(entry_id)
        with get_conn() as conn:
            row = conn.execute(
                "SELECT 1 FROM vault WHERE id = %s",
                (entry_uuid,),
            ).fetchone()
        return row is not None
    except (ValidationError, RuntimeError):
        return False


def get_entry_secret(entry_id: str, key: bytes) -> str:
    """
    Get the decrypted secret for an entry.
    
    Args:
        entry_id: Entry ID (validated UUID)
        key: Decryption key
        
    Returns:
        Decrypted secret string
        
    Raises:
        ValidationError: If entry ID is invalid
        RuntimeError: If entry not found or decryption fails
    """
    entry_uuid = validate_entry_id(entry_id)

    try:
        with get_conn() as conn:
            row = conn.execute(
                "SELECT secret FROM vault WHERE id = %s",
                (entry_uuid,),
            ).fetchone()

        if not row:
            raise RuntimeError("ENTRY_NOT_FOUND")

        return decrypt(row[0], key)
    except RuntimeError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve entry: {str(e)}")

def update_entry(entry_id, service, username, secret, key):
    """
    Update a vault entry with validation.
    
    Args:
        entry_id: Entry ID (validated UUID)
        service: Service name (validated)
        username: Username (validated)
        secret: Password/secret (validated)
        key: Encryption key
        
    Raises:
        ValidationError: If validation fails
        RuntimeError: If entry not found or update fails
    """
    # Validate inputs
    entry_uuid = validate_entry_id(entry_id)
    service = validate_service(service)
    username = validate_username(username)
    secret = validate_password(secret)
    
    encrypted = encrypt(secret, key)

    try:
        with get_conn() as conn:
            result = conn.execute(
                """
                UPDATE vault
                SET service = %s,
                    username = %s,
                    secret = %s,
                    updated_at = now()
                WHERE id = %s
                """,
                (service, username, encrypted, entry_uuid),
            )
            conn.commit()

        if result.rowcount == 0:
            raise RuntimeError("ENTRY_NOT_FOUND")
    except RuntimeError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to update entry: {str(e)}")

