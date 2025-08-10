# 🌉 NeoXBridge AI - Comprehensive Blockchain Assistant

**Advanced Neo N3 Blockchain Agent with AI-Powered Security Analysis**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Neo N3](https://img.shields.io/badge/Neo-N3-brightgreen.svg)](https://neo.org/)
[![GoPlusLabs](https://img.shields.io/badge/Security-GoPlusLabs-red.svg)](https://gopluslabs.io/)

> The most comprehensive Neo blockchain assistant with advanced security analysis, wallet management, and AI-powered operations.

## ✨ Features

### 🧠 **Advanced AI Agent**
- **Intelligent Intent Recognition**: Natural language understanding for blockchain operations
- **Context-Aware Responses**: Maintains conversation state and user preferences
- **Comprehensive Help System**: Built-in guidance for all features
- **Session Management**: Track your interaction history and patterns

### 🔐 **Wallet Management**
- **Private Key Import**: Support for WIF and HEX formats
- **Address Validation**: Neo N3 address format verification
- **Balance Checking**: Real-time NEO/GAS balance queries
- **Transaction History**: Complete wallet activity tracking

### 🛡️ **Multi-Layer Security**
- **GoPlusLabs Integration**: Advanced malicious address detection
- **Token Security Analysis**: Comprehensive smart contract analysis
- **Phishing Protection**: Website and dApp security verification
- **Transaction Preview**: Review all operations before execution

### 💰 **Blockchain Operations**
- **Neo N3 API Integration**: Complete blockchain data access
- **Asset Management**: NEP-17 tokens and NEP-11 NFTs support
- **Transaction Sending**: Secure NEO/GAS transfers with confirmation
- **Real-time Data**: Current block height, transaction counts, and more

### 📈 **Price Monitoring**
- **Price Alerts**: Create custom alerts for NEO, GAS, and other assets
- **Alert Management**: View and manage active price alerts
- **Multi-Asset Support**: Monitor various cryptocurrency prices

### 🎨 **NFT Operations**
- **NFT Collection Viewing**: Display owned NEP-11 tokens
- **Contract Analysis**: Group NFTs by collection/contract
- **Comprehensive Stats**: Total counts and collection breakdowns

### 🏛️ **Governance Features**
- **Committee Information**: Neo governance committee details
- **Candidate Tracking**: Monitor governance candidates
- **Voting Information**: Access to Neo's governance system

## 🚦 Quick Start

### Prerequisites

- **Python 3.8+** installed on your system
- **OpenAI API Key** (required for AI functionality)
- **Neo RPC Access** (optional - defaults to public mainnet)
- **GoPlus Labs API Key** (optional but recommended for security)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/NikhilRaikwar/NeoXBridge-AI.git
   cd NeoXBridge-AI
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   ```bash
   # Copy the environment template
   cp .env.example .env
   
   # Edit .env file with your API keys
   nano .env
   ```

4. **Configure Environment Variables**
   ```env
   # Required
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Optional but recommended
   GO_PLUS_LABS_APP_KEY=your_goplus_api_key_here
   NEO_RPC_URL=https://mainnet1.neo.coz.io:443
   
   # Optional settings
   OPENAI_MODEL=gpt-4o-mini
   DEMO_MODE=true
   ENABLE_SECURITY_CHECKS=true
   ```

5. **Run the Application**
   ```bash
   # Run the comprehensive NeoXBridge AI agent
   python neoxbridge_comprehensive_agent.py
   ```

## 🎯 Usage Examples

### Wallet Management

```
💬 You: load wallet <private_key>
🤖 NeoXBridge AI: ✅ Wallet Loaded Successfully!
                📍 Address: NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N
                💼 Network: testnet
                🔐 Status: Ready for operations

💬 You: check my balance
🤖 NeoXBridge AI: 💰 Balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N
                🔸 NEO: 150.0
                🔸 GAS: 85.42
```

### Security Analysis

```
💬 You: security check NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c
🤖 NeoXBridge AI: 🛡️ Security Analysis - SAFE
                ✅ Target: NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c
                🔸 Type: address
                🔸 Risk Level: low
                🔸 Confidence: 95.0%
```

### Transaction Operations

```
💬 You: send 5 NEO to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c
🤖 NeoXBridge AI: 💸 Transaction Preview
                📤 From: NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N
                📥 To: NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c
                💰 Amount: 5 NEO
                🛡️ Security Status: ✅ SAFE
```

### Price Monitoring

```
💬 You: create price alert NEO above 50
🤖 NeoXBridge AI: 🚨 Price Alert Created
                🔸 Symbol: NEO
                🔸 Condition: above $50
                🔸 Status: Active
```

### Natural Language Queries

```
💬 You: What's the current block height?
💬 You: Show me my NFT collection
💬 You: How many committee members are there?
💬 You: Is this token contract safe?
💬 You: Check recent blocks
```

## 📚 Command Reference

Here are the key commands available in NeoXBridge AI:

### 💼 Wallet Operations
- `load wallet PRIVATE_KEY` - Import your wallet
- `wallet status` - Check wallet status
- `check my balance` - View NEO/GAS balances

### 🛡️ Security Commands
- `security check ADDRESS` - Analyze address safety
- `analyze token CONTRACT` - Token security analysis
- `security check URL` - Website safety check

### 💸 Transaction Commands
- `send AMOUNT ASSET to ADDRESS` - Transfer tokens
- `transfer 5 NEO to ADDRESS` - Send NEO
- `pay 10.5 GAS to ADDRESS` - Send GAS

### 📊 Blockchain Data
- `block height` - Current blockchain height
- `recent blocks` - Recent block information
- `asset count` - Total assets on network

### 📈 Price Monitoring
- `create price alert SYMBOL above/below PRICE` - Create alerts
- `check my alerts` - View active alerts

### 🎨 NFT Operations
- `my nfts` - View your NFT collection
- `nfts for ADDRESS` - Check NFTs for address

### 🏛️ Governance
- `committee info` - Neo committee details
- `candidate count` - Total candidates

## 🏗️ Project Structure

```
NeoXBridge-AI/
├── 🤖 neoxbridge_comprehensive_agent.py  # Main comprehensive AI agent
├── 🔧 neo_blockchain_tools.py           # Neo N3 blockchain operations
├── 🛡️ security_and_analysis_tools.py   # Security and analysis suite
├── ⚙️ config.yaml                       # Configuration file
├── 📋 requirements.txt                  # Python dependencies
├── 📋 requirements_comprehensive.txt    # Full dependencies list
├── 🗂️ spoon-core-main/                 # Spoon AI framework (optional)
├── 🗂️ spoon-toolkit-main/              # Spoon toolkits (optional)
├── ⚙️ .env.example                      # Environment template
├── 🛡️ .gitignore                       # Git ignore file
├── 📜 LICENSE                           # MIT License
└── 📖 README.md                         # This file
```

## ⚙️ Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | ✅ Yes | - | OpenAI API key for GPT-4 |
| `GO_PLUS_LABS_APP_KEY` | 🟡 Recommended | - | Security analysis API key |
| `NEO_RPC_URL` | ❌ No | Public mainnet | Neo blockchain RPC endpoint |
| `OPENAI_MODEL` | ❌ No | `gpt-4o-mini` | OpenAI model to use |
| `DEMO_MODE` | ❌ No | `true` | Enable safe demo mode |
| `ENABLE_SECURITY_CHECKS` | ❌ No | `true` | Enable GoPlus security |
| `LOG_LEVEL` | ❌ No | `INFO` | Logging verbosity |

### Getting API Keys

#### 1. OpenAI API Key (Required)
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account or log in
3. Generate a new API key
4. Add it to your `.env` file

#### 2. GoPlus Labs API Key (Recommended)
1. Visit [GoPlus Labs](https://gopluslabs.io/)
2. Sign up for a free developer account
3. Get your API key from the dashboard
4. Add it to your `.env` file

## 🛡️ Security Features

### Multi-Layer Protection
- **Address Validation**: Verify Neo N3 address format and checksums
- **Security Scanning**: Integration with GoPlus Labs for malicious address detection
- **Transaction Confirmation**: Multi-step verification before executing transfers
- **Rate Limiting**: Prevent abuse and ensure responsible usage
- **Demo Mode**: Safe testing environment without real blockchain interactions

### Best Practices
- Always verify recipient addresses before large transfers
- Use the security check feature for unknown addresses
- Keep your private keys secure and never share them
- Start with small amounts when testing new features
- Enable two-factor authentication on all related accounts

## 🎨 Features in Detail

### Conversational AI
- **GPT-4 Integration**: Advanced natural language understanding
- **Context Awareness**: Maintains conversation state and user preferences
- **Error Recovery**: Intelligent handling of invalid requests with helpful suggestions
- **Multi-turn Conversations**: Complex operations through natural dialog

### Blockchain Integration
- **Neo N3 Compatible**: Full support for Neo's latest blockchain version
- **Multi-Asset Support**: Handle NEO, GAS, and various N3 tokens
- **Real-time Data**: Up-to-date blockchain information and transaction status
- **Transaction Simulation**: Preview operations before execution

### User Experience
- **Beautiful CLI Interface**: Rich console output with emojis and formatting
- **Session Management**: Track usage statistics and conversation history
- **Help System**: Comprehensive guidance and example commands
- **Error Handling**: Clear error messages with actionable solutions

## 🔧 Development

### Running in Development Mode

```bash
# Install development dependencies
pip install -r requirements.txt

# Set development environment
set DEMO_MODE=true
set LOG_LEVEL=DEBUG

# Run the comprehensive agent
python neoxbridge_comprehensive_agent.py
```

### Project Architecture

The application follows a comprehensive modular architecture:

1. **Main Agent** (`neoxbridge_comprehensive_agent.py`): Complete AI agent with all features
2. **Blockchain Tools** (`neo_blockchain_tools.py`): Neo N3 API integration and wallet management
3. **Security Suite** (`security_and_analysis_tools.py`): GoPlusLabs integration and security analysis
4. **Configuration** (`config.yaml`): Application settings and configuration
5. **Environment** (`.env`): Sensitive API keys and environment variables

### Adding New Features

1. **New Blockchain Operation**:
   - Add function to `neo_blockchain_tools.py`
   - Update intent classification in `neoxbridge_comprehensive_agent.py`
   - Add corresponding handler method

2. **New Security Feature**:
   - Extend `security_and_analysis_tools.py`
   - Update security suite in main agent
   - Add new security check methods

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Found an issue? Let us know!
- 💡 **Feature Requests**: Have an idea? Share it!
- 🔧 **Code Contributions**: Submit pull requests
- 📖 **Documentation**: Improve guides and examples
- 🧪 **Testing**: Help test new features and edge cases

### Development Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 Python style guidelines
- Add type hints for better code clarity
- Include docstrings for all functions and classes
- Write comprehensive tests for new features

## 📊 Roadmap

### Version 1.1 (Coming Soon)
- [ ] **Web Interface**: Browser-based GUI
- [ ] **Transaction History**: Complete transaction tracking
- [ ] **Multi-Wallet Support**: Manage multiple addresses
- [ ] **Custom Token Support**: Add any Neo N3 token

### Version 1.2 (Future)
- [ ] **Mobile App**: iOS and Android applications
- [ ] **Advanced Analytics**: Portfolio tracking and insights
- [ ] **DeFi Integration**: Swap, stake, and yield farming
- [ ] **NFT Support**: Neo N3 NFT operations

### Version 2.0 (Vision)
- [ ] **Multi-Chain Support**: Ethereum, Binance Smart Chain
- [ ] **AI Trading Assistant**: Automated trading strategies
- [ ] **Social Features**: Share insights and collaborate
- [ ] **Enterprise Features**: Team management and compliance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Nikhil Raikwar**
- GitHub: [@NikhilRaikwar](https://github.com/NikhilRaikwar)
- Twitter: [@NikhilRaikwar](https://twitter.com/NikhilRaikwarr)
- LinkedIn: [Nikhil Raikwar](https://linkedin.com/in/nikhilraikwar16)

## 🙏 Acknowledgments

- **Neo Foundation** for the amazing blockchain platform
- **OpenAI** for providing GPT-4 capabilities
- **GoPlus Labs** for security infrastructure
- **Neo Community** for inspiration and support
- **Open Source Community** for tools and libraries

## ⚠️ Disclaimer

This software is provided "as is", without warranty of any kind. Always verify transactions and use appropriate security measures when handling cryptocurrency. The authors are not responsible for any financial losses incurred through the use of this software.

---

<div align="center">

**🌟 Star this repository if you found it helpful!**

[Report Bug](https://github.com/NikhilRaikwar/NeoXBridgeAI/issues) · [Request Feature](https://github.com/NikhilRaikwar/NeoXBridgeAI/issues) 

Made with ❤️ for the Neo Community

</div>
