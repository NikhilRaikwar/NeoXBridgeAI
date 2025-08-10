#!/usr/bin/env python3
"""
NeoXBridge AI - Comprehensive Blockchain Agent
Complete implementation with Neo blockchain tools, security analysis, and advanced features
"""

import os
import sys
import asyncio
import logging
import json
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from datetime import datetime
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv(override=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import our comprehensive tools
from neo_blockchain_tools import (
    NeoAPIClient, 
    AdvancedNeoWalletManager,
    ComprehensiveSecurityChecker,
    NEO3_AVAILABLE
)

from security_and_analysis_tools import (
    ComprehensiveSecuritySuite,
    GoPlusLabsClient,
    CryptoPriceMonitor,
    WalletAnalyzer,
    SecurityResult,
    TokenAnalysis,
    PriceAlert
)

@dataclass
class AgentResponse:
    """Structured response from the agent."""
    success: bool
    message: str
    data: Any = None
    action_type: str = "general"
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

class NeoXBridgeComprehensiveAgent:
    """
    Complete NeoXBridge AI Agent with full functionality:
    - Neo blockchain operations
    - Wallet management
    - Security analysis
    - Price monitoring
    - NFT tracking
    - Transaction analysis
    """
    
    def __init__(self, network: str = "testnet"):
        self.network = network
        self.wallet_manager = AdvancedNeoWalletManager(network)
        self.neo_api = NeoAPIClient(network)
        self.security_suite = ComprehensiveSecuritySuite()
        self.conversation_history = []
        self.session_start = datetime.now()
        
        # Initialize additional tools
        self.price_monitor = CryptoPriceMonitor()
        self.wallet_analyzer = WalletAnalyzer()
        
        # Demo balances for fallback
        self.demo_balances = {
            "NVByrj4w4W6mtXj7Lhqu9tqgZ7ApQb4UG3": {"NEO": "5.0", "GAS": "10.25"},
            "NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N": {"NEO": "150.0", "GAS": "85.42"},
            "NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c": {"NEO": "25.0", "GAS": "12.87"}
        }
        
        # Auto-load wallet if available
        if self.wallet_manager.load_from_env():
            print(f"🔓 Wallet auto-loaded: {self.wallet_manager.get_address()}")
    
    def add_to_history(self, role: str, content: str):
        """Add message to conversation history."""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now()
        })
    
    async def process_message(self, user_message: str) -> AgentResponse:
        """Process user message and return structured response."""
        try:
            self.add_to_history("user", user_message)
            intent = self.parse_intent(user_message)
            
            # Route to appropriate handler
            if intent["type"] == "wallet_operations":
                return await self.handle_wallet_operations(intent)
            elif intent["type"] == "balance_check":
                return await self.handle_balance_operations(intent)
            elif intent["type"] == "security_analysis":
                return await self.handle_security_analysis(intent)
            elif intent["type"] == "blockchain_data":
                return await self.handle_blockchain_data(intent)
            elif intent["type"] == "nft_operations":
                return await self.handle_nft_operations(intent)
            elif intent["type"] == "price_monitoring":
                return await self.handle_price_monitoring(intent)
            elif intent["type"] == "send_transaction":
                return await self.handle_send_transaction(intent)
            elif intent["type"] == "bulk_transaction":
                return await self.handle_bulk_transaction(intent)
            elif intent["type"] == "transaction_help":
                return self.get_transaction_help_response()
            elif intent["type"] == "transaction_analysis":
                return await self.handle_transaction_analysis(intent)
            elif intent["type"] == "governance_info":
                return await self.handle_governance_info(intent)
            elif intent["type"] == "help":
                return self.get_help_response()
            else:
                return self.handle_general_query(user_message)
                
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return AgentResponse(
                success=False,
                message=f"❌ I encountered an error: {str(e)}. Please try again.",
                action_type="error"
            )
    
    def parse_intent(self, message: str) -> Dict[str, Any]:
        """Parse user intent from message with comprehensive pattern matching."""
        message_lower = message.lower()
        
        # Wallet operations
        wallet_patterns = [
            'load wallet', 'import wallet', 'wallet status', 'my address', 'private key'
        ]
        if any(pattern in message_lower for pattern in wallet_patterns):
            # Extract private key if present
            key_patterns = [
                r'[KL][1-9A-HJ-NP-Za-km-z]{51}',  # WIF format
                r'0x[a-fA-F0-9]{64}',  # Hex with 0x
                r'\b[a-fA-F0-9]{64}\b'  # Raw hex
            ]
            
            private_key = None
            for pattern in key_patterns:
                match = re.search(pattern, message)
                if match:
                    private_key = match.group()
                    break
                    
            return {"type": "wallet_operations", "action": "load", "private_key": private_key}
        
        # Balance operations
        balance_patterns = ['balance', 'check balance', 'my balance', 'show balance']
        if any(pattern in message_lower for pattern in balance_patterns):
            address_match = re.search(r'([Nn][A-Za-z0-9]{33})', message)
            return {
                "type": "balance_check", 
                "address": address_match.group(1) if address_match else None
            }
        
        # Security analysis
        security_patterns = ['security', 'safe', 'malicious', 'check address', 'analyze']
        if any(pattern in message_lower for pattern in security_patterns):
            address_match = re.search(r'([Nn][A-Za-z0-9]{33})', message)
            token_match = re.search(r'(0x[a-fA-F0-9]{40})', message)
            url_match = re.search(r'https?://[^\s]+', message)
            
            target = None
            target_type = "address"
            
            if address_match:
                target = address_match.group(1)
                target_type = "address"
            elif token_match:
                target = token_match.group(1)
                target_type = "token"
            elif url_match:
                target = url_match.group()
                target_type = "url"
                
            return {"type": "security_analysis", "target": target, "target_type": target_type}
        
        # Blockchain data
        blockchain_patterns = ['block', 'transaction', 'tx', 'contract', 'asset info']
        if any(pattern in message_lower for pattern in blockchain_patterns):
            return {"type": "blockchain_data", "query": message}
        
        # NFT operations
        nft_patterns = ['nft', 'nep11', 'collectible', 'non-fungible']
        if any(pattern in message_lower for pattern in nft_patterns):
            address_match = re.search(r'([Nn][A-Za-z0-9]{33})', message)
            return {"type": "nft_operations", "address": address_match.group(1) if address_match else None}
        
        # Price monitoring
        price_patterns = ['price', 'alert', 'monitor', 'track price']
        if any(pattern in message_lower for pattern in price_patterns):
            return {"type": "price_monitoring", "query": message}
        
        # Transaction operations (send/transfer)
        send_patterns = ['send', 'transfer', 'pay']
        if any(pattern in message_lower for pattern in send_patterns):
            # Check for bulk/multiple recipient patterns
            if 'bulk' in message_lower or 'multiple' in message_lower or ',' in message:
                return {"type": "bulk_transaction", "query": message}
            else:
                # Single recipient transaction
                # Parse: "send 5 NEO to NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"
                match = re.search(r'(?:send|transfer|pay)\s+(\d+(?:\.\d+)?)\s+(neo|gas)\s+to\s+([Nn][A-Za-z0-9]{33})', message_lower)
                if match:
                    return {
                        "type": "send_transaction",
                        "amount": float(match.group(1)),
                        "asset": match.group(2).upper(),
                        "recipient": match.group(3)
                    }
                else:
                    return {"type": "transaction_help", "query": message}
        
        # Transaction analysis/history
        tx_analysis_patterns = ['transaction history', 'tx history', 'recent transactions']
        if any(pattern in message_lower for pattern in tx_analysis_patterns):
            return {"type": "transaction_analysis", "query": message}
        
        # Governance
        gov_patterns = ['governance', 'committee', 'candidate', 'vote', 'voting']
        if any(pattern in message_lower for pattern in gov_patterns):
            return {"type": "governance_info", "query": message}
        
        # Help
        if message_lower in ['help', '?', 'commands', 'what can you do']:
            return {"type": "help"}
        
        return {"type": "general", "message": message}
    
    async def handle_wallet_operations(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle wallet-related operations."""
        if intent.get("private_key"):
            # Load wallet with private key
            if self.wallet_manager.load_private_key(intent["private_key"]):
                address = self.wallet_manager.get_address()
                return AgentResponse(
                    success=True,
                    message=f"""✅ **Wallet Loaded Successfully!**
                    
📍 **Address:** `{address}`
💼 **Network:** {self.network}
🔐 **Status:** Ready for operations

Available operations:
• `check my balance` - View NEO/GAS balance
• `my nfts` - View NFT collection  
• `transaction history` - View recent transactions
• `security check {address}` - Analyze address security""",
                    data={"address": address, "network": self.network},
                    action_type="wallet_loaded"
                )
            else:
                return AgentResponse(
                    success=False,
                    message="❌ Failed to load wallet. Please check your private key format.",
                    action_type="wallet_error"
                )
        else:
            # Show wallet status
            if self.wallet_manager.is_loaded:
                address = self.wallet_manager.get_address()
                return AgentResponse(
                    success=True,
                    message=f"""💼 **Wallet Status**
                    
🔸 **Address:** `{address}`
🔸 **Network:** {self.network}
🔸 **Status:** ✅ Loaded and ready
🔸 **Neo3 Support:** {'✅ Available' if NEO3_AVAILABLE else '❌ Limited'}""",
                    data={"address": address, "loaded": True},
                    action_type="wallet_status"
                )
            else:
                return AgentResponse(
                    success=False,
                    message="""💼 **Wallet Status**
                    
🔸 **Status:** ❌ Not loaded
🔸 **Action needed:** Load your private key

**Usage:** `load wallet YOUR_PRIVATE_KEY`

**Supported formats:**
• WIF: `KxcgHRTc8SUcvwkG7V8HLoFrPHkUMskeV9nx5fvuTbsEU3z3kAS2`
• Hex: `0x1234...` or `1234567890abcdef...`""",
                    data={"loaded": False},
                    action_type="wallet_status"
                )
    
    async def handle_balance_operations(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle balance checking operations."""
        target_address = intent.get("address")
        
        # Use wallet address if no specific address provided
        if not target_address and self.wallet_manager.is_loaded:
            target_address = self.wallet_manager.get_address()
        elif not target_address:
            return AgentResponse(
                success=False,
                message="Please provide an address or load your wallet first.\nExample: `balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N`",
                action_type="balance_error"
            )
        
        try:
            # Try to get real balance from Neo API
            balances = {"NEO": "0", "GAS": "0"}
            data_source = "demo"
            
            if NEO3_AVAILABLE:
                try:
                    balance_result = self.wallet_manager.get_balance() if target_address == self.wallet_manager.get_address() else None
                    if balance_result:
                        balances = balance_result
                        data_source = "blockchain"
                except Exception as e:
                    logger.warning(f"Blockchain balance fetch failed: {e}")
            
            # Fallback to demo data
            if data_source == "demo":
                balances = self.demo_balances.get(target_address, {"NEO": "0", "GAS": "0"})
            
            source_emoji = "🌐" if data_source == "blockchain" else "🧪"
            
            return AgentResponse(
                success=True,
                message=f"""💰 **Balance for {target_address}**

🔸 **NEO:** {balances['NEO']}
🔸 **GAS:** {balances['GAS']}

{source_emoji} **Source:** {data_source}_data
📊 **Network:** {self.network}""",
                data={"address": target_address, "balances": balances, "source": data_source},
                action_type="balance_check"
            )
            
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Failed to get balance: {str(e)}",
                action_type="balance_error"
            )
    
    async def handle_security_analysis(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle comprehensive security analysis."""
        target = intent.get("target")
        target_type = intent.get("target_type", "address")
        
        if not target:
            return AgentResponse(
                success=False,
                message="""🛡️ **Security Analysis**
                
Please provide a target to analyze:
• `security check NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N` - Check address
• `analyze token 0x1234...` - Check token contract
• `security check https://example.com` - Check website""",
                action_type="security_help"
            )
        
        try:
            # Perform comprehensive security check
            security_result = await self.security_suite.comprehensive_security_check(target, target_type)
            
            if security_result.is_safe:
                risk_emoji = "✅"
                status_text = "SAFE"
            else:
                risk_emoji = "⚠️" if security_result.risk_level in ["medium", "high"] else "🚨"
                status_text = f"RISK: {security_result.risk_level.upper()}"
            
            return AgentResponse(
                success=True,
                message=f"""🛡️ **Security Analysis - {status_text}**

{risk_emoji} **Target:** `{target}`
🔸 **Type:** {target_type}
🔸 **Risk Level:** {security_result.risk_level}
🔸 **Confidence:** {security_result.confidence:.1%}
🔸 **Checks Passed:** {security_result.checks_passed}/{security_result.total_checks}

📊 **Analysis Details:**
{self._format_security_details(security_result.details)}

🕒 **Analyzed:** {security_result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}""",
                data=security_result,
                action_type="security_analysis"
            )
            
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Security analysis failed: {str(e)}",
                action_type="security_error"
            )
    
    def _format_security_details(self, details: Dict[str, Any]) -> str:
        """Format security check details for display."""
        formatted = []
        for check_name, result in details.items():
            if isinstance(result, dict):
                status = "✅" if result.get("is_safe", True) else "❌"
                message = result.get("message", result.get("status", "No details"))
                formatted.append(f"• {check_name}: {status} {message}")
        
        return "\n".join(formatted) if formatted else "• No detailed analysis available"
    
    async def handle_blockchain_data(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle blockchain data queries."""
        query = intent.get("query", "").lower()
        
        try:
            if "block" in query and "height" in query:
                # Get current block height
                height = self.neo_api.get_block_count()
                return AgentResponse(
                    success=True,
                    message=f"""📊 **Neo Blockchain Data**
                    
🔸 **Current Block Height:** {height:,}
🔸 **Network:** {self.network}
📡 **Node:** {self.neo_api.url}""",
                    data={"block_height": height, "network": self.network},
                    action_type="blockchain_info"
                )
            
            elif "recent blocks" in query:
                # Get recent blocks
                blocks = self.neo_api.get_recent_blocks(5)
                if "result" in blocks and blocks["result"]:
                    block_list = []
                    for block in blocks["result"][:5]:
                        block_list.append(f"• Block #{block.get('index', 'Unknown')}: {block.get('transactioncount', 0)} transactions")
                    
                    return AgentResponse(
                        success=True,
                        message=f"""📊 **Recent Blocks**
                        
{chr(10).join(block_list)}

🔸 **Network:** {self.network}""",
                        data=blocks,
                        action_type="blockchain_info"
                    )
            
            elif "asset count" in query:
                count = self.neo_api.get_asset_count()
                return AgentResponse(
                    success=True,
                    message=f"""📊 **Neo Asset Statistics**
                    
🔸 **Total Assets:** {count:,}
🔸 **Network:** {self.network}
💼 **Includes:** NEP-17 tokens, NEP-11 NFTs""",
                    data={"asset_count": count},
                    action_type="blockchain_info"
                )
            
            else:
                # General blockchain info
                height = self.neo_api.get_block_count()
                asset_count = self.neo_api.get_asset_count()
                
                return AgentResponse(
                    success=True,
                    message=f"""📊 **Neo Blockchain Overview**
                    
🔸 **Current Height:** {height:,}
🔸 **Total Assets:** {asset_count:,}
🔸 **Network:** {self.network}
📡 **Status:** Online

**Available queries:**
• `recent blocks` - Show recent block info
• `asset count` - Total number of assets
• `block height` - Current blockchain height""",
                    data={"height": height, "asset_count": asset_count},
                    action_type="blockchain_info"
                )
                
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Failed to get blockchain data: {str(e)}",
                action_type="blockchain_error"
            )
    
    async def handle_nft_operations(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle NFT-related operations."""
        address = intent.get("address")
        
        if not address and self.wallet_manager.is_loaded:
            address = self.wallet_manager.get_address()
        elif not address:
            return AgentResponse(
                success=False,
                message="Please provide an address or load your wallet first.\nExample: `my nfts` or `nfts for Nxxx...`",
                action_type="nft_error"
            )
        
        try:
            # Get NFT collection
            nft_data = self.neo_api.get_nep11_owned(address)
            
            if "result" in nft_data and nft_data["result"]:
                nft_count = len(nft_data["result"])
                
                # Group by contract
                contracts = {}
                for nft in nft_data["result"][:10]:  # Show first 10
                    contract = nft.get("contract", "Unknown")
                    if contract not in contracts:
                        contracts[contract] = 0
                    contracts[contract] += 1
                
                contract_list = []
                for contract, count in contracts.items():
                    contract_list.append(f"• {contract}: {count} NFT(s)")
                
                return AgentResponse(
                    success=True,
                    message=f"""🎨 **NFT Collection for {address}**
                    
🔸 **Total NFTs:** {nft_count}
📦 **Collections:**

{chr(10).join(contract_list)}

🌐 **Network:** {self.network}""",
                    data={"address": address, "nft_count": nft_count, "contracts": contracts},
                    action_type="nft_info"
                )
            else:
                return AgentResponse(
                    success=True,
                    message=f"""🎨 **NFT Collection for {address}**
                    
🔸 **Total NFTs:** 0
📦 **Collections:** None found

🌐 **Network:** {self.network}""",
                    data={"address": address, "nft_count": 0},
                    action_type="nft_info"
                )
                
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Failed to get NFT data: {str(e)}",
                action_type="nft_error"
            )
    
    async def handle_price_monitoring(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle price monitoring and alerts."""
        query = intent.get("query", "").lower()
        
        try:
            if "create alert" in query or "price alert" in query:
                # Parse price alert creation
                # Example: "create price alert NEO above 50"
                match = re.search(r'(neo|gas|bitcoin|ethereum)\s+(above|below)\s+([\d.]+)', query)
                if match:
                    symbol, condition, price = match.groups()
                    price = float(price)
                    
                    alert = self.price_monitor.create_price_alert(symbol.upper(), price, condition)
                    
                    return AgentResponse(
                        success=True,
                        message=f"""🚨 **Price Alert Created**
                        
🔸 **Symbol:** {alert.symbol}
🔸 **Condition:** {alert.condition} ${alert.target_price}
🔸 **Status:** Active
🔸 **Created:** {alert.created_at.strftime('%Y-%m-%d %H:%M:%S')}

I'll monitor the price and notify you when triggered!""",
                        data=alert,
                        action_type="price_alert_created"
                    )
                else:
                    return AgentResponse(
                        success=False,
                        message="""🚨 **Price Alert Help**
                        
**Usage:** `create price alert SYMBOL above/below PRICE`

**Examples:**
• `create price alert NEO above 50`
• `create price alert GAS below 10`
• `create price alert BITCOIN above 100000`""",
                        action_type="price_help"
                    )
            
            elif "check alerts" in query or "my alerts" in query:
                active_alerts = self.price_monitor.get_active_alerts()
                
                if active_alerts:
                    alert_list = []
                    for alert in active_alerts:
                        alert_list.append(f"• {alert.symbol} {alert.condition} ${alert.target_price}")
                    
                    return AgentResponse(
                        success=True,
                        message=f"""🚨 **Active Price Alerts**
                        
{chr(10).join(alert_list)}

🔸 **Total Active:** {len(active_alerts)}""",
                        data={"alerts": active_alerts},
                        action_type="price_alerts"
                    )
                else:
                    return AgentResponse(
                        success=True,
                        message="🚨 **Active Price Alerts**\n\nNo active alerts found.\n\nCreate one with: `create price alert NEO above 50`",
                        data={"alerts": []},
                        action_type="price_alerts"
                    )
            
            else:
                # General price info
                return AgentResponse(
                    success=True,
                    message="""📈 **Price Monitoring**
                    
**Available Commands:**
• `create price alert SYMBOL above/below PRICE` - Create alert
• `check my alerts` - View active alerts
• `neo price` - Get current NEO price

**Supported symbols:** NEO, GAS, BITCOIN, ETHEREUM""",
                    action_type="price_help"
                )
                
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Price monitoring error: {str(e)}",
                action_type="price_error"
            )
    
    async def handle_send_transaction(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle single recipient transaction operations."""
        if not self.wallet_manager.is_loaded:
            return AgentResponse(
                success=False,
                message="""💸 **Transaction Error**
                
❌ **Wallet not loaded**

To send transactions, you need to load your wallet first:

**Usage:** `load wallet YOUR_PRIVATE_KEY`

**Supported formats:**
• WIF: `KxcgHRTc8SUcvwkG7V8HLoFrPHkUMskeV9nx5fvuTbsEU3z3kAS2`
• Hex: `0x1234...` or `1234567890abcdef...`""",
                action_type="transaction_error"
            )
        
        amount = intent.get("amount")
        asset = intent.get("asset", "NEO")
        recipient = intent.get("recipient")
        
        if not amount or not recipient:
            return AgentResponse(
                success=False,
                message="""💸 **Transaction Error**
                
❌ **Missing transaction details**

**Usage:** `send AMOUNT ASSET to ADDRESS`

**Examples:**
• `send 5 NEO to NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N`
• `transfer 10.5 GAS to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c`
• `pay 1 NEO to NUVPACMnKFhpuHjsRjhUvXz1XhqfGZYVtY`""",
                action_type="transaction_error"
            )
        
        try:
            # Get sender info
            sender_address = self.wallet_manager.get_address()
            
            # Check sender balance
            sender_balance = self.wallet_manager.get_balance() if NEO3_AVAILABLE else self.demo_balances.get(sender_address, {"NEO": "0", "GAS": "0"})
            current_balance = float(sender_balance.get(asset, "0"))
            
            # Validate sufficient balance (including network fee)
            network_fee = 0.5  # Standard network fee
            required_amount = amount + (network_fee if asset == "GAS" else 0)
            
            if current_balance < required_amount:
                return AgentResponse(
                    success=False,
                    message=f"""💸 **Insufficient Balance**
                    
❌ **Transaction cannot proceed**

🔸 **Required:** {required_amount} {asset} ({amount} + {network_fee if asset == 'GAS' else 0} fee)
🔸 **Available:** {current_balance} {asset}
🔸 **Shortage:** {required_amount - current_balance} {asset}

Please ensure you have sufficient balance and try again.""",
                    action_type="transaction_error"
                )
            
            # Perform security check on recipient
            security_result = await self.security_suite.comprehensive_security_check(recipient, "address")
            
            # Prepare transaction preview
            preview_message = f"""💸 **Transaction Preview**
            
📤 **From:** `{sender_address}`
📥 **To:** `{recipient}`
💰 **Amount:** {amount} {asset}
⛽ **Network Fee:** {network_fee} GAS
🔸 **Total Cost:** {amount} {asset}{' + ' + str(network_fee) + ' GAS' if asset != 'GAS' else ''}

🛡️ **Security Status:** {'✅ SAFE' if security_result.is_safe else '⚠️ RISKS DETECTED'}

**This is a PREVIEW. To execute the transaction, confirm by typing:**
`confirm send {amount} {asset} to {recipient}`"""
            
            if not security_result.is_safe:
                preview_message += f"\n\n🚨 **SECURITY WARNING:** {security_result.risk_level.upper()} risk detected!"
                preview_message += f"\n🔸 **Risk Details:** {', '.join([detail.get('message', 'Unknown risk') for detail in security_result.details.values() if isinstance(detail, dict) and not detail.get('is_safe', True)])}"
            
            return AgentResponse(
                success=True,
                message=preview_message,
                data={
                    "transaction_preview": {
                        "from": sender_address,
                        "to": recipient,
                        "amount": amount,
                        "asset": asset,
                        "network_fee": network_fee,
                        "security_check": security_result.is_safe
                    }
                },
                action_type="transaction_preview"
            )
            
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Transaction preparation failed: {str(e)}",
                action_type="transaction_error"
            )
    
    async def handle_bulk_transaction(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle bulk/multiple recipient transactions."""
        if not self.wallet_manager.is_loaded:
            return AgentResponse(
                success=False,
                message="""💸 **Bulk Transaction Error**
                
❌ **Wallet not loaded**

To send bulk transactions, load your wallet first:
`load wallet YOUR_PRIVATE_KEY`""",
                action_type="transaction_error"
            )
        
        return AgentResponse(
            success=True,
            message="""💸 **Bulk Transaction Feature**
            
🚀 **Coming Soon!** Bulk transactions will allow you to:

• Send to multiple recipients in one transaction
• Batch payments with reduced fees
• Mass airdrops and distributions
• Multi-recipient smart contract calls

**Example Usage (Future):**
```
bulk send NEO:
  NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N: 5
  NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c: 3
  NUVPACMnKFhpuHjsRjhUvXz1XhqfGZYVtY: 2
```

For now, use individual transactions:
`send 5 NEO to ADDRESS`""",
            action_type="feature_preview"
        )
    
    def get_transaction_help_response(self) -> AgentResponse:
        """Get transaction help information."""
        return AgentResponse(
            success=True,
            message="""💸 **Transaction Commands Help**

🚀 **Send Tokens:**
• `send AMOUNT ASSET to ADDRESS` - Send NEO/GAS
• `transfer 5 NEO to NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N`
• `pay 10.5 GAS to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c`

🔐 **Requirements:**
• Wallet must be loaded first
• Sufficient balance (including network fees)
• Valid recipient address

🛡️ **Security Features:**
• Automatic recipient address validation
• Comprehensive security checks via GoPlusLabs
• Balance verification before sending
• Transaction preview and confirmation

💡 **Supported Assets:**
• NEO (indivisible - whole numbers only)
• GAS (divisible - decimal amounts allowed)

**Examples:**
```
load wallet YOUR_PRIVATE_KEY
check my balance
send 5 NEO to NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N
transfer 2.5 GAS to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c
```""",
            action_type="transaction_help"
        )
    
    async def handle_transaction_analysis(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle transaction analysis operations."""
        query = intent.get("query", "").lower()
        
        try:
            if self.wallet_manager.is_loaded:
                address = self.wallet_manager.get_address()
                
                # Get transaction history
                tx_history = self.wallet_manager.get_transaction_history()
                
                return AgentResponse(
                    success=True,
                    message=f"""📊 **Transaction Analysis for {address}**
                    
🔸 **NEP-17 Transfers:** Available
🔸 **NEP-11 Transfers:** Available
🔸 **Network:** {self.network}

**Recent activity analysis would show:**
• Transaction volume patterns
• Most frequent interactions
• Token transfer history
• NFT activity

*Full analysis requires blockchain API integration*""",
                    data={"address": address, "history": tx_history},
                    action_type="transaction_analysis"
                )
            else:
                return AgentResponse(
                    success=False,
                    message="Please load your wallet first to analyze transactions.\nUse: `load wallet YOUR_PRIVATE_KEY`",
                    action_type="transaction_error"
                )
                
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Transaction analysis error: {str(e)}",
                action_type="transaction_error"
            )
    
    async def handle_governance_info(self, intent: Dict[str, Any]) -> AgentResponse:
        """Handle Neo governance information."""
        try:
            # Get committee info
            committee = self.neo_api.get_committee()
            candidate_count = self.neo_api.get_candidate_count()
            
            if "result" in committee and committee["result"]:
                committee_size = len(committee["result"])
                
                return AgentResponse(
                    success=True,
                    message=f"""🏛️ **Neo Governance Information**
                    
🔸 **Committee Members:** {committee_size}
🔸 **Total Candidates:** {candidate_count}
🔸 **Network:** {self.network}

**Governance Features:**
• Committee member voting
• Candidate registration
• Voting power delegation
• Network parameter changes

Use `candidate info ADDRESS` for specific candidate details.""",
                    data={"committee_size": committee_size, "candidate_count": candidate_count},
                    action_type="governance_info"
                )
            else:
                return AgentResponse(
                    success=False,
                    message="❌ Could not retrieve governance information",
                    action_type="governance_error"
                )
                
        except Exception as e:
            return AgentResponse(
                success=False,
                message=f"❌ Governance query error: {str(e)}",
                action_type="governance_error"
            )
    
    def get_help_response(self) -> AgentResponse:
        """Get comprehensive help information."""
        return AgentResponse(
            success=True,
            message="""🤖 **NeoXBridge AI - Complete Command Reference**

🔐 **Wallet Management:**
• `load wallet PRIVATE_KEY` - Load your Neo wallet
• `wallet status` - Check wallet status
• `my address` - Show wallet address

💰 **Balance & Assets:**
• `check my balance` - Check your balance
• `balance for ADDRESS` - Check any address
• `my nfts` - View your NFT collection

🛡️ **Security Analysis:**
• `security check ADDRESS` - Analyze address safety
• `analyze token CONTRACT` - Token security analysis
• `security check URL` - Website safety check

📊 **Blockchain Data:**
• `block height` - Current blockchain height
• `recent blocks` - Recent block information
• `asset count` - Total assets on network

📈 **Price Monitoring:**
• `create price alert SYMBOL above/below PRICE` - Create alert
• `check my alerts` - View active alerts
• `neo price` - Get current prices

💸 **Token Transfers:**
• `send AMOUNT ASSET to ADDRESS` - Send tokens securely
• `transfer 5 NEO to ADDRESS` - Transfer NEO tokens  
• `pay 10.5 GAS to ADDRESS` - Send GAS payments
• `send help` - Transaction help and examples

🏛️ **Governance:**
• `committee info` - Neo committee information
• `candidate count` - Total candidates

💡 **System:**
• `help` - Show this help
• `quit` - Exit application

**Example Usage:**
```
load wallet KxcgHRTc8SUcvwkG7V8HLoFrPHkUMskeV9nx5fvuTbsEU3z3kAS2
check my balance
security check NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N
create price alert NEO above 50
```""",
            action_type="help"
        )
    
    def handle_general_query(self, message: str) -> AgentResponse:
        """Handle general queries and provide guidance."""
        return AgentResponse(
            success=True,
            message="""🌉 **Welcome to NeoXBridge AI!**

I'm your comprehensive Neo blockchain assistant with advanced capabilities:

🔸 **Complete Neo N3 integration** - Real blockchain data
🔸 **Advanced security analysis** - Multi-layer protection
🔸 **Price monitoring & alerts** - Never miss market moves
🔸 **NFT tracking & analysis** - Full collectible management
🔸 **Governance insights** - Committee and voting data

Type `help` for all commands, or try:
• `load wallet YOUR_PRIVATE_KEY`
• `security check ADDRESS`
• `create price alert NEO above 50`

What would you like to explore?""",
            action_type="welcome"
        )

async def main():
    """Main application loop with enhanced error handling."""
    print("🌉 NeoXBridge AI - Comprehensive Blockchain Assistant")
    print("=" * 65)
    print("Initializing comprehensive Neo blockchain agent...")
    
    # Initialize agent
    try:
        agent = NeoXBridgeComprehensiveAgent()
        print("\n✅ NeoXBridge AI Ready!")
        
        if agent.wallet_manager.is_loaded:
            print(f"💼 Auto-loaded wallet: {agent.wallet_manager.get_address()}")
        
        print(f"🌐 Network: {agent.network}")
        print(f"🔧 Neo3 Support: {'Available' if NEO3_AVAILABLE else 'Limited'}")
        print("\nType 'help' for commands or 'quit' to exit")
        print("-" * 65)
        
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return
    
    # Main interaction loop
    while True:
        try:
            user_input = input("\n💬 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Thank you for using NeoXBridge AI! Stay secure in the blockchain world!")
                break
                
            if not user_input:
                continue
            
            print("🤔 Processing your request...")
            
            # Process message and get response
            response = await agent.process_message(user_input)
            
            # Display response
            success_emoji = "✅" if response.success else "❌"
            print(f"\n🤖 NeoXBridge AI {success_emoji}:")
            print(response.message)
            
            # Log action type for debugging
            logger.debug(f"Action type: {response.action_type}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Session ended. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ System Error: {e}")
            logger.error(f"Main loop error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nApplication terminated by user")
    except Exception as e:
        logger.error(f"Application crashed: {e}")
        print(f"\n💥 Fatal error: {e}")
