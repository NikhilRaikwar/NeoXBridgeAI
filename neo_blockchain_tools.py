"""
NeoXBridge AI - Comprehensive Neo Blockchain Tools
Complete Neo N3 API toolkit integrated directly into the main agent
"""

import requests
import json
import os
import getpass
from typing import Annotated, Any, Dict, List, Optional
from decimal import Decimal
from datetime import datetime
import asyncio
import aiohttp
import logging

# Neo3 imports
try:
    import neo3.wallet.utils
    from neo3.wallet.account import Account
    NEO3_AVAILABLE = True
except ImportError:
    NEO3_AVAILABLE = False

logger = logging.getLogger(__name__)

class NeoAPIClient:
    """Complete Neo N3 API client for blockchain operations."""
    
    def __init__(self, network: str = "testnet"):
        self.mainnet_url = "https://explorer.onegate.space/api"
        self.testnet_url = "https://testmagnet.explorer.onegate.space/api"
        
        self.network = network
        self.url = self.testnet_url if network == "testnet" else self.mainnet_url
        
        # Standard Neo/GAS contract hashes
        self.NEO_CONTRACT = "0xef4073a0f2b305a38ec4050e4d3d28bc40ea63f5"
        self.GAS_CONTRACT = "0xd2a4cff31913016155e38e474a2c06d08be276cf"
        
    def _make_request(self, method: str, params: Dict = None) -> Dict[str, Any]:
        """Make RPC request to Neo API."""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "id": 1
        }
        
        try:
            response = requests.post(self.url, json=payload, timeout=30)
            return response.json()
        except Exception as e:
            logger.error(f"API request failed: {e}")
            return {"error": str(e)}
    
    def convert_address_to_script_hash(self, address: str) -> str:
        """Convert Neo address to script hash."""
        if NEO3_AVAILABLE and neo3.wallet.utils.is_valid_address(address):
            return "0x" + neo3.wallet.utils.address_to_script_hash(address=address).__str__()
        return address
    
    def convert_asset_amount_string(self, amount_str: str, decimals: int) -> str:
        """Convert raw asset amount to human readable format."""
        try:
            amount = Decimal(amount_str)
            divisor = Decimal(10) ** decimals
            result = amount / divisor
            return str(result)
        except:
            return "0"
    
    # === Address Information ===
    def get_address_info(self, address: str) -> Dict[str, Any]:
        """Get detailed address information."""
        script_hash = self.convert_address_to_script_hash(address)
        result = self._make_request("GetAddressInfoByAddress", {"address": script_hash})
        
        if "result" in result:
            data = result["result"]
            return {
                "address": data.get("address"),
                "first_use_time": datetime.fromtimestamp(data.get("firstusetime", 0) / 1000).strftime('%Y-%m-%d %H:%M:%S'),
                "last_use_time": datetime.fromtimestamp(data.get("lastusetime", 0) / 1000).strftime('%Y-%m-%d %H:%M:%S'),
                "transactions_sent": data.get("transactionssent", 0)
            }
        return result
    
    def get_assets_by_address(self, address: str) -> Dict[str, Any]:
        """Get all assets held by an address."""
        script_hash = self.convert_address_to_script_hash(address)
        result = self._make_request("GetAssetsHeldByAddress", {"Address": script_hash})
        
        if "result" in result and "result" in result["result"]:
            assets = result["result"]["result"]
            processed_assets = []
            
            for asset in assets:
                asset_hash = asset.get("asset")
                balance_raw = asset.get("balance", "0")
                
                # Get asset info for decimals and symbol
                asset_info = self.get_asset_info_by_hash(asset_hash)
                if isinstance(asset_info, dict) and "symbol" in asset_info:
                    decimals = int(asset_info.get("decimals", 0))
                    symbol = asset_info.get("symbol", "UNKNOWN")
                    balance_formatted = self.convert_asset_amount_string(balance_raw, decimals)
                    
                    processed_assets.append({
                        "symbol": symbol,
                        "balance": balance_formatted,
                        "raw_balance": balance_raw,
                        "contract_hash": asset_hash,
                        "decimals": decimals
                    })
            
            return {"assets": processed_assets}
        
        return result
    
    def get_asset_info_by_hash(self, asset_hash: str) -> Dict[str, Any]:
        """Get asset information by contract hash."""
        result = self._make_request("GetAssetInfoByContractHash", {"ContractHash": asset_hash})
        
        if "result" in result:
            return result["result"]
        return result
    
    def get_asset_info_by_name(self, asset_name: str) -> Dict[str, Any]:
        """Get asset information by name (fuzzy search)."""
        result = self._make_request("GetAssetInfosByName", {"Name": asset_name})
        return result
    
    # === Block Information ===
    def get_block_count(self) -> int:
        """Get current block height."""
        result = self._make_request("GetBlockCount")
        if "result" in result:
            return result["result"]["index"]
        return 0
    
    def get_best_block_hash(self) -> str:
        """Get the latest block hash."""
        result = self._make_request("GetBestBlockHash")
        if "result" in result:
            return result["result"]["hash"]
        return ""
    
    def get_block_by_height(self, height: int) -> Dict[str, Any]:
        """Get block information by height."""
        result = self._make_request("GetBlockByBlockHeight", {"BlockHeight": height})
        return result
    
    def get_block_by_hash(self, block_hash: str) -> Dict[str, Any]:
        """Get block information by hash."""
        result = self._make_request("GetBlockByBlockHash", {"BlockHash": block_hash})
        return result
    
    def get_recent_blocks(self, limit: int = 10) -> Dict[str, Any]:
        """Get recent block information."""
        result = self._make_request("GetBlockInfoList", {"Limit": limit})
        return result
    
    # === Transaction Information ===
    def get_application_log(self, tx_hash: str) -> Dict[str, Any]:
        """Get application log by transaction hash."""
        result = self._make_request("GetApplicationLogByTransactionHash", {"TransactionHash": tx_hash})
        return result
    
    def get_daily_transactions(self, days: int = 7) -> List[int]:
        """Get daily transaction counts."""
        result = self._make_request("GetDailyTransactions", {"Days": days})
        if "result" in result and isinstance(result["result"], list):
            return [item["DailyTransactions"] for item in result["result"] if "DailyTransactions" in item]
        return []
    
    def get_hourly_transactions(self, hours: int = 24) -> List[int]:
        """Get hourly transaction counts."""
        result = self._make_request("GetHourlyTransactions", {"Hours": hours})
        if "result" in result and isinstance(result["result"], list):
            return [item["HourlyTransactions"] for item in result["result"] if "HourlyTransactions" in item]
        return []
    
    # === NEP-17 Token Operations ===
    def get_nep17_transfers(self, address: str) -> Dict[str, Any]:
        """Get NEP-17 token transfer history for address."""
        script_hash = self.convert_address_to_script_hash(address)
        result = self._make_request("GetNep17TransferByAddress", {"Address": script_hash})
        return result
    
    def get_nep17_transfers_by_block(self, block_height: int) -> Dict[str, Any]:
        """Get NEP-17 transfers in a specific block."""
        result = self._make_request("GetNep17TransferByBlockHeight", {"BlockHeight": block_height})
        return result
    
    # === NEP-11 NFT Operations ===
    def get_nep11_owned(self, address: str) -> Dict[str, Any]:
        """Get NFTs owned by address."""
        script_hash = self.convert_address_to_script_hash(address)
        result = self._make_request("GetNep11OwnedByAddress", {"Address": script_hash})
        return result
    
    def get_nep11_transfers(self, address: str) -> Dict[str, Any]:
        """Get NFT transfer history for address."""
        script_hash = self.convert_address_to_script_hash(address)
        result = self._make_request("GetNep11TransferByAddress", {"Address": script_hash})
        return result
    
    def get_nep11_balance(self, contract_hash: str, address: str, token_id: str) -> Dict[str, Any]:
        """Get specific NFT balance."""
        script_hash = self.convert_address_to_script_hash(address)
        result = self._make_request("GetNep11BalanceByContractHashAddressTokenId", {
            "ContractHash": contract_hash,
            "Address": script_hash,
            "tokenId": token_id
        })
        return result
    
    # === Contract Information ===
    def get_contract_by_hash(self, contract_hash: str) -> Dict[str, Any]:
        """Get contract information by hash."""
        result = self._make_request("GetContractByContractHash", {"ContractHash": contract_hash})
        return result
    
    def get_contracts_by_name(self, name: str) -> Dict[str, Any]:
        """Get contracts by name (fuzzy search)."""
        result = self._make_request("GetContractListByName", {"Name": name})
        return result
    
    def get_contract_count(self) -> int:
        """Get total contract count."""
        result = self._make_request("GetContractCount")
        if "result" in result:
            return result["result"]["total counts"]
        return 0
    
    # === Governance Operations ===
    def get_committee(self) -> Dict[str, Any]:
        """Get current committee members."""
        result = self._make_request("GetCommittee")
        return result
    
    def get_candidate_by_address(self, address: str) -> Dict[str, Any]:
        """Get candidate information by address."""
        script_hash = self.convert_address_to_script_hash(address)
        result = self._make_request("GetCandidateByAddress", {"Address": script_hash})
        return result
    
    def get_candidate_by_voter(self, voter_address: str) -> Dict[str, Any]:
        """Get candidate voted by specific voter."""
        script_hash = self.convert_address_to_script_hash(voter_address)
        result = self._make_request("GetCandidateByVoterAddress", {"VoterAddress": script_hash})
        return result
    
    def get_candidate_count(self) -> int:
        """Get total candidate count."""
        result = self._make_request("GetCandidateCount")
        if "result" in result:
            return result["result"]["total counts"]
        return 0
    
    # === Statistics ===
    def get_active_addresses(self, days: int = 7) -> List[int]:
        """Get active address counts for past days."""
        result = self._make_request("GetActiveAddresses", {"Days": days})
        if "result" in result and isinstance(result["result"], list):
            return [item["ActiveAddresses"] for item in result["result"] if "ActiveAddresses" in item]
        return []
    
    def get_address_count(self) -> int:
        """Get total address count."""
        result = self._make_request("GetAddressCount")
        if "result" in result:
            return result["result"]["total counts"]
        return 0
    
    def get_asset_count(self) -> int:
        """Get total asset count."""
        result = self._make_request("GetAssetCount")
        if "result" in result:
            return result["result"]["total counts"]
        return 0

