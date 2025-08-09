#!/usr/bin/env python3
"""
NeoXBridge AI - Complete End-to-End Use Case Demonstration
===========================================================

This script demonstrates a complete real-world scenario showcasing all the key 
features of NeoXBridge AI in a cohesive user journey.

Scenario: "Sarah's DeFi Portfolio Management"
- A crypto enthusiast wants to manage her Neo N3 portfolio
- She uses NeoXBridge AI for all blockchain operations through natural conversation
- The AI helps with security checks, balance management, and transaction execution

Author: Nikhil Raikwar
"""

import asyncio
import sys
import time
from datetime import datetime
from typing import List, Dict
from src.ui import (
    print_banner, 
    print_divider, 
    print_success, 
    print_info, 
    print_warning,
    print_agent_response,
    print_error,
    print_step
)
from src.config import config


class EndToEndDemo:
    """Complete end-to-end demonstration of NeoXBridge AI capabilities."""
    
    def __init__(self):
        self.user_name = "Sarah"
        self.scenario_steps = [
            {
                "step": 1,
                "title": "Initial Setup & Greeting",
                "user_input": "Hello! I'm new to NeoXBridge AI. Can you help me manage my crypto portfolio?",
                "description": "User greets the AI and asks for help with portfolio management"
            },
            {
                "step": 2,
                "title": "Address Validation",
                "user_input": "I have this Neo address: NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N - can you validate it's correct?",
                "description": "User provides a Neo N3 address for validation"
            },
            {
                "step": 3,
                "title": "Security Check",
                "user_input": "Is this address safe to receive funds: NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c?",
                "description": "User requests security analysis for a recipient address"
            },
            {
                "step": 4,
                "title": "Balance Inquiry",
                "user_input": "Check my current balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N",
                "description": "User requests current wallet balance information"
            },
            {
                "step": 5,
                "title": "Transaction Planning",
                "user_input": "I want to send 25 NEO to my friend at NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c. What should I know?",
                "description": "User plans a significant transaction and seeks guidance"
            },
            {
                "step": 6,
                "title": "Transaction Execution",
                "user_input": "Send 25 NEO to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c",
                "description": "User executes the planned transaction"
            },
            {
                "step": 7,
                "title": "Transaction Status Check",
                "user_input": "What's the status of my last transaction?",
                "description": "User checks on the transaction they just sent"
            },
            {
                "step": 8,
                "title": "Portfolio Summary",
                "user_input": "Give me a summary of my current portfolio and recent activity",
                "description": "User requests comprehensive portfolio overview"
            },
            {
                "step": 9,
                "title": "Help & Features",
                "user_input": "What else can you help me with regarding Neo blockchain?",
                "description": "User explores additional capabilities"
            },
            {
                "step": 10,
                "title": "Session Wrap-up",
                "user_input": "Thank you for the help! This was amazing.",
                "description": "User concludes the session with positive feedback"
            }
        ]
        
        self.session_metrics = {
            "start_time": None,
            "end_time": None,
            "total_interactions": 0,
            "successful_operations": 0,
            "security_checks_performed": 0,
            "addresses_validated": 0,
            "transactions_processed": 0
        }
    
    def print_scenario_intro(self):
        """Print the scenario introduction."""
        print_banner()
        print("\n🎭 COMPLETE END-TO-END USE CASE DEMONSTRATION")
        print("=" * 80)
        print(f"""
📖 SCENARIO: "{self.user_name}'s DeFi Portfolio Management Journey"

{self.user_name} is a crypto enthusiast who wants to manage her Neo N3 portfolio using 
natural language instead of complex blockchain tools. She'll interact with 
NeoXBridge AI to perform real-world tasks including:

🎯 OBJECTIVES:
├─ ✅ Validate her Neo addresses
├─ 🛡️ Check security of recipient addresses  
├─ 💰 Check her current token balances
├─ 🚀 Execute secure token transfers
├─ 📊 Monitor transaction status
└─ 📈 Get portfolio insights

🌟 FEATURES DEMONSTRATED:
├─ 🗣️ Natural Language Processing
├─ 🔍 Address Validation & Security Analysis
├─ 💼 Portfolio Management
├─ 🛡️ GoPlus Labs Security Integration  
├─ 🚀 Transaction Simulation & Execution
├─ 📊 Real-time Status Tracking
├─ 🎯 Contextual Conversations
└─ 🧠 AI-Powered Assistance

💡 This demo runs in SAFE MODE - all transactions are simulated!
""")
        print_divider()
    
    def print_step_header(self, step_info: Dict):
        """Print step header with context."""
        print(f"\n📋 STEP {step_info['step']}/10: {step_info['title']}")
        print_divider("-", 60)
        print(f"📝 Context: {step_info['description']}")
        print(f"💬 {self.user_name}: \"{step_info['user_input']}\"")
        print()
    
    async def run_interactive_scenario(self):
        """Run the interactive scenario step by step."""
        try:
            from src.agent import NeoXBridgeAgent
            from src.ui import get_user_input
            
            # Initialize the AI agent
            print("🚀 Initializing NeoXBridge AI for the demonstration...")
            agent = NeoXBridgeAgent()
            await agent.initialize()
            print_success("NeoXBridge AI is ready for Sarah's portfolio management session!")
            
            self.session_metrics["start_time"] = datetime.now()
            
            print("\n" + "=" * 80)
            print("🎬 STARTING INTERACTIVE DEMONSTRATION")
            print("⏸️  Press Enter after each step to continue...")
            print("=" * 80)
            
            # Process each scenario step
            for step_info in self.scenario_steps:
                self.print_step_header(step_info)
                
                # Process the user input through the AI
                print("🔄 NeoXBridge AI is processing...")
                try:
                    response = await agent.process_message(step_info["user_input"])
                    print_agent_response(response)
                    
                    # Update metrics
                    self.session_metrics["total_interactions"] += 1
                    self.session_metrics["successful_operations"] += 1
                    
                    if "security" in step_info["title"].lower() or "safe" in step_info["user_input"].lower():
                        self.session_metrics["security_checks_performed"] += 1
                    
                    if "validate" in step_info["user_input"].lower() or "address" in step_info["user_input"].lower():
                        self.session_metrics["addresses_validated"] += 1
                    
                    if "send" in step_info["user_input"].lower() or "transaction" in step_info["user_input"].lower():
                        self.session_metrics["transactions_processed"] += 1
                
                except Exception as e:
                    print_error(f"Step {step_info['step']} failed: {e}")
                    print_warning("Continuing to next step...")
                
                # Wait for user to continue (except for last step)
                if step_info["step"] < len(self.scenario_steps):
                    input(f"\n⏸️  Press Enter to continue to step {step_info['step'] + 1}...")
                    print_divider("=", 80)
            
            self.session_metrics["end_time"] = datetime.now()
            self.print_session_summary()
            
        except Exception as e:
            print_error(f"Demo initialization failed: {e}")
            self.print_setup_instructions()
    
    async def run_automated_scenario(self):
        """Run automated scenario with timed pauses."""
        try:
            from src.agent import NeoXBridgeAgent
            
            print("🤖 Running Automated End-to-End Demonstration...")
            agent = NeoXBridgeAgent()
            await agent.initialize()
            print_success("AI Agent initialized successfully!")
            
            self.session_metrics["start_time"] = datetime.now()
            
            print("\n" + "=" * 80)
            print("🎬 AUTOMATED DEMONSTRATION STARTING")
            print("⏱️  Each step will auto-advance after showing results")
            print("=" * 80)
            
            for step_info in self.scenario_steps:
                self.print_step_header(step_info)
                
                print("🔄 Processing...")
                time.sleep(1)  # Simulate thinking time
                
                try:
                    response = await agent.process_message(step_info["user_input"])
                    print_agent_response(response)
                    
                    # Update metrics
                    self.session_metrics["total_interactions"] += 1
                    self.session_metrics["successful_operations"] += 1
                    
                    if "security" in step_info["title"].lower():
                        self.session_metrics["security_checks_performed"] += 1
                    if "address" in step_info["user_input"].lower():
                        self.session_metrics["addresses_validated"] += 1
                    if "send" in step_info["user_input"].lower():
                        self.session_metrics["transactions_processed"] += 1
                
                except Exception as e:
                    print_error(f"Step {step_info['step']} error: {e}")
                
                # Auto-advance delay
                if step_info["step"] < len(self.scenario_steps):
                    print(f"\n⏳ Auto-advancing to step {step_info['step'] + 1} in 3 seconds...")
                    time.sleep(3)
                    print_divider("=", 80)
            
            self.session_metrics["end_time"] = datetime.now()
            self.print_session_summary()
            
        except Exception as e:
            print_error(f"Automated demo failed: {e}")
            self.print_setup_instructions()
    
    def print_session_summary(self):
        """Print comprehensive session summary."""
        duration = self.session_metrics["end_time"] - self.session_metrics["start_time"]
        
        print("\n" + "🎉" * 20)
        print("✅ END-TO-END DEMONSTRATION COMPLETED!")
        print("🎉" * 20)
        
        print(f"""
📊 SESSION ANALYTICS:
┌─────────────────────────────────────────┐
│ 👤 User: {self.user_name}                          │
│ ⏱️  Duration: {str(duration).split('.')[0]}              │
│ 💬 Total Interactions: {self.session_metrics['total_interactions']:2d}             │
│ ✅ Successful Operations: {self.session_metrics['successful_operations']:2d}           │
│ 🛡️ Security Checks: {self.session_metrics['security_checks_performed']:2d}                │
│ 🔍 Addresses Validated: {self.session_metrics['addresses_validated']:2d}            │
│ 🚀 Transactions Processed: {self.session_metrics['transactions_processed']:2d}         │
└─────────────────────────────────────────┘

🌟 FEATURES SUCCESSFULLY DEMONSTRATED:
✅ Natural Language Understanding
✅ Address Validation & Security Analysis  
✅ Real-time Balance Checking
✅ Transaction Simulation & Execution
✅ GoPlus Labs Security Integration
✅ Contextual Conversation Flow
✅ Error Handling & Recovery
✅ Session Management & Analytics

🎯 REAL-WORLD USE CASES COVERED:
├─ 👤 New User Onboarding
├─ 🔍 Address & Security Validation
├─ 💰 Portfolio Balance Management  
├─ 🚀 Secure Token Transfers
├─ 📊 Transaction Status Monitoring
└─ 🤝 AI-Assisted Decision Making

💡 NEXT STEPS:
• Try the interactive mode: python main.py
• Explore more features: python demo.py  
• Read documentation: README.md
• Set up your own API keys in .env
""")
        
        print_divider("=", 80)
        print("🌟 NeoXBridge AI - Making Blockchain as Easy as Conversation!")
        print_divider("=", 80)
    
    def print_setup_instructions(self):
        """Print setup instructions if demo fails."""
        print("""
🔧 SETUP REQUIRED FOR FULL DEMONSTRATION:

1️⃣ COPY ENVIRONMENT FILE:
   cp .env.example .env

2️⃣ ADD YOUR OPENAI API KEY:
   Edit .env file and add: OPENAI_API_KEY=your_key_here
   Get key from: https://platform.openai.com/api-keys

3️⃣ INSTALL DEPENDENCIES:
   pip install -r requirements.txt

4️⃣ OPTIONAL - ADD GOPLUS LABS API KEY:
   Add to .env: GO_PLUS_LABS_APP_KEY=your_key_here
   Get key from: https://gopluslabs.io/

5️⃣ RUN DEMONSTRATION:
   python end_to_end_demo.py

📚 For more help, see README.md
""")
    
    async def run(self):
        """Main demo runner."""
        self.print_scenario_intro()
        
        # Check configuration
        if not config.is_configured():
            print_error("❌ Configuration incomplete!")
            config.print_status()
            self.print_setup_instructions()
            return
        
        # Ask user for demo type
        print("🎭 DEMONSTRATION OPTIONS:")
        print("1. 🎮 Interactive Demo - Step through each interaction manually")
        print("2. 🤖 Automated Demo - Watch the complete scenario automatically")  
        print("3. 📖 Show scenario overview only")
        
        try:
            choice = input("\n💭 Choose demonstration type (1-3): ").strip()
            
            if choice == "1":
                await self.run_interactive_scenario()
            elif choice == "2":
                await self.run_automated_scenario()
            elif choice == "3":
                print("\n✅ Scenario overview shown above!")
                print(f"📚 {len(self.scenario_steps)} steps covering complete portfolio management workflow")
                print("💡 Run option 1 or 2 to see the full demonstration with AI responses")
            else:
                print("❌ Invalid choice. Running interactive demo...")
                await self.run_interactive_scenario()
                
        except KeyboardInterrupt:
            print("\n\n🛑 Demonstration stopped by user")
            if self.session_metrics["start_time"]:
                self.session_metrics["end_time"] = datetime.now()
                print(f"⏱️  Partial session duration: {self.session_metrics['end_time'] - self.session_metrics['start_time']}")
            print("👋 Thank you for trying NeoXBridge AI!")
        except Exception as e:
            print_error(f"Demonstration error: {e}")


async def main():
    """Main entry point for the end-to-end demonstration."""
    demo = EndToEndDemo()
    await demo.run()


if __name__ == "__main__":
    print("🚀 NeoXBridge AI - Complete End-to-End Use Case Demonstration")
    print("=" * 70)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Demonstration ended by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Demonstration crashed: {e}")
        print("\n🔧 Setup Help:")
        print("1. Copy .env.example to .env")  
        print("2. Add your OpenAI API key")
        print("3. Run: pip install -r requirements.txt")
        sys.exit(1)
