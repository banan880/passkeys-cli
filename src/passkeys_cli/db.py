"""
Database connection management.
Provides connection pooling and error handling for PostgreSQL/Neon database.
"""
import psycopg
from contextlib import contextmanager
from config import DATABASE_URL


@contextmanager
def get_conn():
    """
    Get a database connection with automatic cleanup.
    
    Yields:
        Database connection object
        
    Raises:
        RuntimeError: If connection fails
    """
    conn = None
    try:
        if not DATABASE_URL:
            raise RuntimeError("DATABASE_URL is not configured")
        
        conn = psycopg.connect(DATABASE_URL)
        yield conn
        conn.commit()
    except psycopg.Error as e:
        if conn:
            conn.rollback()
        raise RuntimeError(f"Database error: {str(e)}")
    except Exception as e:
        if conn:
            conn.rollback()
        raise RuntimeError(f"Unexpected database error: {str(e)}")
    finally:
        if conn:
            conn.close()
