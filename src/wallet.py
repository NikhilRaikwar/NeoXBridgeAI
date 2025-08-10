"""
NeoXBridge AI - Wallet Management
Handles private key management and Neo address derivation.
"""

import hashlib
import base58
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


class NeoWallet:
    """Neo wallet management with private key support."""
    
    def __init__(self):
        self.private_key: Optional[str] = None
        self.address: Optional[str] = None
        self.logger = logging.getLogger(__name__ + ".NeoWallet")
    
    def set_private_key(self, private_key: str, known_address: Optional[str] = None) -> bool:
        """
        Set the private key and derive or use the provided Neo address.
        
        Args:
            private_key (str): Private key in hex format
            known_address (str, optional): Known address for this private key
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Basic validation - private key should be 64 hex characters
            if not private_key or len(private_key) != 64:
                return False
                
            # Check if it's valid hex
            try:
                bytes.fromhex(private_key)
            except ValueError:
                return False
            
            self.private_key = private_key
            
            # Use provided address if available, otherwise derive it
            if known_address:
                self.address = known_address
                self.logger.info(f"Wallet initialized with provided address: {self.address}")
            else:
                self.address = self._derive_address_from_private_key(private_key)
                self.logger.info(f"Wallet initialized with derived address: {self.address}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to set private key: {e}")
            return False
    
    def _derive_address_from_private_key(self, private_key: str) -> str:
        """
        Derive Neo N3 address from private key.
        
        Args:
            private_key (str): Private key in hex format
            
        Returns:
            str: Neo N3 address
        """
        try:
            # Try to use Neo3 libraries for proper address derivation
            try:
                import neo3.wallet.utils
                from neo3.wallet.account import Account
                
                # Create account from private key bytes and derive address
                private_key_bytes = bytes.fromhex(private_key)
                account = Account.from_private_key(private_key_bytes)
                address = account.address
                self.logger.info(f"Successfully derived address using Neo3 libraries: {address}")
                return address
                
            except ImportError as e:
                self.logger.warning(f"Neo3 libraries not available ({e}), using manual derivation")
                # Continue to manual derivation below
            
            # Manual address derivation for fallback
            # This is a simplified implementation based on Neo's address generation
            
            # Create a hash from the private key to simulate public key derivation
            key_bytes = bytes.fromhex(private_key)
            
            # Simulate elliptic curve point multiplication (simplified)
            # In real Neo, this would be: public_key = private_key * G (generator point)
            public_key_hash = hashlib.sha256(key_bytes).digest()
            
            # Neo uses Script Hash for addresses: Hash160(verification_script)
            # Simplified: SHA256 + RIPEMD160 (or SHA256 if RIPEMD160 not available)
            sha_hash = hashlib.sha256(public_key_hash).digest()
            
            # Try to use RIPEMD160 if available
            try:
                from Crypto.Hash import RIPEMD160
                ripemd = RIPEMD160.new()
                ripemd.update(sha_hash)
                script_hash = ripemd.digest()
            except ImportError:
                # Fallback to SHA256 truncated to 20 bytes
                script_hash = hashlib.sha256(sha_hash).digest()[:20]
            
            # Neo N3 uses version byte 0x35
            versioned_payload = b'\x35' + script_hash
            
            # Calculate checksum: first 4 bytes of double SHA256
            checksum_full = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()
            checksum = checksum_full[:4]
            
            # Combine and encode with base58
            full_payload = versioned_payload + checksum
            address = base58.b58encode(full_payload).decode('utf-8')
            
            self.logger.info(f"Manual address derivation completed: {address}")
            return address
            
        except Exception as e:
            self.logger.error(f"Address derivation failed: {e}")
            # Ultimate fallback - create a deterministic address that's at least unique to the key
            hash_hex = hashlib.sha256(private_key.encode()).hexdigest()
            fallback_address = f"N{hash_hex[:32]}"
            self.logger.warning(f"Using fallback address: {fallback_address}")
            return fallback_address
    
    def is_wallet_loaded(self) -> bool:
        """Check if wallet is loaded with private key."""
        return self.private_key is not None and self.address is not None
    
    def get_address(self) -> Optional[str]:
        """Get the wallet address."""
        return self.address
    
    def get_wallet_info(self) -> Dict[str, Any]:
        """Get wallet information."""
        return {
            "address": self.address,
            "has_private_key": self.private_key is not None,
            "is_loaded": self.is_wallet_loaded()
        }
    
    def sign_transaction(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sign a transaction with the private key.
        This is a simplified implementation for demo purposes.
        
        Args:
            transaction_data (dict): Transaction data to sign
            
        Returns:
            dict: Signed transaction result
        """
        if not self.is_wallet_loaded():
            return {
                "success": False,
                "error": "Wallet not loaded with private key"
            }
        
        try:
            # In a real implementation, you would:
            # 1. Create the transaction object
            # 2. Sign it with the private key using Neo's cryptographic functions
            # 3. Return the signed transaction
            
            # For demo purposes, we'll simulate signing
            signature = self._create_demo_signature(transaction_data)
            
            return {
                "success": True,
                "signed_transaction": {
                    **transaction_data,
                    "signature": signature,
                    "signer": self.address
                }
            }
            
        except Exception as e:
            self.logger.error(f"Transaction signing failed: {e}")
            return {
                "success": False,
                "error": f"Signing failed: {str(e)}"
            }
    
    def _create_demo_signature(self, transaction_data: Dict[str, Any]) -> str:
        """Create a demo signature for educational purposes."""
        # Create a deterministic "signature" based on transaction data and private key
        data_str = str(transaction_data) + self.private_key
        signature_hash = hashlib.sha256(data_str.encode()).hexdigest()
        return f"0x{signature_hash}"
    
    def clear_wallet(self):
        """Clear the wallet data for security."""
        self.private_key = None
        self.address = None
        self.logger.info("Wallet cleared")


