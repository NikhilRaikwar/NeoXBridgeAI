"""
NeoXBridge AI - UI Utilities
Console interface utilities for the NeoXBridge AI application.
"""

import os
from datetime import datetime


def print_banner():
    """Print the application banner."""
    banner = """
╔════════════════════════════════════════════════════════════════════════════════╗
║                            🚀 NeoXBridge AI 🚀                                ║
║                                                                                ║
║         Conversational AI Assistant for NeoX Blockchain Operations            ║
║                                                                                ║
║  Features:                                                                     ║
║  • 🔍 Natural language address validation                                     ║
║  • 💰 Real-time balance checking                                              ║
║  • 🛡️ GoPlus Labs security integration                                        ║
║  • 🚀 Secure token transfers with confirmations                               ║
║  • 📊 Transaction status tracking                                             ║
║                                                                                ║
║  Example commands:                                                             ║
║  • "Check balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"                     ║
║  • "Send 10 NEO to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c"                       ║
║  • "Is this address safe: [paste address]"                                    ║
║  • "Help" - Show available commands                                           ║
║                                                                                ║
║  Type 'quit' or 'exit' to end the session                                     ║
║                                                                                ║
║  Author: Nikhil Raikwar | GitHub: @NikhilRaikwar                              ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_system_info():
    """Print system information and configuration status."""
    print("\n📋 System Information:")
    print(f"   Version: 1.0.0")
    print(f"   Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check environment configuration
    api_key_configured = "✅" if os.getenv('OPENAI_API_KEY') else "❌"
    neo_rpc_configured = "✅" if os.getenv('NEO_RPC_URL') else "🔄 (using default)"
    goplus_configured = "✅" if os.getenv('GO_PLUS_LABS_APP_KEY') else "❌"
    
    print(f"   OpenAI API Key: {api_key_configured}")
    print(f"   Neo RPC URL: {neo_rpc_configured}")
    print(f"   GoPlus Labs API: {goplus_configured}")
    
    if not os.getenv('OPENAI_API_KEY'):
        print(f"   ⚠️  Warning: Set OPENAI_API_KEY in .env file for full functionality")
    
    print()


def get_user_input() -> str:
    """Get user input with enhanced prompt."""
    try:
        user_input = input("💬 You: ").strip()
        return user_input
    except KeyboardInterrupt:
        print("\n\n👋 Session ended by user. Goodbye!")
        return "quit"
    except EOFError:
        return "quit"


def print_agent_response(response: str):
    """Print agent response with formatting."""
    print(f"\n🤖 NeoXBridge AI:")
    
    # Split response into lines for better formatting
    lines = response.split('\n')
    for line in lines:
        if line.strip():  # Only print non-empty lines
            print(f"   {line}")
        else:
            print()  # Print empty line for spacing
    
    print("\n" + "─" * 80)


def print_error(error_message: str):
    """Print error message with formatting."""
    print(f"\n❌ Error: {error_message}\n")
    print("─" * 80)


def print_success(message: str):
    """Print success message with formatting."""
    print(f"\n✅ Success: {message}\n")
    print("─" * 80)


def print_warning(message: str):
    """Print warning message with formatting."""
    print(f"\n⚠️ Warning: {message}\n")
    print("─" * 80)


def print_info(message: str):
    """Print info message with formatting."""
    print(f"\nℹ️ Info: {message}\n")
    print("─" * 80)


def format_address(address: str) -> str:
    """Format address for display."""
    if len(address) > 20:
        return f"{address[:8]}...{address[-8:]}"
    return address


def format_amount(amount: float, asset: str) -> str:
    """Format amount with asset for display."""
    return f"{amount:,.8f}".rstrip('0').rstrip('.') + f" {asset}"


def format_timestamp(timestamp: str) -> str:
    """Format timestamp for display."""
    try:
        from datetime import datetime
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        return timestamp


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_loading(message: str = "Processing..."):
    """Print loading message."""
    print(f"⏳ {message}")


def print_step(step_num: int, message: str):
    """Print step in a process."""
    print(f"📋 Step {step_num}: {message}")


def print_divider(char: str = "=", length: int = 80):
    """Print a divider line."""
    print(char * length)