class AdvancedNeoWalletManager:
    """Advanced Neo wallet management with full blockchain integration."""
    
    def __init__(self, network: str = "testnet"):
        self.private_key = None
        self.wallet_address = None
        self.account = None
        self.is_loaded = False
        self.api_client = NeoAPIClient(network)
        
    def load_from_env(self) -> bool:
        """Load wallet from environment variables."""
        private_key = os.getenv("PRIVATE_KEY")
        if private_key:
            return self.load_private_key(private_key)
        return False
    
    def load_private_key(self, private_key: str) -> bool:
        """Load private key and derive wallet address using neo-mamba."""
        try:
            self.private_key = private_key.strip()
            
            if not NEO3_AVAILABLE:
                logger.warning("Neo3 libraries not available, limited functionality")
                return False
            
            # Handle different private key formats
            if self.private_key.startswith('K') or self.private_key.startswith('L'):
                # WIF format
                self.account = Account.from_wif(self.private_key, "")
                self.wallet_address = self.account.address
                logger.info(f"✅ Derived address from WIF: {self.wallet_address}")
                
            elif len(self.private_key) == 66 and self.private_key.startswith('0x'):
                # Hex with 0x prefix
                private_key_bytes = bytes.fromhex(self.private_key[2:])
                self.account = Account.from_private_key(private_key_bytes)
                self.wallet_address = self.account.address
                logger.info(f"✅ Derived address from hex: {self.wallet_address}")
                
            elif len(self.private_key) == 64:
                # Raw hex format
                private_key_bytes = bytes.fromhex(self.private_key)
                self.account = Account.from_private_key(private_key_bytes)
                self.wallet_address = self.account.address
                logger.info(f"✅ Derived address from raw hex: {self.wallet_address}")
                
            else:
                logger.error("❌ Invalid private key format")
                return False
            
            self.is_loaded = True
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to load private key: {e}")
            return False
    
    def get_address(self) -> Optional[str]:
        """Get the wallet address."""
        return self.wallet_address if self.is_loaded else None
    
    def get_balance(self) -> Dict[str, str]:
        """Get wallet balance for NEO and GAS."""
        if not self.is_loaded:
            return {"NEO": "0", "GAS": "0"}
        
        try:
            assets_result = self.api_client.get_assets_by_address(self.wallet_address)
            if "assets" in assets_result:
                balances = {"NEO": "0", "GAS": "0"}
                for asset in assets_result["assets"]:
                    symbol = asset["symbol"]
                    if symbol in ["NEO", "GAS"]:
                        balances[symbol] = asset["balance"]
                return balances
        except Exception as e:
            logger.error(f"Failed to get balance: {e}")
        
        return {"NEO": "0", "GAS": "0"}
    
    def get_transaction_history(self) -> Dict[str, Any]:
        """Get transaction history for the wallet."""
        if not self.is_loaded:
            return {}
        
        try:
            # Get NEP-17 transfers
            nep17_transfers = self.api_client.get_nep17_transfers(self.wallet_address)
            
            # Get NEP-11 transfers
            nep11_transfers = self.api_client.get_nep11_transfers(self.wallet_address)
            
            return {
                "nep17_transfers": nep17_transfers,
                "nep11_transfers": nep11_transfers
            }
        except Exception as e:
            logger.error(f"Failed to get transaction history: {e}")
            return {}
    
    def get_nft_collection(self) -> Dict[str, Any]:
        """Get NFT collection owned by the wallet."""
        if not self.is_loaded:
            return {}
        
        try:
            return self.api_client.get_nep11_owned(self.wallet_address)
        except Exception as e:
            logger.error(f"Failed to get NFT collection: {e}")
            return {}

