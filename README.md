# 🚀 NeoXBridge AI

**Conversational AI Assistant for NeoX Blockchain Operations**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com/)
[![Neo Blockchain](https://img.shields.io/badge/Neo-Blockchain-brightgreen.svg)](https://neo.org/)

> Transform complex blockchain operations into simple conversations with the power of AI.

## ✨ Features

### 🔍 **Natural Language Processing**
- **Address Validation**: "Is this address valid: NiEtVMWVYgpXrWkRTMwRaMJtJ41gD3912N?"
- **Balance Queries**: "Check balance for my Neo address"
- **Transaction Status**: "What's the status of transaction [hash]?"

### 🛡️ **Security-First Design**
- **GoPlus Labs Integration**: Real-time malicious address detection
- **Transaction Confirmation**: Multi-step verification for transfers
- **Risk Assessment**: Smart contract and token security analysis
- **Demo Mode**: Safe testing environment without real transactions

### 💰 **Blockchain Operations**
- **Token Transfers**: Send NEO, GAS, and other Neo N3 tokens
- **Real-time Balance Checking**: Get up-to-date wallet balances
- **Transaction Simulation**: Preview transactions before execution
- **Multi-asset Support**: Handle various Neo ecosystem tokens

### 🤖 **Conversational Interface**
- **Natural Commands**: Speak as you would to a human assistant
- **Context Awareness**: Remember conversation history and user preferences
- **Error Handling**: Intelligent error recovery and helpful suggestions
- **Session Statistics**: Track your activity and usage patterns

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

## 🎬 End-to-End Demonstration

We've included a comprehensive **end-to-end use case demonstration** that showcases NeoXBridge AI in a real-world scenario:

**Scenario: "Sarah's DeFi Portfolio Management Journey"**

Run the complete demonstration:
```bash
python end_to_end_demo.py
```

**10-Step User Journey:**
1. 👋 **Initial Greeting** - New user onboarding
2. 🔍 **Address Validation** - Verify Neo N3 addresses
3. 🛡️ **Security Check** - GoPlus Labs integration
4. 💰 **Balance Inquiry** - Portfolio balance checking
5. 📋 **Transaction Planning** - AI-assisted planning
6. 🚀 **Transaction Execution** - Secure token transfer
7. 📊 **Status Monitoring** - Real-time tracking
8. 📈 **Portfolio Summary** - Comprehensive overview
9. ❓ **Feature Discovery** - Capability exploration
10. 👋 **Session Wrap-up** - User satisfaction

**Demo Features:**
- 🎮 **Interactive Mode** - Step through manually
- 🤖 **Automated Mode** - Watch full scenario
- 📊 **Session Analytics** - Comprehensive metrics
- 🛡️ **Safe Mode** - All transactions simulated

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
├── 🎮 demo.py              # Interactive demo script
├── 🎬 end_to_end_demo.py   # Complete use case demonstration
├── 📋 requirements.txt      # Python dependencies
├── ⚙️ .env.example          # Environment template
├── 🛡️ .gitignore           # Git ignore file
├── 📜 LICENSE              # MIT License
└── 📖 README.md            # This file
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
