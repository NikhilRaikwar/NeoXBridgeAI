# 🚀 NeoXBridge AI

**Advanced Conversational AI Assistant for Neo Blockchain Operations**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com/)
[![Neo Blockchain](https://img.shields.io/badge/Neo-N3-brightgreen.svg)](https://neo.org/)

> 🌟 **Transform complex blockchain operations into natural conversations with cutting-edge AI technology**

NeoXBridge AI is a sophisticated conversational interface that bridges the gap between human language and Neo blockchain operations. Built with advanced AI capabilities, it enables users to interact with the Neo N3 blockchain through natural language commands, making cryptocurrency operations accessible to everyone.

## ✨ Key Features

### 🧠 **Advanced AI Integration**
- **GPT-4 Powered**: Leverages OpenAI's most advanced language model
- **Natural Language Understanding**: Process complex blockchain requests in plain English
- **Context-Aware Conversations**: Maintains conversation history and user context
- **Intelligent Error Recovery**: Provides helpful suggestions when operations fail

### 🔐 **Enterprise-Grade Security**
- **Multi-Layer Validation**: Comprehensive address and transaction verification
- **GoPlus Labs Integration**: Real-time security analysis and threat detection
- **Transaction Confirmation**: Multi-step verification process for all operations
- **Safe Demo Mode**: Test functionality without real blockchain transactions
- **Private Key Management**: Secure wallet setup with multiple authentication options

### ⚡ **Comprehensive Blockchain Operations**
- **Multi-Asset Support**: Handle NEO, GAS, and all Neo N3 compatible tokens
- **Real-Time Balance Queries**: Instant wallet balance checking across all assets
- **Smart Transaction Management**: Preview, simulate, and execute transactions
- **Address Validation**: Verify Neo N3 address format and legitimacy
- **Transaction Tracking**: Monitor transaction status and confirmation

### 🎨 **Superior User Experience**
- **Intuitive CLI Interface**: Beautiful console interface with rich formatting
- **Interactive Demos**: Comprehensive demonstration scenarios
- **Session Analytics**: Track usage patterns and operation statistics
- **Comprehensive Help System**: Built-in guidance and examples

## 🚦 Quick Start

### Prerequisites

- **Python 3.8+** installed on your system
- **OpenAI API Key** (required for AI functionality)
- **Neo RPC Access** (optional - defaults to public mainnet)
- **GoPlus Labs API Key** (optional but recommended for security)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/NeoXBridgeAI.git
   cd NeoXBridgeAI
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
   # Full interactive application
   python main.py
   
   # Quick demo
   python demo.py
   
   # Complete end-to-end use case demonstration
   python end_to_end_demo.py
   ```

## 🎯 Usage Examples

### Basic Commands

```
💬 You: Help
🤖 NeoXBridge AI: [Shows available commands and features]

💬 You: Check balance for NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N
🤖 NeoXBridge AI: [Returns current NEO, GAS, and token balances]

💬 You: Is this address safe: NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c
🤖 NeoXBridge AI: [Provides security analysis using GoPlus Labs]

💬 You: Send 10 NEO to NhGomKyZgSuYUGqrXHcpv1bNH9ntwvfm4c
🤖 NeoXBridge AI: [Initiates secure transfer with confirmation steps]
```

### Natural Language Queries

```
💬 You: What's my wallet balance?
💬 You: I want to transfer some tokens to my friend
💬 You: Is this smart contract legitimate?
💬 You: Show me my transaction history
💬 You: How much GAS do I have?
```

## 🏗️ Project Structure

```
NeoXBridge-AI/
├── 📁 src/
│   ├── 🧠 agent.py          # Main AI agent logic
│   ├── 🔧 tools.py          # Blockchain operation tools
│   ├── 💬 llm_client.py     # OpenAI integration
│   ├── 📝 prompts.py        # AI system prompts
│   ├── ⚙️ config.py         # Configuration management
│   ├── 🎨 ui.py             # User interface utilities
│   └── 📦 __init__.py       # Package initialization
├── 📄 main.py               # Main application entry point
├── 🎮 demo.py               # Interactive demo script
├── 🎬 end_to_end_demo.py    # Complete use case demonstration
├── 📋 requirements.txt      # Python dependencies
├── ⚙️ .env.example          # Environment template
├── 🛡️ .gitignore            # Git ignore file
└── 📖 README.md             # This file
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

## 🔧 Development

### Running in Development Mode

```bash
# Install development dependencies
pip install -r requirements.txt

# Set development environment
export DEMO_MODE=true
export LOG_LEVEL=DEBUG

# Run with hot reload (if using nodemon equivalent)
python main.py
```

### Project Architecture

The application follows a modular architecture:

1. **Agent Layer** (`agent.py`): Core AI logic and intent processing
2. **Tools Layer** (`tools.py`): Blockchain operation implementations
3. **LLM Layer** (`llm_client.py`): AI model integration and prompt handling
4. **Config Layer** (`config.py`): Environment and application configuration
5. **UI Layer** (`ui.py`): User interface and interaction management

### Adding New Features

1. **New Blockchain Operation**:
   - Add function to `tools.py`
   - Update intent classification in `agent.py`
   - Add corresponding prompts in `prompts.py`

2. **New AI Capabilities**:
   - Extend system prompts in `prompts.py`
   - Update the agent logic in `agent.py`
   - Add any required tools in `tools.py`

## 📊 Roadmap

### Version 1.1 (Next Release)
- [ ] **Enhanced Wallet Integration**: Support for multiple wallet types
- [ ] **Transaction History**: Complete transaction tracking and analysis
- [ ] **DeFi Operations**: Support for Neo N3 DeFi protocols
- [ ] **Web Interface**: Browser-based GUI alongside CLI

### Version 1.2 (Future)
- [ ] **Mobile App**: iOS and Android applications
- [ ] **Advanced Analytics**: Portfolio tracking and insights
- [ ] **DeFi Integration**: Swap, stake, and yield farming
- [ ] **NFT Support**: Neo N3 NFT operations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is provided "as is", without warranty of any kind. Always verify transactions and use appropriate security measures when handling cryptocurrency. The authors are not responsible for any financial losses incurred through the use of this software.

---

<div align="center">

**🌟 Star this repository if you found it helpful!**

Made with ❤️ for the Neo Community

</div>
