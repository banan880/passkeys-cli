"""
Enhanced CLI UI utilities for better user experience.
Provides colored output, formatted tables, and clear messaging.
"""
import sys
from typing import List, Dict, Optional


class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    DARK_GRAY = '\033[90m'  # Bright black / Dark gray
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'


def print_success(message: str):
    """Print a success message in green."""
    print(f"{Colors.GREEN}✓ {message}{Colors.RESET}")


def print_error(message: str):
    """Print an error message in red."""
    print(f"{Colors.RED}✗ {message}{Colors.RESET}")


def print_warning(message: str):
    """Print a warning message in yellow."""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.RESET}")


def print_info(message: str):
    """Print an info message in cyan."""
    print(f"{Colors.CYAN}ℹ {message}{Colors.RESET}")


def print_header(text: str):
    """Print a header with bold formatting."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 90}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(90)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 90}{Colors.RESET}\n")


def print_separator():
    """Print a separator line."""
    print(f"{Colors.DIM}{'-' * 90}{Colors.RESET}")


def print_banner():
    """Print the main ASCII banner."""
    banner = f"""
{Colors.BOLD}{Colors.CYAN}
╔═════════════════════════════════════════════════════════════════════════╗
║                                                                         ║
║    {Colors.MAGENTA}██████╗  █████╗ ███████╗███████╗██╗  ██╗███████╗██╗   ██╗███████╗{Colors.CYAN}    ║
║    {Colors.MAGENTA}██╔══██╗██╔══██╗██╔════╝██╔════╝██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝{Colors.CYAN}    ║
║    {Colors.MAGENTA}██████╔╝███████║███████╗███████╗█████╔╝ █████╗   ╚████╔╝ ███████╗{Colors.CYAN}    ║
║    {Colors.MAGENTA}██╔═══╝ ██╔══██║╚════██║╚════██║██╔═██╗ ██╔══╝    ╚██╔╝  ╚════██║{Colors.CYAN}    ║
║    {Colors.MAGENTA}██║     ██║  ██║███████║███████║██║  ██╗███████╗   ██║   ███████║{Colors.CYAN}    ║
║    {Colors.MAGENTA}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝{Colors.CYAN}    ║
║                                                                         ║
║                         {Colors.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.CYAN}                      ║
║                    {Colors.BOLD}{Colors.GREEN} Secure Password Manager CLI {Colors.CYAN}                        ║
║                         {Colors.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.CYAN}                      ║
║                                                                         ║
║         {Colors.WHITE} Military-Grade Encryption  •  Zero-Knowledge Security{Colors.CYAN}          ║
║                                                                         ║
╚═════════════════════════════════════════════════════════════════════════╝

    {Colors.GREEN}⚡ Welcome to PassKeys{Colors.RESET} {Colors.DARK_GRAY}│{Colors.RESET} {Colors.YELLOW}Your secrets, secured.{Colors.RESET}
{Colors.RESET}
"""
    print(banner)


def print_footer():
    """Print a smaller footer banner with creator info."""
    footer = f"""
{Colors.DIM}{'─' * 90}{Colors.RESET}
{Colors.BOLD}{Colors.CYAN}                    Made with ❤️  by {Colors.MAGENTA}mohammadumar-dev{Colors.CYAN}                    {Colors.RESET}
{Colors.DIM}{'─' * 90}{Colors.RESET}
"""
    print(footer)


def print_menu():
    """Print the main menu with enhanced formatting."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}╔════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  {Colors.BOLD}Passkeys CLI - Main Menu{Colors.RESET}              {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}╠════════════════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  1. View passkeys                      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  2. Create passkey                     {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  3. Update passkey                     {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  4. Delete passkey                     {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  5. Generate password                  {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  6. Exit                               {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}╚════════════════════════════════════════╝{Colors.RESET}\n")


def print_entries_table(entries: List[Dict]):
    """Print entries in a formatted table."""
    if not entries:
        print_warning("No passkeys found in vault.")
        return
    
    print_header("Your Passkeys")
    
    # Table header
    print(f"{Colors.BOLD}{'ID':<38} {'Service':<20} {'Username':<20}{Colors.RESET}")
    print_separator()
    
    # Table rows
    for entry in entries:
        entry_id = str(entry['id'])
        service = entry['service'][:18] + '..' if len(entry['service']) > 20 else entry['service']
        username = entry['username'][:25] + '..' if len(entry['username']) > 35 else entry['username']
        print(f"{Colors.CYAN}{entry_id:<38}{Colors.RESET} {service:<20} {username:<30}")
    
    print()


def get_input(prompt: str, required: bool = True, validator=None) -> str:
    """
    Get user input with validation.
    
    Args:
        prompt: Input prompt
        required: Whether input is required
        validator: Optional validation function
        
    Returns:
        Validated input string
    """
    while True:
        try:
            value = input(f"{Colors.CYAN}{prompt}{Colors.RESET}: ").strip()
            
            if required and not value:
                print_error("This field is required.")
                continue
            
            if validator:
                value = validator(value)
            
            return value
        except KeyboardInterrupt:
            print("\n")
            print_warning("Operation cancelled.")
            sys.exit(0)
        except Exception as e:
            print_error(str(e))
            continue


def get_password_input(prompt: str, confirm: bool = False) -> str:
    """
    Get password input with optional confirmation.
    
    Args:
        prompt: Password prompt
        confirm: Whether to ask for confirmation
        
    Returns:
        Password string
    """
    import getpass
    
    while True:
        try:
            password = getpass.getpass(f"{Colors.CYAN}{prompt}{Colors.RESET}: ")
            
            if not password:
                print_error("Password cannot be empty.")
                continue
            
            if confirm:
                confirm_password = getpass.getpass(f"{Colors.CYAN}Confirm {prompt.lower()}{Colors.RESET}: ")
                if password != confirm_password:
                    print_error("Passwords do not match. Please try again.")
                    continue
            
            return password
        except KeyboardInterrupt:
            print("\n")
            print_warning("Operation cancelled.")
            sys.exit(0)
