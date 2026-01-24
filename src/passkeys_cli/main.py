import getpass
import sys
from auth import (
    master_password_exists,
    setup_master_password,
    verify_master_password,
)
from crypto import derive_key
from generator import generate_password
from vault import (
    list_entries_metadata,
    create_entry,
    delete_entry,
    get_entry_secret,
    update_entry,
    entry_exists,
)
from validation import (
    ValidationError,
    validate_service,
    validate_username,
    validate_entry_id,
)
from ui import (
    print_menu,
    print_success,
    print_error,
    print_warning,
    print_info,
    print_header,
    print_entries_table,
    get_input,
    get_password_input,
    print_banner,
    print_footer,
    Colors,
)

def main():
    """Main application entry point."""
    try:
        # Print ASCII banner
        print_banner()
        
        # Master password setup/verification
        master = get_password_input("Master password", confirm=False)
        
        if not master_password_exists():
            print_info("No master password found. Setting up new vault...")
            confirm_master = get_password_input("Confirm master password", confirm=False)
            if master != confirm_master:
                print_error("Master passwords do not match. Exiting.")
                print_footer()
                sys.exit(1)
            setup_master_password(master)
            salt = verify_master_password(master)
            print_success("Master password set successfully!")
        else:
            try:
                salt = verify_master_password(master)
                print_success("Master password verified!")
            except RuntimeError as e:
                if str(e) == "MASTER_PASSWORD_MISMATCH":
                    print_error("Master password does not match.")
                    print_footer()
                    sys.exit(1)
                else:
                    raise

        key = derive_key(master, salt)

        # Main application loop
        while True:
            print_menu()
            choice = get_input("Choose an option", required=True).strip()

            match choice:
                case "1":
                    try:
                        entries = list_entries_metadata()
                        print_entries_table(entries)
                        
                        if entries:
                            reveal = get_input("Reveal a password? (y/n)", required=False).lower()
                            if reveal == "y":
                                entry_id = get_input(
                                    "Enter Entry ID",
                                    validator=lambda x: str(validate_entry_id(x))
                                )
                                try:
                                    secret = get_entry_secret(entry_id, key)
                                    print_header("Password Revealed")
                                    print(f"{Colors.BOLD}{Colors.GREEN}Password:{Colors.RESET} {secret}")
                                    print()
                                except RuntimeError as e:
                                    if str(e) == "ENTRY_NOT_FOUND":
                                        print_error("No entry found with that ID.")
                                    else:
                                        print_error(f"Error: {str(e)}")
                    except Exception as e:
                        print_error(f"Failed to list entries: {str(e)}")
                
                case "2":
                    try:
                        print_header("Create New Passkey")
                        service = get_input("Service", validator=validate_service)
                        username = get_input("Username", validator=validate_username)
                        secret = get_password_input("Password", confirm=True)
                        
                        create_entry(service, username, secret, key)
                        print_success(f"Passkey for '{service}' created successfully!")
                    except ValidationError as e:
                        print_error(f"Validation error: {str(e)}")
                    except RuntimeError as e:
                        print_error(f"Failed to create entry: {str(e)}")
                    except Exception as e:
                        print_error(f"Unexpected error: {str(e)}")
                
                case "3":
                    try:
                        print_header("Update Passkey")
                        entry_id = get_input(
                            "Entry ID",
                            validator=lambda x: str(validate_entry_id(x))
                        )
                        
                        # Check if entry exists
                        if not entry_exists(entry_id):
                            print_error("Entry not found.")
                            continue
                        
                        service = get_input("New service (press Enter to keep current)", required=False)
                        username = get_input("New username (press Enter to keep current)", required=False)
                        
                        # Get current values if not provided
                        if not service or not username:
                            entries = list_entries_metadata()
                            current_entry = next((e for e in entries if str(e['id']) == entry_id), None)
                            if current_entry:
                                service = service or current_entry['service']
                                username = username or current_entry['username']
                        
                        service = validate_service(service)
                        username = validate_username(username)
                        
                        secret = get_password_input("New password", confirm=True)
                        
                        update_entry(entry_id, service, username, secret, key)
                        print_success("Passkey updated successfully!")
                    except ValidationError as e:
                        print_error(f"Validation error: {str(e)}")
                    except RuntimeError as e:
                        if str(e) == "ENTRY_NOT_FOUND":
                            print_error("Entry not found.")
                        else:
                            print_error(f"Failed to update entry: {str(e)}")
                    except Exception as e:
                        print_error(f"Unexpected error: {str(e)}")
                
                case "4":
                    try:
                        print_header("Delete Passkey")
                        entry_id = get_input(
                            "Entry ID",
                            validator=lambda x: str(validate_entry_id(x))
                        )
                        
                        # Confirm deletion
                        confirm = get_input(
                            f"{Colors.RED}Are you sure you want to delete this entry? (yes/no){Colors.RESET}",
                            required=True
                        ).lower()
                        
                        if confirm != "yes":
                            print_info("Deletion cancelled.")
                            continue
                        
                        delete_entry(entry_id)
                        print_success("Passkey deleted successfully!")
                    except ValidationError as e:
                        print_error(f"Validation error: {str(e)}")
                    except RuntimeError as e:
                        if str(e) == "ENTRY_NOT_FOUND":
                            print_error("Entry not found.")
                        else:
                            print_error(f"Failed to delete entry: {str(e)}")
                    except Exception as e:
                        print_error(f"Unexpected error: {str(e)}")
                
                case "5":
                    try:
                        print_header("Generate Password")
                        length_input = get_input(
                            "Password length (default: 16)",
                            required=False
                        )
                        length = int(length_input) if length_input else 16
                        
                        if length < 8 or length > 128:
                            print_warning("Length should be between 8 and 128. Using default: 16")
                            length = 16
                        
                        password = generate_password(length)
                        print(f"\n{Colors.BOLD}{Colors.GREEN}Generated Password:{Colors.RESET}")
                        print(f"{Colors.CYAN}{password}{Colors.RESET}\n")
                    except ValueError:
                        print_error("Invalid length. Using default: 16")
                        password = generate_password()
                        print(f"\n{Colors.BOLD}{Colors.GREEN}Generated Password:{Colors.RESET}")
                        print(f"{Colors.CYAN}{password}{Colors.RESET}\n")
                    except Exception as e:
                        print_error(f"Failed to generate password: {str(e)}")
                
                case "6":
                    print_header("Goodbye!")
                    print_success("Thank you for using Passkeys CLI!")
                    print_footer()
                    break
                
                case _:
                    print_error("Invalid option. Please choose 1-6.")
    
    except KeyboardInterrupt:
        print("\n")
        print_warning("Operation cancelled by user.")
        print_footer()
        sys.exit(0)
    except Exception as e:
        print_error(f"Fatal error: {str(e)}")
        print_footer()
        sys.exit(1)

if __name__ == "__main__":
    main()