class ComprehensiveSecurityChecker:
    """Enhanced security checker with multiple validation layers."""
    
    def __init__(self):
        self.goplus_api_key = os.getenv("GOPLUS_API_KEY") or os.getenv("GO_PLUS_LABS_APP_KEY")
        self.base_url = "https://api.gopluslabs.io"
    
    async def check_address_security(self, address: str) -> Dict[str, Any]:
        """Comprehensive address security check."""
        results = {
            "address": address,
            "is_safe": True,
            "risk_level": "low",
            "checks": {}
        }
        
        # Format validation
        results["checks"]["format"] = self._check_address_format(address)
        
        # GoPlusLabs API check
        if self.goplus_api_key:
            results["checks"]["goplus"] = await self._check_goplus_security(address)
        else:
            results["checks"]["goplus"] = {
                "status": "skipped",
                "reason": "API key not configured"
            }
        
        # Neo network validation
        results["checks"]["neo_network"] = self._check_neo_network_validity(address)
        
        # Determine overall safety
        overall_safe = all(
            check.get("is_safe", True) for check in results["checks"].values()
            if isinstance(check, dict) and "is_safe" in check
        )
        
        results["is_safe"] = overall_safe
        results["risk_level"] = self._calculate_risk_level(results["checks"])
        
        return results
    
    def _check_address_format(self, address: str) -> Dict[str, Any]:
        """Check Neo address format."""
        if not address or len(address) != 34 or not address.startswith('N'):
            return {
                "is_safe": False,
                "status": "invalid_format",
                "message": "Invalid Neo address format"
            }
        
        if NEO3_AVAILABLE:
            try:
                is_valid = neo3.wallet.utils.is_valid_address(address)
                return {
                    "is_safe": is_valid,
                    "status": "valid" if is_valid else "invalid",
                    "message": "Address format validation complete"
                }
            except:
                pass
        
        return {
            "is_safe": True,
            "status": "basic_validation",
            "message": "Basic format validation passed"
        }
    
    async def _check_goplus_security(self, address: str) -> Dict[str, Any]:
        """Check address against GoPlusLabs database."""
        try:
            url = f"{self.base_url}/api/v1/address_security/{address}"
            headers = {"Authorization": f"Bearer {self.goplus_api_key}"}
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        result = data.get("result", {})
                        
                        malicious_flags = [
                            "blacklist_doubt", "blackmail_activities", "cybercrime",
                            "darkweb_transactions", "financial_crime", "fake_token",
                            "honeypot_related_address", "malicious_mining_activities",
                            "mixer", "money_laundering", "phishing_activities", "stealing_attack"
                        ]
                        
                        detected_flags = [flag for flag in malicious_flags if result.get(flag) == "1"]
                        is_malicious = len(detected_flags) > 0
                        
                        return {
                            "is_safe": not is_malicious,
                            "status": "flagged" if is_malicious else "clean",
                            "detected_flags": detected_flags,
                            "message": f"GoPlusLabs check: {'Flagged' if is_malicious else 'Clean'}"
                        }
            
            return {
                "is_safe": True,
                "status": "api_error",
                "message": "Could not verify with GoPlusLabs"
            }
                    
        except Exception as e:
            logger.warning(f"GoPlusLabs check failed: {e}")
            return {
                "is_safe": True,
                "status": "check_failed",
                "message": f"Security check failed: {str(e)}"
            }
    
    def _check_neo_network_validity(self, address: str) -> Dict[str, Any]:
        """Check if address exists on Neo network."""
        try:
            # This is a placeholder - would require actual network check
            return {
                "is_safe": True,
                "status": "assumed_valid",
                "message": "Address format suggests Neo network compatibility"
            }
        except Exception as e:
            return {
                "is_safe": True,
                "status": "check_failed",
                "message": f"Network check failed: {str(e)}"
            }
    
    def _calculate_risk_level(self, checks: Dict[str, Any]) -> str:
        """Calculate overall risk level based on checks."""
        unsafe_checks = sum(1 for check in checks.values() 
                          if isinstance(check, dict) and not check.get("is_safe", True))
        
        if unsafe_checks == 0:
            return "low"
        elif unsafe_checks <= 1:
            return "medium"
        else:
            return "high"

# Export classes for use in main agent
__all__ = [
    'NeoAPIClient',
    'AdvancedNeoWalletManager', 
    'ComprehensiveSecurityChecker',
    'NEO3_AVAILABLE'
]