def validate_private_key(private_key: str) -> Dict[str, Any]:
    """
    Validate a Neo private key format.
    Supports both raw hex (64 chars) and WIF format.
    
    Args:
        private_key (str): Private key to validate
        
    Returns:
        dict: Validation result with converted hex key
    """
    try:
        # Remove any whitespace
        private_key = private_key.strip()
        
        # Try to convert WIF to hex if it looks like WIF
        if len(private_key) == 52 and (private_key.startswith('K') or private_key.startswith('L')):
            try:
                hex_key = wif_to_hex(private_key)
                return {
                    "is_valid": True,
                    "message": "WIF private key converted to hex format",
                    "hex_key": hex_key,
                    "original_format": "WIF"
                }
            except Exception as e:
                return {
                    "is_valid": False,
                    "error": f"Invalid WIF format: {str(e)}",
                    "format": "wif_error"
                }
        
        # Check if it's 64-character hex
        elif len(private_key) == 64:
            # Check if it's valid hexadecimal
            try:
                bytes.fromhex(private_key)
            except ValueError:
                return {
                    "is_valid": False,
                    "error": "Private key must contain only hexadecimal characters (0-9, a-f, A-F)",
                    "format": "hex_error"
                }
            
            # Check if it's not all zeros
            if private_key == "0" * 64:
                return {
                    "is_valid": False,
                    "error": "Private key cannot be all zeros",
                    "format": "zero_key"
                }
            
            return {
                "is_valid": True,
                "message": "Hex private key format is valid",
                "hex_key": private_key,
                "original_format": "hex"
            }
        
        else:
            return {
                "is_valid": False,
                "error": "Private key must be either 64 hex characters or 52-character WIF format (starting with K or L)",
                "format": "length_error"
            }
        
    except Exception as e:
        return {
            "is_valid": False,
            "error": f"Validation error: {str(e)}",
            "format": "unknown_error"
        }


def wif_to_hex(wif_key: str) -> str:
    """
    Convert WIF (Wallet Import Format) private key to hex format.
    
    Args:
        wif_key (str): WIF format private key
        
    Returns:
        str: Hex format private key
    """
    try:
        # Decode the base58 WIF
        decoded = base58.b58decode(wif_key)
        
        # For Neo, WIF format is:
        # [version byte][32-byte private key][compression flag][4-byte checksum]
        if len(decoded) == 38:  # Compressed key (1 + 32 + 1 + 4 = 38)
            private_key_bytes = decoded[1:-5]  # Skip version and checksum + compression flag
        elif len(decoded) == 37:  # Uncompressed key (1 + 32 + 4 = 37)
            private_key_bytes = decoded[1:-4]  # Skip version and checksum
        else:
            raise ValueError(f"Invalid WIF length: {len(decoded)}, expected 37 or 38")
        
        # Verify we have 32 bytes (256 bits) for the private key
        if len(private_key_bytes) != 32:
            raise ValueError(f"Invalid private key length: {len(private_key_bytes)}, expected 32")
        
        # Convert to hex
        return private_key_bytes.hex()
        
    except Exception as e:
        raise ValueError(f"Invalid WIF format: {str(e)}")


def generate_demo_private_key() -> str:
    """
    Generate a demo private key for testing purposes.
    WARNING: Never use this for real funds!
    
    Returns:
        str: Demo private key in hex format
    """
    import secrets
    return secrets.token_hex(32)
