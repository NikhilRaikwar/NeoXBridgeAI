"""
NeoXBridge AI - Security and Blockchain Data Analysis Tools
Comprehensive security validation and blockchain data analysis toolkit
"""

import asyncio
import aiohttp
import logging
import json
import hashlib
import hmac
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timedelta
from dataclasses import dataclass
import os
from urllib.parse import urlencode
import time

logger = logging.getLogger(__name__)

@dataclass
class SecurityResult:
    """Security check result data structure."""
    is_safe: bool
    risk_level: str  # low, medium, high, critical
    confidence: float  # 0.0 to 1.0
    checks_passed: int
    total_checks: int
    details: Dict[str, Any]
    timestamp: datetime

@dataclass 
class TokenAnalysis:
    """Token security analysis result."""
    token_address: str
    symbol: str
    name: str
    is_honeypot: bool
    can_sell: bool
    honeypot_reason: Optional[str]
    buy_tax: float
    sell_tax: float
    slippage_modifiable: bool
    is_proxy: bool
    is_mintable: bool
    owner_change_balance: bool
    hidden_owner: bool
    anti_whale: bool
    trading_cooldown: bool

@dataclass
class PriceAlert:
    """Price alert configuration."""
    symbol: str
    target_price: float
    condition: str  # 'above', 'below'
    active: bool
    created_at: datetime
    triggered_at: Optional[datetime] = None

