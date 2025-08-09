#!/usr/bin/env python3
"""
NeoXBridge AI - Demo Script
A simple demonstration script showing the capabilities of NeoXBridge AI.
"""

import asyncio
import sys
from typing import List
from src.ui import print_banner, print_divider
from src.config import config


class NeoXBridgeDemo:
    """Demo class for showcasing NeoXBridge AI capabilities."""
    
    def __init__(self):
        self.demo_commands = [
            "Help",
            "Check balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N",
            "Is this address safe: NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c",
            "Send 10 NEO to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c",
            "What's the status of my last transaction?",
            "Validate address NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"
        ]
    
    def print_demo_intro(self):
        """Print demo introduction."""
        print_banner()
        print("\n🎭 DEMO MODE - NeoXBridge AI Showcase")
        print("=" * 80)
        print("""
This demo showcases the natural language capabilities of NeoXBridge AI.
In demo mode, all blockchain operations are simulated for safety.

🌟 Key Features Demonstrated:
├─ 🗣️ Natural Language Processing
├─ 🔍 Address Validation & Security Checking  
├─ 💰 Balance Queries & Token Information
├─ 🚀 Transaction Simulation & Status Tracking
├─ 🛡️ GoPlus Labs Security Integration
└─ 🎯 Conversational Error Handling

💡 Try speaking naturally - the AI understands context and intent!
""")
        print_divider()
    
    def print_sample_commands(self):
        """Print sample commands for users to try."""
        print("\n🎯 Sample Commands to Try:")
        print_divider("-", 50)
        
        for i, command in enumerate(self.demo_commands, 1):
            print(f"{i:2d}. 💬 \"{command}\"")
        
        print("\n💡 Or try your own natural language queries!")
        print("   Examples:")
        print("   • \"What's my wallet balance?\"")
        print("   • \"I want to send tokens to my friend\"")
        print("   • \"Is this smart contract legitimate?\"")
        print("   • \"How much GAS do I have?\"")
        print_divider()
    
    async def run_interactive_demo(self):
        """Run interactive demo mode."""
        try:
            from src.agent import NeoXBridgeAgent
            from src.ui import get_user_input, print_agent_response, print_error
            
            # Initialize agent
            print("🚀 Initializing NeoXBridge AI Demo...")
            agent = NeoXBridgeAgent()
            await agent.initialize()
            print("✅ Demo ready!\n")
            
            print("💬 Start chatting with NeoXBridge AI (type 'quit' to exit):")
            print_divider()
            
            while True:
                user_input = get_user_input()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n👋 Thanks for trying NeoXBridge AI Demo!")
                    break
                
                if not user_input.strip():
                    continue
                
                # Process input
                print("🔄 Processing...")
                try:
                    response = await agent.process_message(user_input)
                    print_agent_response(response)
                except Exception as e:
                    print_error(f"Demo error: {e}")
                    print("💡 Try a different command or check your API configuration.")
        
        except Exception as e:
            print_error(f"Failed to initialize demo: {e}")
            print("""
🔧 Setup Required:
1. Copy .env.example to .env
2. Add your OpenAI API key to the .env file
3. Optionally add GoPlus Labs API key for security features
4. Run: pip install -r requirements.txt
""")
    
    async def run_automated_demo(self):
        """Run automated demo with predefined commands."""
        try:
            from src.agent import NeoXBridgeAgent
            from src.ui import print_agent_response, print_error
            
            print("🤖 Running Automated Demo...")
            agent = NeoXBridgeAgent()
            await agent.initialize()
            print("✅ Agent initialized!\n")
            
            for i, command in enumerate(self.demo_commands, 1):
                print(f"\n📋 Demo Step {i}/{len(self.demo_commands)}")
                print(f"💬 You: {command}")
                print("🔄 Processing...")
                
                try:
                    response = await agent.process_message(command)
                    print_agent_response(response)
                    
                    # Wait for user to continue
                    input("\n⏸️  Press Enter to continue to next demo...")
                    
                except Exception as e:
                    print_error(f"Demo step failed: {e}")
                    continue
            
            print("\n🎉 Automated demo completed!")
            print("💡 Try the interactive mode by running: python main.py")
        
        except Exception as e:
            print_error(f"Automated demo failed: {e}")
    
    async def run(self):
        """Run the demo."""
        self.print_demo_intro()
        
        if not config.is_configured():
            print("❌ Configuration incomplete!")
            config.print_status()
            print("""
🔧 Quick Setup:
1. Copy .env.example to .env
2. Add your OpenAI API key
3. Run: pip install -r requirements.txt
4. Run: python demo.py
""")
            return
        
        self.print_sample_commands()
        
        # Ask user for demo type
        print("\n🎭 Demo Options:")
        print("1. 🎮 Interactive Demo - Chat with the AI")
        print("2. 🤖 Automated Demo - Watch predefined examples")
        print("3. 📖 Show sample commands only")
        
        try:
            choice = input("\n💭 Choose demo type (1-3): ").strip()
            
            if choice == "1":
                await self.run_interactive_demo()
            elif choice == "2":
                await self.run_automated_demo()
            elif choice == "3":
                print("\n✅ Sample commands shown above!")
                print("💡 Run 'python main.py' to start the full application.")
            else:
                print("❌ Invalid choice. Running interactive demo...")
                await self.run_interactive_demo()
        
        except KeyboardInterrupt:
            print("\n\n👋 Demo ended by user. Goodbye!")
        except Exception as e:
            print_error(f"Demo error: {e}")


async def main():
    """Main demo entry point."""
    demo = NeoXBridgeDemo()
    await demo.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Demo ended. Goodbye!")
    except Exception as e:
        print(f"\n❌ Demo crashed: {e}")
        sys.exit(1)
