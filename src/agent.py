"""
NeoXBridge AI Agent - Main conversational agent for NeoX blockchain operations
"""

import os
import re
import asyncio
import logging
from typing import Optional, Dict, Any
from datetime import datetime

from .tools import NeoXTools
from .llm_client import LLMClient
from .prompts import SYSTEM_PROMPT, get_contextual_response

logger = logging.getLogger(__name__)


class NeoXBridgeAgent:
    """
    NeoXBridge AI Agent - A conversational AI for secure NeoX blockchain operations.
    
    Features:
    - Natural language understanding for blockchain operations
    - Security-first transaction processing
    - GoPlus Labs integration for address validation
    - Context-aware conversation management
    """
    
    def __init__(self):
        self.tools = NeoXTools()
        self.llm_client = None
        self.conversation_history = []
        self.context = {
            "last_address": None,
            "pending_transaction": None,
            "user_preferences": {},
            "session_start": datetime.now()
        }
        self.logger = logging.getLogger(__name__ + ".NeoXBridgeAgent")
    
    async def initialize(self):
        """Initialize the agent with LLM client and tools."""
        try:
            # Initialize LLM client
            self.llm_client = LLMClient()
            await self.llm_client.initialize()
            
            # Initialize tools
            await self.tools.initialize()
            
            self.logger.info("NeoXBridge AI Agent initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize agent: {e}")
            raise
    
    async def process_message(self, user_message: str) -> str:
        """
        Process a user message and return an appropriate response.
        
        Args:
            user_message (str): The user's input message
            
        Returns:
            str: The agent's response
        """
        try:
            # Add to conversation history
            self.conversation_history.append({
                "role": "user", 
                "content": user_message,
                "timestamp": datetime.now()
            })
            
            # Extract any Neo addresses from the message
            extracted_address = self._extract_neo_address(user_message)
            if extracted_address:
                self.context["last_address"] = extracted_address
            
            # Determine intent and execute appropriate action
            intent = await self._classify_intent(user_message)
            response = await self._execute_intent(intent, user_message)
            
            # Add response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now()
            })
            
            return response
            
        except Exception as e:
            self.logger.error(f"Error processing message: {e}")
            return "I apologize, but I encountered an error processing your request. Please try again or type 'help' for assistance."
    
    def _extract_neo_address(self, message: str) -> Optional[str]:
        """Extract Neo address from message using regex."""
        # Neo addresses are 34 characters starting with 'N'
        pattern = r'\bN[A-Za-z0-9]{33}\b'
        matches = re.findall(pattern, message)
        return matches[0] if matches else None
    
    async def _classify_intent(self, message: str) -> Dict[str, Any]:
        """
        Classify the user's intent using LLM.
        
        Args:
            message (str): User message
            
        Returns:
            dict: Intent classification with confidence and parameters
        """
        classification_prompt = f"""
Classify this user message for NeoX blockchain operations:

Message: "{message}"

Respond with ONLY a JSON object in this format:
{{
    "intent": "one of: validate_address, check_balance, send_transaction, check_transaction, general_help, security_check",
    "confidence": 0.0-1.0,
    "parameters": {{
        "address": "extracted_address_if_any",
        "amount": "extracted_amount_if_any",
        "asset": "NEO_or_GAS_if_mentioned",
        "recipient": "recipient_address_if_any"
    }}
}}
"""
        
        try:
            response = await self.llm_client.generate_response(
                classification_prompt,
                max_tokens=200,
                temperature=0.1
            )
            
            # Parse JSON response
            import json
            intent_data = json.loads(response.strip())
            return intent_data
            
        except Exception as e:
            self.logger.error(f"Intent classification failed: {e}")
            return {
                "intent": "general_help",
                "confidence": 0.5,
                "parameters": {}
            }
    
    async def _execute_intent(self, intent_data: Dict[str, Any], original_message: str) -> str:
        """Execute the classified intent."""
        intent = intent_data.get("intent", "general_help")
        params = intent_data.get("parameters", {})
        
        try:
            if intent == "validate_address":
                return await self._handle_address_validation(params, original_message)
            
            elif intent == "check_balance":
                return await self._handle_balance_check(params, original_message)
            
            elif intent == "send_transaction":
                return await self._handle_send_transaction(params, original_message)
            
            elif intent == "check_transaction":
                return await self._handle_transaction_check(params, original_message)
            
            elif intent == "security_check":
                return await self._handle_security_check(params, original_message)
            
            else:
                return await self._handle_general_help(original_message)
                
        except Exception as e:
            self.logger.error(f"Intent execution failed: {e}")
            return f"I encountered an error while processing your {intent} request. Please try again."
    
    async def _handle_address_validation(self, params: Dict[str, Any], original_message: str) -> str:
        """Handle address validation requests."""
        address = params.get("address") or self.context.get("last_address")
        
        if not address:
            return "Please provide a Neo address to validate. Example: 'Validate address NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N'"
        
        result = await self.tools.validate_address(address)
        
        # Generate contextual response
        return get_contextual_response("address_validation", {
            "address": address,
            "result": result,
            "original_message": original_message
        })
    
    async def _handle_balance_check(self, params: Dict[str, Any], original_message: str) -> str:
        """Handle balance check requests."""
        address = params.get("address") or self.context.get("last_address")
        
        if not address:
            return "Please provide a Neo address to check the balance. Example: 'Check balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N'"
        
        result = await self.tools.get_balance(address)
        
        return get_contextual_response("balance_check", {
            "address": address,
            "result": result,
            "original_message": original_message
        })
    
    async def _handle_send_transaction(self, params: Dict[str, Any], original_message: str) -> str:
        """Handle send transaction requests."""
        recipient = params.get("recipient")
        amount = params.get("amount")
        asset = params.get("asset", "NEO")
        
        if not recipient or not amount:
            return "To send tokens, please specify both recipient address and amount. Example: 'Send 10 NEO to NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N'"
        
        try:
            # Convert amount to float
            amount_float = float(amount)
            
            result = await self.tools.send_transaction(recipient, amount_float, asset)
            
            return get_contextual_response("send_transaction", {
                "recipient": recipient,
                "amount": amount_float,
                "asset": asset,
                "result": result,
                "original_message": original_message
            })
            
        except ValueError:
            return f"Invalid amount '{amount}'. Please specify a valid number."
    
    async def _handle_transaction_check(self, params: Dict[str, Any], original_message: str) -> str:
        """Handle transaction status check requests."""
        # Extract transaction hash from parameters or message
        tx_hash = params.get("tx_hash")
        if not tx_hash:
            # Try to extract from original message
            hash_pattern = r'0x[a-fA-F0-9]{64}'
            matches = re.findall(hash_pattern, original_message)
            tx_hash = matches[0] if matches else None
        
        if not tx_hash:
            return "Please provide a transaction hash to check. Example: 'Check transaction 0xabc123...'"
        
        result = await self.tools.check_transaction_status(tx_hash)
        
        return get_contextual_response("transaction_check", {
            "tx_hash": tx_hash,
            "result": result,
            "original_message": original_message
        })
    
    async def _handle_security_check(self, params: Dict[str, Any], original_message: str) -> str:
        """Handle security check requests."""
        address = params.get("address") or self.context.get("last_address")
        
        if not address:
            return "Please provide an address to check for security. Example: 'Is this address safe: NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N'"
        
        result = await self.tools.check_address_security(address)
        
        return get_contextual_response("security_check", {
            "address": address,
            "result": result,
            "original_message": original_message
        })
    
    async def _handle_general_help(self, original_message: str) -> str:
        """Handle general help and conversation."""
        # Use LLM for general conversation with blockchain context
        context_prompt = f"""
You are NeoXBridge AI, a helpful assistant for NeoX blockchain operations.

User message: "{original_message}"

Recent conversation context:
{self._get_recent_conversation_context()}

Respond helpfully about NeoX blockchain operations. You can:
- Validate Neo addresses
- Check NEO/GAS balances  
- Help with secure token transfers
- Check transaction status
- Provide security advice

Keep responses friendly, informative, and focused on blockchain operations.
"""
        
        try:
            response = await self.llm_client.generate_response(
                context_prompt,
                max_tokens=300,
                temperature=0.7
            )
            return response.strip()
            
        except Exception as e:
            self.logger.error(f"General help response failed: {e}")
            return get_contextual_response("general_help", {
                "original_message": original_message
            })
    
    def _get_recent_conversation_context(self) -> str:
        """Get recent conversation context for LLM."""
        if len(self.conversation_history) <= 4:
            return "No recent conversation."
        
        recent = self.conversation_history[-4:]
        context_lines = []
        
        for entry in recent:
            role = "User" if entry["role"] == "user" else "Assistant"
            content = entry["content"][:100] + "..." if len(entry["content"]) > 100 else entry["content"]
            context_lines.append(f"{role}: {content}")
        
        return "\n".join(context_lines)
    
    def get_session_info(self) -> Dict[str, Any]:
        """Get current session information."""
        uptime = datetime.now() - self.context["session_start"]
        
        return {
            "session_duration": str(uptime).split('.')[0],
            "messages_processed": len(self.conversation_history) // 2,
            "last_address": self.context.get("last_address"),
            "tools_available": len(self.tools.get_available_tools()),
            "status": "active"
        }
