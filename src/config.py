"""
NeoXBridge AI - Configuration
Configuration management for the NeoXBridge AI application.
"""

import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration class for NeoXBridge AI."""
    
    # Application settings
    APP_NAME: str = "NeoXBridge AI"
    APP_VERSION: str = "1.0.0"
    APP_AUTHOR: str = "Nikhil Raikwar"
    APP_GITHUB: str = "@NikhilRaikwar"
    
    # OpenAI configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", "2000"))
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    
    # Neo blockchain configuration
    NEO_RPC_URL: str = os.getenv("NEO_RPC_URL", "https://mainnet1.neo.coz.io:443")
    NEO_NETWORK: str = os.getenv("NEO_NETWORK", "mainnet")
    NEO_TIMEOUT: int = int(os.getenv("NEO_TIMEOUT", "30"))
    
    # GoPlus Labs configuration
    GO_PLUS_LABS_APP_KEY: Optional[str] = os.getenv("GO_PLUS_LABS_APP_KEY")
    GO_PLUS_LABS_BASE_URL: str = os.getenv(
        "GO_PLUS_LABS_BASE_URL", 
        "https://api.gopluslabs.io"
    )
    GO_PLUS_LABS_TIMEOUT: int = int(os.getenv("GO_PLUS_LABS_TIMEOUT", "10"))
    
    # Logging configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_FILE: Optional[str] = os.getenv("LOG_FILE")
    
    # Security settings
    ENABLE_SECURITY_CHECKS: bool = os.getenv("ENABLE_SECURITY_CHECKS", "true").lower() == "true"
    REQUIRE_CONFIRMATION: bool = os.getenv("REQUIRE_CONFIRMATION", "true").lower() == "true"
    MAX_TRANSFER_AMOUNT: float = float(os.getenv("MAX_TRANSFER_AMOUNT", "1000"))
    
    # Rate limiting
    MAX_REQUESTS_PER_MINUTE: int = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "60"))
    COOLDOWN_SECONDS: int = int(os.getenv("COOLDOWN_SECONDS", "1"))
    
    # Demo mode settings
    DEMO_MODE: bool = os.getenv("DEMO_MODE", "true").lower() == "true"
    MOCK_TRANSACTIONS: bool = os.getenv("MOCK_TRANSACTIONS", "true").lower() == "true"
    
    # UI settings
    ENABLE_BANNER: bool = os.getenv("ENABLE_BANNER", "true").lower() == "true"
    ENABLE_COLORS: bool = os.getenv("ENABLE_COLORS", "true").lower() == "true"
    CONSOLE_WIDTH: int = int(os.getenv("CONSOLE_WIDTH", "80"))
    
    @classmethod
    def get_neo_config(cls) -> Dict[str, Any]:
        """Get Neo blockchain configuration."""
        return {
            "rpc_url": cls.NEO_RPC_URL,
            "network": cls.NEO_NETWORK,
            "timeout": cls.NEO_TIMEOUT
        }
    
    @classmethod
    def get_openai_config(cls) -> Dict[str, Any]:
        """Get OpenAI configuration."""
        return {
            "api_key": cls.OPENAI_API_KEY,
            "model": cls.OPENAI_MODEL,
            "max_tokens": cls.OPENAI_MAX_TOKENS,
            "temperature": cls.OPENAI_TEMPERATURE
        }
    
    @classmethod
    def get_goplus_config(cls) -> Dict[str, Any]:
        """Get GoPlus Labs configuration."""
        return {
            "app_key": cls.GO_PLUS_LABS_APP_KEY,
            "base_url": cls.GO_PLUS_LABS_BASE_URL,
            "timeout": cls.GO_PLUS_LABS_TIMEOUT
        }
    
    @classmethod
    def validate_required_config(cls) -> list[str]:
        """Validate required configuration and return missing items."""
        missing = []
        
        if not cls.OPENAI_API_KEY:
            missing.append("OPENAI_API_KEY")
        
        # GoPlus Labs API key is optional but recommended
        if not cls.GO_PLUS_LABS_APP_KEY:
            missing.append("GO_PLUS_LABS_APP_KEY (optional but recommended)")
        
        return missing
    
    @classmethod
    def is_configured(cls) -> bool:
        """Check if the application is properly configured."""
        required_missing = [item for item in cls.validate_required_config() 
                          if not item.endswith("(optional but recommended)")]
        return len(required_missing) == 0
    
    @classmethod
    def get_status(cls) -> Dict[str, Any]:
        """Get configuration status."""
        return {
            "app_name": cls.APP_NAME,
            "app_version": cls.APP_VERSION,
            "openai_configured": bool(cls.OPENAI_API_KEY),
            "neo_configured": True,  # Neo RPC has default
            "goplus_configured": bool(cls.GO_PLUS_LABS_APP_KEY),
            "security_enabled": cls.ENABLE_SECURITY_CHECKS,
            "demo_mode": cls.DEMO_MODE,
            "missing_config": cls.validate_required_config()
        }
    
    @classmethod
    def print_status(cls):
        """Print configuration status."""
        status = cls.get_status()
        
        print(f"\n📊 Configuration Status:")
        print(f"   Application: {status['app_name']} v{status['app_version']}")
        print(f"   OpenAI API: {'✅ Configured' if status['openai_configured'] else '❌ Missing'}")
        print(f"   Neo RPC: {'✅ Configured' if status['neo_configured'] else '❌ Missing'}")
        print(f"   GoPlus Labs: {'✅ Configured' if status['goplus_configured'] else '⚠️ Optional'}")
        print(f"   Security Checks: {'✅ Enabled' if status['security_enabled'] else '❌ Disabled'}")
        print(f"   Demo Mode: {'✅ Enabled' if status['demo_mode'] else '❌ Disabled'}")
        
        if status['missing_config']:
            print(f"\n⚠️ Missing Configuration:")
            for item in status['missing_config']:
                print(f"   • {item}")
        
        print()


# Create global config instance
config = Config()


# Utility functions
def get_env_bool(key: str, default: bool = False) -> bool:
    """Get boolean value from environment variable."""
    value = os.getenv(key, str(default)).lower()
    return value in ("true", "1", "yes", "on")


def get_env_int(key: str, default: int = 0) -> int:
    """Get integer value from environment variable."""
    try:
        return int(os.getenv(key, str(default)))
    except ValueError:
        return default


def get_env_float(key: str, default: float = 0.0) -> float:
    """Get float value from environment variable."""
    try:
        return float(os.getenv(key, str(default)))
    except ValueError:
        return default
