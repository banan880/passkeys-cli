# Passkeys CLI - Production-Ready Password Manager

A secure, production-level command-line password manager with encryption, validation, and enhanced user experience.

## Features

- 🔐 **Secure Encryption**: AES-GCM encryption with Scrypt key derivation
- ✅ **Input Validation**: Comprehensive validation for all user inputs
- 🔑 **Password Confirmation**: Mandatory password confirmation for create/update operations
- 🎨 **Enhanced CLI**: Beautiful, colorized terminal interface
- 🛡️ **Production-Ready**: Robust error handling and transaction management
- 🔒 **Master Password**: Argon2 hashed master password protection
- 📊 **Formatted Output**: Clean, readable table displays
- 🎲 **Password Generator**: Cryptographically secure password generation

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=your_postgresql_connection_string
   ```

3. **Set up database schema:**
   ```sql
   CREATE TABLE master_key (
       id INT PRIMARY KEY,
       password_hash TEXT NOT NULL,
       salt BYTEA NOT NULL
   );

   CREATE TABLE vault (
       id UUID PRIMARY KEY,
       service TEXT NOT NULL,
       username TEXT NOT NULL,
       secret BYTEA NOT NULL,
       created_at TIMESTAMP DEFAULT now(),
       updated_at TIMESTAMP DEFAULT now()
   );
   ```

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **View passkeys** - List all stored passkeys with formatted table display
2. **Create passkey** - Add a new passkey (requires password confirmation)
3. **Update passkey** - Update an existing passkey (requires password confirmation)
4. **Delete passkey** - Remove a passkey (requires confirmation)
5. **Generate password** - Generate a secure random password
6. **Exit** - Exit the application

## Production Features

### Input Validation
- Service names: 2-100 characters, alphanumeric + special chars
- Usernames: 1-255 characters
- Passwords: Minimum 8 characters, maximum 1000 characters
- Entry IDs: Valid UUID format validation

### Security
- AES-GCM encryption for all secrets
- Scrypt key derivation (n=2^14, r=8, p=1)
- Argon2 password hashing for master password
- Secure random password generation
- Input sanitization and validation

### Error Handling
- Comprehensive exception handling
- Clear, user-friendly error messages
- Database transaction rollback on errors
- Graceful handling of invalid inputs

### User Experience
- Colorized terminal output
- Formatted tables and menus
- Clear success/error/warning messages
- Password confirmation for critical operations
- Confirmation prompts for destructive actions

## Project Structure

```
passkeys/
├── main.py          # CLI entry point with enhanced UI
├── auth.py          # Master password logic with validation
├── crypto.py        # Encryption/decryption utilities
├── db.py            # Database connection management
├── vault.py         # CRUD operations with validation
├── generator.py     # Secure password generation
├── validation.py    # Input validation utilities
├── ui.py            # Enhanced CLI UI components
├── config.py        # Environment configuration
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Security Best Practices

1. **Master Password**: Choose a strong master password (minimum 8 characters)
2. **Database Security**: Use secure database credentials and connection strings
3. **Environment Variables**: Never commit `.env` files to version control
4. **Backup**: Regularly backup your database
5. **Access Control**: Restrict file permissions on sensitive files

## Error Codes

- `INVALID_ENTRY_ID`: Entry ID format is invalid
- `ENTRY_NOT_FOUND`: Requested entry does not exist
- `MASTER_PASSWORD_MISMATCH`: Master password verification failed
- `MASTER_NOT_SET`: Master password has not been configured

## License

See the [LICENSE](LICENSE) file for details.
