"""
NeoXBridge AI - Prompts and Response Templates
System prompts and contextual response generation for conversational AI.
"""

from typing import Dict, Any

SYSTEM_PROMPT = """
You are NeoXBridge AI, a secure conversational assistant for NeoX blockchain operations.

Your primary role is to help users safely interact with the NeoX blockchain through natural language commands.

## CORE CAPABILITIES:
• 🔍 Validate Neo wallet addresses and check their network existence
• 💰 Check NEO and GAS token balances for any address
• 🚀 Send NEO/GAS tokens securely with built-in malicious address detection
• 📊 Check transaction status and provide detailed information
• 🛡️ Integrate with GoPlus Labs for real-time security analysis

## SECURITY-FIRST APPROACH:
🔒 ALWAYS validate addresses before any transaction
🔒 ALWAYS run malicious address checks via GoPlus Labs before sending tokens
🔒 ALWAYS confirm transaction details with the user before execution
🔒 NEVER proceed with transactions to flagged addresses
🔒 Provide clear security warnings and explanations

## CONVERSATION STYLE:
• Be friendly, professional, and conversational
• Use clear, non-technical language for explanations
• Provide detailed confirmations for all operations
• Use emojis and visual formatting to make responses engaging
• Always prioritize user safety over convenience
• Explain blockchain concepts when needed, but keep it simple

## IMPORTANT REMINDERS:
- NEO addresses are 34 characters long and start with 'N'
- Always confirm recipient addresses before sending
- Transaction fees (GAS) will be automatically calculated
- All transactions are irreversible once confirmed
- Security checks may take a few moments - this is normal and important

Your goal is to make blockchain interactions as simple and safe as texting a friend, while maintaining the highest security standards.
"""


def get_contextual_response(response_type: str, context: Dict[str, Any]) -> str:
    """
    Generate contextual responses based on operation type and results.
    
    Args:
        response_type (str): Type of response needed
        context (dict): Context data for response generation
        
    Returns:
        str: Formatted response string
    """
    
    if response_type == "address_validation":
        return _format_address_validation_response(context)
    elif response_type == "balance_check":
        return _format_balance_response(context)
    elif response_type == "send_transaction":
        return _format_transaction_response(context)
    elif response_type == "transaction_check":
        return _format_transaction_status_response(context)
    elif response_type == "security_check":
        return _format_security_response(context)
    elif response_type == "general_help":
        return _format_help_response(context)
    else:
        return "I'm not sure how to help with that. Type 'help' to see what I can do!"


def _format_address_validation_response(context: Dict[str, Any]) -> str:
    """Format address validation response."""
    address = context["address"]
    result = context["result"]
    
    if result["is_valid"]:
        return f"""✅ **Address Validation Successful**

🔍 Address: `{address}`
📍 Status: Valid and found on NeoX network
🛡️ Security: Verified format and network presence

This address is ready to use for transactions! Would you like me to:
• Check the balance for this address
• Send tokens to this address
• Run a security check"""
    
    elif result["format_valid"]:
        return f"""⚠️ **Address Format Valid but Not Found**

🔍 Address: `{address}`
📍 Status: Valid format but not found on network
🛡️ Security: Format verified

The address format is correct, but it wasn't found on the NeoX network. This could mean:
• It's a new address that hasn't been used yet
• There might be a typo in the address
• It could be from a different blockchain network

Double-check the address before using it for transactions."""
    
    else:
        return f"""❌ **Invalid Address Format**

🔍 Address: `{address}`
📍 Status: Invalid format
🛡️ Security: Format validation failed

**Issue:** {result["reason"]}

💡 **Neo Address Requirements:**
• Must be exactly 34 characters long
• Must start with the letter 'N'
• Contains only alphanumeric characters
• Example: `NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N`

Please check the address and try again."""


def _format_balance_response(context: Dict[str, Any]) -> str:
    """Format balance check response."""
    address = context["address"]
    result = context["result"]
    
    if result["success"]:
        balances = result["balances"]
        
        if any(float(balance) > 0 for balance in balances.values()):
            balance_lines = []
            for asset, amount in balances.items():
                balance_lines.append(f"  • {asset}: {amount}")
            
            balance_str = "\n".join(balance_lines)
            
            return f"""💰 **Balance Information**

🔍 Address: `{address}`
📊 Current Balances:
{balance_str}

💡 **Tip:** NEO generates GAS over time. GAS is used for transaction fees.

Need to do anything else? I can help you:
• Send tokens to another address
• Validate a different address
• Check transaction history"""
        
        else:
            return f"""💰 **Balance Information**

🔍 Address: `{address}`
📊 Current Balances: 
  • NEO: 0.0
  • GAS: 0.0

This address currently has no tokens. To get started:
• Receive tokens from another address
• Purchase tokens on an exchange
• Check if this is the correct address"""
    
    else:
        return f"""❌ **Balance Check Failed**

🔍 Address: `{address}`
📊 Error: {result["error"]}

Please verify the address is correct and try again."""