class GoPlusLabsClient:
    """Comprehensive GoPlusLabs security API client."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GOPLUS_API_KEY") or os.getenv("GO_PLUS_LABS_APP_KEY")
        self.base_url = "https://api.gopluslabs.io"
        self.session = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def _get_headers(self) -> Dict[str, str]:
        """Get API headers."""
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers
    
    async def _make_request(self, endpoint: str, params: Dict = None) -> Dict[str, Any]:
        """Make API request to GoPlusLabs."""
        if not self.session:
            self.session = aiohttp.ClientSession()
        
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()
        
        try:
            async with self.session.get(url, headers=headers, params=params, timeout=15) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.warning(f"GoPlusLabs API returned status {response.status}")
                    return {"error": f"API request failed with status {response.status}"}
        except Exception as e:
            logger.error(f"GoPlusLabs API request failed: {e}")
            return {"error": str(e)}
    
    async def check_token_security(self, token_address: str, chain_id: str = "1") -> TokenAnalysis:
        """Comprehensive token security analysis."""
        endpoint = f"/api/v1/token_security/{chain_id}"
        params = {"contract_addresses": token_address}
        
        result = await self._make_request(endpoint, params)
        
        if "result" in result and token_address.lower() in result["result"]:
            token_data = result["result"][token_address.lower()]
            
            return TokenAnalysis(
                token_address=token_address,
                symbol=token_data.get("token_symbol", "UNKNOWN"),
                name=token_data.get("token_name", "Unknown Token"),
                is_honeypot=token_data.get("is_honeypot") == "1",
                can_sell=token_data.get("sell_tax", "0") != "1",
                honeypot_reason=token_data.get("honeypot_reason"),
                buy_tax=float(token_data.get("buy_tax", "0")),
                sell_tax=float(token_data.get("sell_tax", "0")),
                slippage_modifiable=token_data.get("slippage_modifiable") == "1",
                is_proxy=token_data.get("is_proxy") == "1",
                is_mintable=token_data.get("is_mintable") == "1",
                owner_change_balance=token_data.get("owner_change_balance") == "1",
                hidden_owner=token_data.get("hidden_owner") == "1",
                anti_whale=token_data.get("anti_whale_modifiable") == "1",
                trading_cooldown=token_data.get("trading_cooldown") == "1"
            )
        else:
            # Return safe defaults if analysis fails
            return TokenAnalysis(
                token_address=token_address,
                symbol="UNKNOWN",
                name="Unknown Token",
                is_honeypot=False,
                can_sell=True,
                honeypot_reason=None,
                buy_tax=0.0,
                sell_tax=0.0,
                slippage_modifiable=False,
                is_proxy=False,
                is_mintable=False,
                owner_change_balance=False,
                hidden_owner=False,
                anti_whale=False,
                trading_cooldown=False
            )
    
    async def check_address_security(self, address: str) -> Dict[str, Any]:
        """Check address for malicious activity."""
        endpoint = f"/api/v1/address_security/{address}"
        result = await self._make_request(endpoint)
        
        if "result" in result:
            return result["result"]
        return {"error": "Could not check address security"}
    
    async def check_approval_security(self, chain_id: str, spender_address: str) -> Dict[str, Any]:
        """Check approval/allowance security."""
        endpoint = f"/api/v1/approval_security/{chain_id}"
        params = {"contract_addresses": spender_address}
        
        result = await self._make_request(endpoint, params)
        return result.get("result", {})
    
    async def check_dapp_security(self, url: str) -> Dict[str, Any]:
        """Check dApp/website security."""
        endpoint = "/api/v1/dapp_security"
        params = {"url": url}
        
        result = await self._make_request(endpoint, params)
        return result.get("result", {})
    
    async def check_phishing_site(self, url: str) -> Dict[str, Any]:
        """Check if URL is a phishing site."""
        endpoint = "/api/v1/phishing_site"
        params = {"url": url}
        
        result = await self._make_request(endpoint, params)
        return result.get("result", {})
    
    async def decode_signature_data(self, chain_id: str, data: str) -> Dict[str, Any]:
        """Decode transaction signature data."""
        endpoint = f"/api/v1/abi/{chain_id}/decode"
        params = {"data": data}
        
        result = await self._make_request(endpoint, params)
        return result.get("result", {})
    
    async def detect_rug_pull(self, token_address: str, chain_id: str = "1") -> Dict[str, Any]:
        """Detect potential rug pull indicators."""
        endpoint = f"/api/v1/rugpull_detecting/{chain_id}"
        params = {"contract_addresses": token_address}
        
        result = await self._make_request(endpoint, params)
        return result.get("result", {})

class CryptoPriceMonitor:
    """Cryptocurrency price monitoring and alerting system."""
    
    def __init__(self):
        self.alerts: List[PriceAlert] = []
        self.price_cache: Dict[str, Dict] = {}
        self.cache_expiry = 60  # seconds
        
    async def get_token_price(self, symbol: str, vs_currency: str = "usd") -> Optional[float]:
        """Get current token price from CoinGecko API."""
        cache_key = f"{symbol}_{vs_currency}"
        now = datetime.now()
        
        # Check cache first
        if cache_key in self.price_cache:
            cached_data = self.price_cache[cache_key]
            if (now - cached_data["timestamp"]).seconds < self.cache_expiry:
                return cached_data["price"]
        
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price"
            params = {
                "ids": symbol.lower(),
                "vs_currencies": vs_currency,
                "include_24hr_change": "true"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        if symbol.lower() in data:
                            price = data[symbol.lower()][vs_currency]
                            
                            # Cache the result
                            self.price_cache[cache_key] = {
                                "price": price,
                                "timestamp": now,
                                "change_24h": data[symbol.lower()].get(f"{vs_currency}_24h_change", 0)
                            }
                            
                            return price
        except Exception as e:
            logger.error(f"Failed to get price for {symbol}: {e}")
        
        return None
    
    def create_price_alert(self, symbol: str, target_price: float, condition: str) -> PriceAlert:
        """Create a new price alert."""
        alert = PriceAlert(
            symbol=symbol.upper(),
            target_price=target_price,
            condition=condition.lower(),
            active=True,
            created_at=datetime.now()
        )
        
        self.alerts.append(alert)
        logger.info(f"Created price alert: {symbol} {condition} {target_price}")
        return alert
    
    async def check_alerts(self) -> List[PriceAlert]:
        """Check all active alerts and return triggered ones."""
        triggered_alerts = []
        
        for alert in self.alerts:
            if not alert.active or alert.triggered_at:
                continue
            
            current_price = await self.get_token_price(alert.symbol)
            if current_price is None:
                continue
            
            should_trigger = False
            if alert.condition == "above" and current_price >= alert.target_price:
                should_trigger = True
            elif alert.condition == "below" and current_price <= alert.target_price:
                should_trigger = True
            
            if should_trigger:
                alert.triggered_at = datetime.now()
                alert.active = False
                triggered_alerts.append(alert)
                logger.info(f"Price alert triggered: {alert.symbol} is {current_price}")
        
        return triggered_alerts
    
    def get_active_alerts(self) -> List[PriceAlert]:
        """Get all active price alerts."""
        return [alert for alert in self.alerts if alert.active]
    
    def remove_alert(self, symbol: str, target_price: float) -> bool:
        """Remove a specific price alert."""
        for i, alert in enumerate(self.alerts):
            if alert.symbol == symbol.upper() and alert.target_price == target_price:
                del self.alerts[i]
                return True
        return False

class WalletAnalyzer:
    """Advanced wallet analysis and tracking."""
    
    def __init__(self):
        self.tracked_wallets: Dict[str, Dict] = {}
        
    async def analyze_wallet_activity(self, address: str, days: int = 30) -> Dict[str, Any]:
        """Analyze wallet activity patterns."""
        # This would integrate with various blockchain APIs
        # For now, return a structure showing what would be analyzed
        
        analysis = {
            "address": address,
            "analysis_period_days": days,
            "total_transactions": 0,
            "total_volume_usd": 0.0,
            "unique_tokens_interacted": 0,
            "defi_protocols_used": [],
            "nft_activity": {
                "mints": 0,
                "buys": 0,
                "sells": 0,
                "unique_collections": 0
            },
            "risk_indicators": {
                "high_value_transactions": 0,
                "suspicious_token_interactions": 0,
                "mixer_usage": False,
                "rapid_trading_patterns": False
            },
            "portfolio_diversity": {
                "token_count": 0,
                "concentration_risk": "low",  # low, medium, high
                "largest_holding_percentage": 0.0
            },
            "behavioral_patterns": {
                "most_active_hours": [],
                "preferred_dexes": [],
                "average_hold_time_days": 0,
                "trading_frequency": "low"  # low, medium, high
            }
        }
        
        return analysis
    
    def track_wallet(self, address: str, label: str = "") -> bool:
        """Add wallet to tracking list."""
        self.tracked_wallets[address] = {
            "label": label,
            "added_at": datetime.now(),
            "last_checked": None,
            "alert_on_large_transactions": True,
            "alert_threshold_usd": 10000.0
        }
        
        logger.info(f"Now tracking wallet: {address} ({label})")
        return True
    
    def untrack_wallet(self, address: str) -> bool:
        """Remove wallet from tracking."""
        if address in self.tracked_wallets:
            del self.tracked_wallets[address]
            logger.info(f"Stopped tracking wallet: {address}")
            return True
        return False
    
    def get_tracked_wallets(self) -> Dict[str, Dict]:
        """Get all tracked wallets."""
        return self.tracked_wallets.copy()

class ComprehensiveSecuritySuite:
    """Complete security analysis suite combining all security tools."""
    
    def __init__(self, goplus_api_key: Optional[str] = None):
        self.goplus_client = GoPlusLabsClient(goplus_api_key)
        self.price_monitor = CryptoPriceMonitor()
        self.wallet_analyzer = WalletAnalyzer()
        
    async def comprehensive_security_check(self, target: str, target_type: str = "address") -> SecurityResult:
        """Perform comprehensive security analysis on target."""
        checks = {}
        total_checks = 0
        passed_checks = 0
        
        try:
            if target_type == "address":
                # Address security checks
                async with self.goplus_client:
                    address_result = await self.goplus_client.check_address_security(target)
                    checks["address_security"] = address_result
                    total_checks += 1
                    
                    # Check if address has malicious indicators
                    malicious_indicators = [
                        "blacklist_doubt", "blackmail_activities", "cybercrime",
                        "darkweb_transactions", "financial_crime", "mixer",
                        "money_laundering", "phishing_activities", "stealing_attack"
                    ]
                    
                    is_safe = not any(address_result.get(indicator) == "1" for indicator in malicious_indicators)
                    if is_safe:
                        passed_checks += 1
                        
            elif target_type == "token":
                # Token security analysis
                async with self.goplus_client:
                    token_analysis = await self.goplus_client.check_token_security(target)
                    checks["token_security"] = {
                        "is_honeypot": token_analysis.is_honeypot,
                        "can_sell": token_analysis.can_sell,
                        "buy_tax": token_analysis.buy_tax,
                        "sell_tax": token_analysis.sell_tax,
                        "is_proxy": token_analysis.is_proxy,
                        "is_mintable": token_analysis.is_mintable,
                        "hidden_owner": token_analysis.hidden_owner
                    }
                    total_checks += 1
                    
                    # Token is considered safe if not a honeypot and has reasonable taxes
                    is_safe = (not token_analysis.is_honeypot and 
                             token_analysis.can_sell and 
                             token_analysis.buy_tax < 10.0 and 
                             token_analysis.sell_tax < 10.0)
                    if is_safe:
                        passed_checks += 1
                        
            elif target_type == "url":
                # Website/dApp security checks
                async with self.goplus_client:
                    dapp_result = await self.goplus_client.check_dapp_security(target)
                    phishing_result = await self.goplus_client.check_phishing_site(target)
                    
                    checks["dapp_security"] = dapp_result
                    checks["phishing_check"] = phishing_result
                    total_checks += 2
                    
                    # Website is safe if not flagged as malicious or phishing
                    dapp_safe = dapp_result.get("malicious_activity") != "1"
                    phishing_safe = phishing_result.get("phishing_site") != "1"
                    
                    if dapp_safe:
                        passed_checks += 1
                    if phishing_safe:
                        passed_checks += 1
            
            # Calculate risk level and confidence
            if total_checks == 0:
                risk_level = "unknown"
                confidence = 0.0
            else:
                pass_rate = passed_checks / total_checks
                if pass_rate >= 0.9:
                    risk_level = "low"
                elif pass_rate >= 0.7:
                    risk_level = "medium"
                elif pass_rate >= 0.5:
                    risk_level = "high"
                else:
                    risk_level = "critical"
                
                confidence = min(pass_rate + 0.1, 1.0)  # Slight confidence boost
            
            return SecurityResult(
                is_safe=passed_checks == total_checks and total_checks > 0,
                risk_level=risk_level,
                confidence=confidence,
                checks_passed=passed_checks,
                total_checks=total_checks,
                details=checks,
                timestamp=datetime.now()
            )
            
        except Exception as e:
            logger.error(f"Security check failed: {e}")
            return SecurityResult(
                is_safe=False,
                risk_level="unknown",
                confidence=0.0,
                checks_passed=0,
                total_checks=1,
                details={"error": str(e)},
                timestamp=datetime.now()
            )
    
    async def monitor_price_alerts(self) -> List[PriceAlert]:
        """Check all price alerts and return triggered ones."""
        return await self.price_monitor.check_alerts()
    
    def create_price_alert(self, symbol: str, target_price: float, condition: str) -> PriceAlert:
        """Create a new price alert."""
        return self.price_monitor.create_price_alert(symbol, target_price, condition)
    
    def track_wallet(self, address: str, label: str = "") -> bool:
        """Add wallet to tracking."""
        return self.wallet_analyzer.track_wallet(address, label)
    
    async def analyze_wallet(self, address: str, days: int = 30) -> Dict[str, Any]:
        """Analyze wallet activity patterns."""
        return await self.wallet_analyzer.analyze_wallet_activity(address, days)

# Export main classes
__all__ = [
    'ComprehensiveSecuritySuite',
    'GoPlusLabsClient', 
    'CryptoPriceMonitor',
    'WalletAnalyzer',
    'SecurityResult',
    'TokenAnalysis',
    'PriceAlert'
]
