#!/usr/bin/env python3
"""
NeoXBridge AI - Conversational Interface for NeoX Blockchain
A standalone AI-powered assistant for secure NeoX blockchain operations.

Author: Nikhil Raikwar
GitHub: https://github.com/NikhilRaikwar
License: MIT
"""

import asyncio
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
import logging

from src.agent import NeoXBridgeAgent
from src.config import config
from src.ui import (
    print_banner, 
    print_system_info, 
    get_user_input, 
    print_agent_response, 
    print_error,
    print_info,
    clear_screen
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL.upper()),
    format=config.LOG_FORMAT,
    filename=config.LOG_FILE
)

# Load environment variables
load_dotenv()

class NeoXBridgeApp:
    """Main application class for NeoXBridge AI."""
    
    def __init__(self):
        self.agent = None
        self.session_stats = {
            "messages_exchanged": 0,
            "commands_processed": 0,
            "addresses_validated": 0,
            "transactions_simulated": 0,
            "start_time": datetime.now()
        }
    
    async def initialize(self):
        """Initialize the NeoXBridge AI agent."""
        try:
            print("🚀 Initializing NeoXBridge AI...")
            self.agent = NeoXBridgeAgent()
            await self.agent.initialize()
            print("✅ NeoXBridge AI initialized successfully!")
            return True
        except Exception as e:
            print_error(f"Failed to initialize NeoXBridge AI: {e}")
            return False
    
    def handle_special_commands(self, user_input: str) -> tuple[bool, str]:
        """Handle special demo commands."""
        user_input_lower = user_input.lower().strip()
        
        if user_input_lower in ["quit", "exit", "bye", "goodbye"]:
            return True, "quit"
        
        elif user_input_lower in ["help", "commands"]:
            return True, self._get_help_message()
        
        elif user_input_lower in ["status", "info"]:
            return True, self._get_status_message()
        
        elif user_input_lower in ["examples", "demo"]:
            return True, self._get_examples_message()
        
        return False, ""
    
    def _get_help_message(self) -> str:
        """Get help message."""
        return """
🔧 NeoXBridge AI Commands

Available Operations:
├─ 🔍 Address Operations
│   ├─ "Validate address [address]"
│   └─ "Check balance [address]"
├─ 💸 Transaction Operations  
│   ├─ "Send [amount] NEO to [address]"
│   ├─ "Send [amount] GAS to [address]" 
│   └─ "Check transaction [hash]"
├─ 🛡️ Security Operations
│   └─ "Is [address] safe?"
└─ ℹ️ Information
    ├─ "help" - Show this menu
    └─ "examples" - Show usage examples

Just speak naturally! Examples:
• "Send 10 NEO to my friend at [address]"
• "What's the balance of this address?"
• "Is this address legitimate?"
"""
    
    def _get_status_message(self) -> str:
        """Get agent status message."""
        uptime = datetime.now() - self.session_stats["start_time"]
        return f"""
🤖 NeoXBridge AI Status:
   Version: 1.0.0
   Uptime: {str(uptime).split('.')[0]}
   
📊 Session Statistics:
   Messages: {self.session_stats['messages_exchanged']}
   Commands: {self.session_stats['commands_processed']}
   Addresses Validated: {self.session_stats['addresses_validated']}
   Transactions: {self.session_stats['transactions_simulated']}

🛡️ Security Features:
   • GoPlus Labs Integration
   • Address Validation
   • Transaction Confirmation
   • Malicious Address Detection
"""
    
    def _get_examples_message(self) -> str:
        """Get examples message."""
        return """
🎯 Sample Commands to Try:

🔍 Address Validation:
   • "Validate address NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"
   • "Is this address valid: NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c"

💰 Balance Checking:
   • "Check balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"
   • "What's my NEO balance?"

🚀 Token Transfers:
   • "Send 10 NEO to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c"
   • "Transfer 5.5 GAS to NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"

🛡️ Security Checks:
   • "Is this address safe: NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"
   • "Check security for NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c"

Try any of these or just speak naturally!
"""
    
    async def run(self):
        """Main application loop."""
        # Check configuration
        if not config.is_configured():
            print_error("Configuration incomplete!")
            config.print_status()
            print_info("Please set the required environment variables in your .env file.")
            return
        
        # Clear screen and show banner
        if config.ENABLE_BANNER:
            clear_screen()
            print_banner()
            print_system_info()
        
        # Initialize agent
        if not await self.initialize():
            return
        
        # Welcome message
        try:
            welcome_response = await self.agent.process_message("Hello! I'm ready to help with NeoX blockchain operations.")
            print_agent_response(welcome_response)
        except Exception as e:
            print_error(f"Welcome message failed: {e}")
        
        print("💬 Start chatting with NeoXBridge AI (type 'help' for commands or 'quit' to exit):")
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                user_input = get_user_input()
                
                if not user_input:
                    continue
                
                self.session_stats["messages_exchanged"] += 1
                
                # Handle special commands
                is_special, special_response = self.handle_special_commands(user_input)
                
                if is_special:
                    if special_response == "quit":
                        break
                    else:
                        print_agent_response(special_response)
                        continue
                
                # Process through agent
                print("🔄 Processing your request...")
                
                try:
                    response = await self.agent.process_message(user_input)
                    print_agent_response(response)
                    
                    # Update stats
                    self.session_stats["commands_processed"] += 1
                    
                    if "validated" in response.lower() or "address" in user_input.lower():
                        self.session_stats["addresses_validated"] += 1
                    
                    if "transaction" in response.lower() and "successful" in response.lower():
                        self.session_stats["transactions_simulated"] += 1
                
                except Exception as e:
                    print_error(f"Processing error: {e}")
                    print("💡 Try rephrasing your request or type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n\n🛑 Session interrupted. Goodbye!")
                break
            
            except Exception as e:
                print_error(f"Unexpected error: {e}")
        
        # Session cleanup
        self._print_session_summary()
    
    def _print_session_summary(self):
        """Print session summary."""
        session_duration = datetime.now() - self.session_stats["start_time"]
        
        print("\n" + "="*80)
        print("👋 Thank you for using NeoXBridge AI!")
        print(f"""
📊 Session Statistics:
   Messages exchanged: {self.session_stats['messages_exchanged']}
   Commands processed: {self.session_stats['commands_processed']}
   Addresses validated: {self.session_stats['addresses_validated']}
   Transactions simulated: {self.session_stats['transactions_simulated']}
   Session duration: {str(session_duration).split('.')[0]}
""")
        print("🌟 NeoXBridge AI - Making blockchain as easy as conversation!")
        print("="*80)

async def main():
    """Main entry point."""
    app = NeoXBridgeApp()
    await app.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Application ended. Goodbye!")
    except Exception as e:
        print(f"\n❌ Application crashed: {e}")
        sys.exit(1)