def _format_transaction_response(context: Dict[str, Any]) -> str:
    """Format transaction response."""
    result = context["result"]
    
    if result["success"]:
        return f"""🚀 **Transaction Successful!**

├─ Asset: {result["asset"]}
├─ Amount: {result["amount"]}
├─ Recipient: `{result["recipient"]}`
├─ Transaction Hash: `{result["tx_hash"]}`
├─ Block Height: {result["block_height"]}
└─ Status: ✅ {result["status"].upper()}

⚡ Your {result["amount"]} {result["asset"]} has been sent successfully!

🎯 **Next Steps:**
• Save the transaction hash for your records
• It may take a few minutes to appear in block explorers
• The recipient will see the tokens once the transaction is confirmed

Would you like me to check the transaction status or help with anything else?"""
    
    elif result.get("security_blocked"):
        return f"""🚨 **SECURITY ALERT - Transaction Blocked**

⚠️ **Security Warning:** {result["error"]}

For your safety, this transaction has been automatically blocked.

🛡️ **What this means:**
• The recipient address has been flagged as potentially dangerous
• This could be a phishing scam or malicious contract
• Your funds are safe because the transaction was prevented

🔒 **What to do:**
• Verify the recipient address through a trusted channel
• Double-check you have the correct address
• Only proceed if you're absolutely certain the address is legitimate"""
    
    else:
        return f"""❌ **Transaction Failed**

🚫 Error: {result["error"]}

Please check your inputs and try again:
• Verify the recipient address is correct
• Ensure you have sufficient balance
• Check that the amount is valid

Need help? I can assist you with:
• Validating the recipient address
• Checking your current balance
• Understanding transaction requirements"""


def _format_transaction_status_response(context: Dict[str, Any]) -> str:
    """Format transaction status response."""
    result = context["result"]
    tx_hash = context["tx_hash"]
    
    if result["success"]:
        return f"""📊 **Transaction Status**

🔍 Hash: `{tx_hash}`
📈 Status: ✅ {result["status"].upper()}
🏗️ Block Height: {result["block_height"]}
✔️ Confirmations: {result["confirmations"]}
⛽ GAS Consumed: {result["gas_consumed"]}
🕐 Timestamp: {result["timestamp"]}
💸 Network Fee: {result["network_fee"]}

Your transaction has been successfully confirmed on the NeoX blockchain!"""
    
    else:
        return f"""❌ **Transaction Status Check Failed**

🔍 Hash: `{tx_hash}`
📊 Error: {result["error"]}

Please verify the transaction hash is correct. Transaction hashes should:
• Start with '0x'
• Be exactly 66 characters long
• Contain only hexadecimal characters (0-9, a-f)"""


def _format_security_response(context: Dict[str, Any]) -> str:
    """Format security check response."""
    address = context["address"]
    result = context["result"]
    
    if result["is_malicious"]:
        return f"""🚨 **SECURITY ALERT - MALICIOUS ADDRESS DETECTED**

⚠️ Address: `{address}`
🛡️ Risk Level: {result["risk_level"].upper()}
📊 Confidence: {int(result["confidence"] * 100)}%
🔍 Source: {result["source"]}

**⛔ DO NOT SEND TOKENS TO THIS ADDRESS**

🚫 **Why this address is dangerous:**
{result["reason"]}

🔒 **This could be:**
• A phishing scam designed to steal your tokens
• A malicious contract that could drain your wallet
• A known fraudulent address from our security database

**✅ What to do:**
• Find an alternative, verified address
• Contact the recipient through a trusted channel
• Report this address if you encountered it in suspicious circumstances"""
    
    elif result["is_safe"]:
        risk_emoji = "🟢" if result["risk_level"] == "low" else "🟡"
        
        return f"""✅ **Security Check Passed**

{risk_emoji} Address: `{address}`
🛡️ Risk Level: {result["risk_level"].capitalize()}
📊 Confidence: {int(result["confidence"] * 100)}%
🔍 Source: {result["source"]}

**Assessment:** {result["reason"]}

This address appears to be safe for transactions. However, always:
• Double-check the address with the recipient
• Start with small amounts for new addresses
• Verify through multiple sources when possible

Would you like me to help you with the next step?"""
    
    else:
        return f"""⚠️ **Security Check Warning**

🔍 Address: `{address}`
🛡️ Risk Level: {result["risk_level"].capitalize()}
📊 Assessment: {result["reason"]}

While this address isn't flagged as malicious, please exercise caution:
• Verify the address with the intended recipient
• Ensure you have the correct address
• Consider starting with a small test transaction

Would you like me to help validate the address format or check something else?"""


def _format_help_response(context: Dict[str, Any]) -> str:
    """Format general help response."""
    return """🤖 **NeoXBridge AI - Your Blockchain Assistant**

I can help you with secure NeoX blockchain operations:

🔍 **Address Operations:**
• "Validate address [your_address]"
• "Check balance for [address]"
• "Is this address safe: [address]"

💸 **Transaction Operations:**
• "Send 10 NEO to [recipient_address]"
• "Transfer 5.5 GAS to [address]"
• "Check transaction status [hash]"

🛡️ **Security Features:**
• Automatic malicious address detection
• Transaction confirmation workflows
• Real-time security validation

💡 **Tips:**
• Just speak naturally! I understand conversational requests
• I'll always run security checks before transactions
• All operations prioritize your safety

**Example:** "Send 25 NEO to NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N"

What would you like to do today?"""
