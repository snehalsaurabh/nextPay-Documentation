import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_agraph import agraph, Node, Edge, Config
import streamlit_lottie
import json

def load_lottie_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def anon_aadhaar():
    st.title("🔐 Anon Aadhaar - Anonymous Identity Verification")
    st.image("Assets/anon-aadhar/intro.png", caption = "Anon Aadhar", use_column_width=True)

    st.subheader("🚀 What is Anon Aadhaar?")
    st.write("""
        **Anon Aadhaar** is a groundbreaking zero-knowledge protocol developed by the Privacy and Scaling Explorations team at the Ethereum Foundation. 
        This innovative technology empowers Indian citizens with Aadhaar cards to verify their identity in a completely privacy-preserving manner. 
        No sensitive information is exposed during the verification process, making Anon Aadhaar a powerful tool in the fight for privacy in the digital age.
    """)
    st.image("Assets/anon-aadhar/works1.png", caption = "Working Procedure", use_column_width=True)
    st.subheader("🔍 How Anon Aadhaar Works")
    st.write("""
        Anon Aadhaar leverages advanced cryptographic techniques, particularly zk-SNARKs (Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge), to ensure that users can prove their identity without revealing any underlying personal data.
        
        - **Aadhaar Secure QR Code:** The foundation of this process lies in the Aadhaar Secure QR code, which encapsulates essential identity data. This QR code is signed by the Unique Identification Authority of India (UIDAI) and contains a SHA-256 hash and an RSA signature.
        - **Zero-Knowledge Proof Generation:** The core of Anon Aadhaar's privacy-preserving magic happens here. The protocol uses zk-SNARKs to create a proof that validates the correctness of the hash and RSA signature without ever exposing the actual data. This ensures that the identity verification is both secure and private.
        - **Circuit Implementation:** The underlying cryptographic circuit is designed to process and verify the Aadhaar data. It ensures that the user's identity can be authenticated without directly revealing personal details like name, address, or contact information.
    """)

    st.image("Assets/anon-aadhar/works2.png", caption = "Mechanism", use_column_width=True)
    st.subheader("🌟 Key Features of Anon Aadhaar")
    st.write("""
        Anon Aadhaar offers a robust set of features designed to protect user privacy while ensuring secure and verifiable identity authentication:
        
        - **User Nullifier:** A unique identifier that prevents proof double-spending and enables revocation of user access, ensuring enhanced privacy and control.
        - **Timestamp:** The UNIX UTC timestamp acts as a TOTP (Time-based One-Time Password) system, verifying the proof's recency, adding an extra layer of security.
        - **Public Key Hash:** Ensures that the signer's public key matches the official public key registered with UIDAI, providing an additional verification step.
        - **Signal Hash:** Allows users to transmit a unique signal alongside their Aadhaar identity, which can be utilized for various purposes, such as preventing front-running in blockchain transactions.
    """)

    st.image("Assets/anon-aadhar/install.png", caption = "Integration", use_column_width=True)
    st.subheader("🛠️ Integrating Anon Aadhaar")
    st.write("""
        nextPay offers a comprehensive set of tools for developers to integrate Anon Aadhaar into their applications. Our SDKs and libraries make it straightforward to implement anonymous identity verification:
        
        - **TypeScript SDK**: Easily integrate Anon Aadhaar into your JavaScript applications.
        - **Solidity Library**: Leverage the power of Anon Aadhaar in your smart contracts on the Ethereum blockchain.
        - **React Library**: Implement seamless identity verification in your React-based front-end applications.

        Developers can utilize these tools to provide their users with a privacy-first identity verification process that is secure, reliable, and decentralized.
    """)

    st.image("Assets/anon-aadhar/onchain.png", caption = "Offchain", use_column_width=True)
    st.image("Assets/anon-aadhar/offchain.png", caption = "Onchain", use_column_width=True)
    st.subheader("🔗 Verifying Proofs")
    st.write("""
        Anon Aadhaar proofs can be verified both off-chain and on-chain, depending on your application's needs:
        
        - **Off-Chain Verification**: Use the `verify()` method from the SDK to validate proofs off-chain, ensuring quick and efficient verification without the need for blockchain interaction.
        - **On-Chain Verification**: For decentralized applications, you can import the `AnonAadhaar.sol` verifier contract into your Hardhat project. This enables secure on-chain verification, with features like user nullifiers to prevent misuse and signal hashes to protect against front-running.
    """)

    st.subheader("💡 Potential Use Cases")
    st.write("""
        Anon Aadhaar's versatile protocol can be utilized in a wide range of decentralized applications (dApps), including but not limited to:
        
        - **Aadhaar-Based Quadratic Funding/Voting**: Enable fair and anonymous voting processes in decentralized platforms.
        - **Gitcoin Passport Integration**: Strengthen identity verification in decentralized funding platforms like Gitcoin.
        - **Decentralized Check-In Systems**: Use Anon Aadhaar for secure and private check-ins at events or locations.
        - **Micro-Loan Approval Platforms**: Provide anonymous yet verifiable identity for loan approvals in DeFi.
        - **On-Chain Voting and Polling**: Secure, private, and verifiable voting systems on blockchain platforms.
        - **Decentralized Identity Management**: Empower users to control and manage their identities across multiple dApps without compromising privacy.
    """)

    st.subheader("👨‍💻 For Developers: Deep Dive into Anon Aadhaar's Technical Architecture")
    st.write("""
        **How Anon Aadhaar Works Behind the Scenes**:
        
        Anon Aadhaar’s technical architecture is built around the principles of zero-knowledge proofs, ensuring that identity verification is both secure and private. Here's a closer look at how it functions:

        - **Circuit Design and Implementation**: The heart of Anon Aadhaar is its cryptographic circuit, implemented using Circom Groth16. This circuit processes the user's Aadhaar data, generating a zero-knowledge proof that can be verified without exposing sensitive information. The succinctness and correctness of this circuit are crucial for efficient on-chain verification.
        
        - **zk-SNARKs Integration**: The protocol leverages zk-SNARKs to generate proofs that are both small in size and quick to verify, making them ideal for on-chain use. This integration ensures that the verification process is secure, scalable, and does not burden the blockchain with excessive data.
        
        - **Proof Verification**: Developers can choose between off-chain and on-chain verification methods. Off-chain verification is ideal for applications where speed is critical, while on-chain verification is essential for decentralized applications that require transparent and trustless verification.

        - **Security Considerations**: The use of a public key hash and a signal hash ensures that each transaction or interaction is unique and verifiable. These features protect against common blockchain vulnerabilities such as front-running, while the user nullifier prevents double-spending of proofs.

        **Customization and Integration**:
        - **Flexible SDKs**: The Anon Aadhaar SDKs are designed to be modular, allowing developers to pick and choose the components that best fit their application’s needs.
        - **Advanced Use Cases**: Anon Aadhaar can be adapted for a variety of advanced use cases, from integrating with ERC-4337 wallets to creating entirely new decentralized identity management systems.

        By integrating Anon Aadhaar into your dApps, you’re not just adopting a new technology—you’re embracing a future where privacy and security are foundational to digital interactions.
    """)


def cross_blockchain_payments():
    st.title("🚀 Cross-Blockchain Payment Gateway")
    st.image("Assets/cross-blockchain/Screenshot 2024-08-09 072952.png", caption="🔗 Seamless Ethereum Transfers Across Blockchains")

    st.subheader("🌐 Revolutionizing Cross-Chain Transactions")
    st.write("""
        **Welcome to the Future of Decentralized Finance with nextPay!**  
        Imagine effortlessly transferring Ethereum across different blockchains, all within a single, secure platform. nextPay takes the complexity out of cross-chain payments, providing you with a seamless and intuitive experience.  
        💸 **Say goodbye to the traditional challenges** of cross-blockchain transactions—no more juggling between wallets or worrying about high fees. With nextPay, your financial transactions are simple, secure, and fast.
    """)

    st.subheader("🔒 Supported Blockchains")
    st.write("""
        nextPay is fully compatible with a range of EVM-based blockchains, ensuring that your Ethereum can move freely across the following ecosystems:
        - **Ethereum** 🌍
        - **Binance Smart Chain** 🛡️
        - **Polygon** 🛠️
        - **Avalanche** ❄️  
        
        And this is just the beginning! Our team is constantly working to integrate more blockchains, giving you even greater flexibility and choice.
    """)

    st.subheader("✨ Key Benefits of nextPay")
    st.write("""
        nextPay isn’t just another payment gateway; it's a transformative tool designed to make your financial life easier and more efficient:
        - **🧩 Simplified Cross-Chain Transactions:** We handle all the complexities, so you don’t have to. Moving Ethereum between different blockchain ecosystems has never been easier.
        - **💰 Cost-Effective Transfers:** nextPay optimizes transaction fees, ensuring that your funds go further. Why pay more when you don’t have to?
        - **🔊 Real-Time Audio Notifications:** Our Soundbox feature delivers instant audio confirmations for every transaction, so you’re always in the loop. Stay informed, stay in control.
    """)
    
    st.image("Assets/cross-blockchain/Screenshot 2024-08-09 073022.png", caption="🔗 Seamless Ethereum Transfers Across Blockchains")
    st.subheader("🤝 Integration with DeFi Apps")
    st.write("""
        nextPay is designed to fit seamlessly into the broader DeFi ecosystem. Whether you’re a developer or an end-user, our platform’s cross-chain capabilities can enhance your interaction with decentralized finance applications.
        - **🌍 Interoperability:** nextPay plays well with others, allowing you to leverage our powerful payment gateway within your preferred DeFi apps.
        - **🔧 Customizable Solutions:** Tailor nextPay to your needs, whether you're a DeFi developer looking to integrate our services or an investor managing a diversified portfolio.
    """)

    st.subheader("👨‍💻 For Developers: How Cross-Blockchain Transactions Work")
    st.write("""
        Developers, let's dive into how nextPay facilitates cross-blockchain transactions within the EVM-based ecosystem. At the core of our cross-chain capability is a Solidity smart contract designed to handle token transfers securely and efficiently.

        Here's a quick overview of the smart contract:
        
        ```solidity
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.8;

        contract TransferTokens {
            event Transfer(
                address indexed _from,
                address indexed _to,
                uint256 _amount,
                string _name,
                string _blockchain
            );

            function transferEther(
                address payable _to,
                string memory _name,
                string memory _blockchain
            ) external payable {
                require(_to != address(0), "Invalid recipient address");
                payable(_to).transfer(msg.value);
                emit Transfer(msg.sender, _to, msg.value, _name, _blockchain);
            }

            function check() public pure returns (string memory) {
                return "Shashwat Singh";
            }
        }
        ```

        **How It Works:**
        - **Transfer Functionality:** The `transferEther` function is designed to facilitate the transfer of Ether from one address to another on the same blockchain. The function requires the recipient's address, a name string, and the blockchain identifier.
        - **Event Emission:** Each transfer triggers the `Transfer` event, which logs critical transaction details, including sender and recipient addresses, the amount transferred, and the blockchain involved.
        - **Cross-Blockchain Coordination:** While this contract operates on individual blockchains, nextPay coordinates transactions across different EVM-compatible blockchains by deploying similar contracts on each supported chain. The platform then links these transactions, enabling a seamless cross-chain transfer experience for users.
        - **Security Considerations:** By using a decentralized approach and requiring valid recipient addresses, the contract ensures that funds are securely transferred without vulnerabilities that could be exploited.
        
        **Customizability:** 
        - The contract's simplicity allows for easy customization to include additional features, such as transaction limits, multi-signature approvals, or integration with other smart contracts to expand functionality across the DeFi ecosystem.
        
        nextPay abstracts these technical details, providing users with a simple interface for cross-chain transfers while ensuring that the underlying process remains secure and efficient.
    """)

def soundbox():
    st.title("🔊 Soundbox - Real-Time Blockchain Transaction Notifications")
    st.image("Assets/soundbox/Screenshot 2024-08-09 073134.png", caption="🎵 Waiting For Transaction")

    st.subheader("🎶 What is Soundbox?")
    st.write("""
        **Soundbox** is an innovative feature of nextPay that delivers real-time audio notifications for every blockchain transaction.  
        Inspired by Paytm's instant payment confirmation system, Soundbox enhances your experience by providing immediate, audible feedback on your financial activities across multiple blockchains. 🌐
    """)

    st.subheader("🎛️ Customizable Alerts")
    st.write("""
        With Soundbox, you have full control over which blockchains you monitor.  
        Customize your notification preferences to receive alerts only for the transactions that matter most to you. 🎯
    """)

    st.subheader("🔥 Key Benefits")
    st.write("""
        - **Instant Feedback:** Receive immediate auditory confirmations for each transaction, boosting your confidence and control over your digital finances. 🛡️
        - **Personalized Monitoring:** Select specific blockchains to monitor, ensuring that you stay updated on the most relevant transactions. 🕵️
        - **Seamless Integration:** Soundbox is fully integrated into nextPay, providing a smooth and intuitive user experience for managing cross-chain transactions. 🚀
    """)
    
    st.image("Assets/soundbox/Screenshot 2024-08-09 073810.png", caption="🎵 Trasaction Complete")
    st.subheader("📈 Potential Use Cases")
    st.write("""
        **Soundbox** is ideal for various scenarios, including:
        - **DeFi Traders:** Get instant audio confirmations for trades and swaps, enhancing decision-making and risk management. 💱
        - **Cross-Chain Users:** Monitor Ethereum transfers across different blockchain networks, ensuring seamless financial management. 🔗
        - **Passive Income Earners:** Stay informed about staking rewards, lending interest, and other DeFi activities with custom alerts. 💸
    """)

    st.subheader("👨‍💻 For Developers: The Technical Breakdown")
    st.write("""
        Let's dive into the technical aspects of Soundbox and how it operates behind the scenes to provide real-time transaction notifications. This feature is built using React and TypeScript, leveraging hooks and state management for optimal performance.

        **Core Components:**
        - **React Hooks:** We utilize `useEffect` and `useState` hooks to manage the component's lifecycle and state. The `useEffect` hook sets up event listeners for blockchain transactions, while `useState` tracks the type of blockchain and the transaction data.
        - **Blockchain Event Handling:** Each blockchain has a dedicated hook (e.g., `toTransferETH`, `toTransferBSC`) that establishes a connection to the corresponding smart contract. These hooks listen for `Transfer` events and update the state when a transaction is detected.
        - **Speech Synthesis API:** For delivering audio notifications, we use the Web Speech API’s `speechSynthesis` feature. When a transaction is detected, the `speak` function converts the event data into spoken words, ensuring the user receives immediate audio feedback.

        **Sample Code Explanation:**
        ```typescript
        const setupListener = async () => {
            const handleTransferEvent = (
                _from: string,
                _to: string,
                _amount: string,
                _name: string,
                _blockchain: string
            ) => {
                const message = `${_from} sent ${formatEther(_amount)} to ${_to} on ${_blockchain} blockchain with name ${_name}`;
                console.log('Event Data:', message);
                if (_to.toLowerCase() === accountName.toLowerCase()) {
                    setEventData({
                        from: _from,
                        to: _to,
                        amount: formatEther(_amount),
                        name: _name,
                        blockchain: _blockchain,
                    });
                }
            };

            const setupEventListener = async (getContract: any) => {
                const TransferTokenContract = getContract();
                console.log('Contract:', TransferTokenContract);

                await TransferTokenContract.on('Transfer', handleTransferEvent);
                contractEventListeners.push(() =>
                    TransferTokenContract.removeAllListeners('Transfer')
                );
            };

            if (type === 'ETH') {
                const { getContractETH } = toTransferETH();
                await setupEventListener(getContractETH);
            } else if (type === 'BSC') {
                const { getContractBSC } = toTransferBSC();
                await setupEventListener(getContractBSC);
            } //... (similar blocks for other blockchains)
        };
        ```

        **Explanation:**
        - **Event Listener Setup:** This function listens for `Transfer` events on various blockchains. When a transaction is detected, the event data (sender, recipient, amount, blockchain, etc.) is captured and logged. If the transaction involves the current user's account, it updates the state with this data.
        - **Dynamic Blockchain Selection:** Depending on the user's selected blockchain (`ETH`, `BSC`, `PLG`, etc.), the corresponding hook is used to get the contract instance and set up the event listener. This modular approach ensures that Soundbox can support multiple blockchains with minimal code duplication.
        - **Real-Time Audio Feedback:** Once the event data is captured, the `speak` function uses the SpeechSynthesis API to provide real-time audio feedback, ensuring users are promptly notified of transactions.

        **Why It Matters:**
        - **Efficiency:** By using modular hooks and centralized event handling, the system remains efficient and scalable, capable of supporting a wide range of blockchains with minimal overhead.
        - **Customization:** The use of hooks allows for easy customization and extension. Developers can add support for new blockchains by simply creating additional hooks and integrating them into the existing framework.
        - **User Experience:** The seamless integration of real-time audio notifications ensures that users are always in the loop, enhancing the overall user experience and providing peace of mind in managing digital assets.

        Soundbox is more than just a notification system—it's a robust, developer-friendly feature that adds tangible value to the nextPay platform. 🚀
    """)

def home():
    # Main Title and Introduction
    st.title("🌟 Welcome to nextPay - The Future of Decentralized Finance 🚀")
    st.image("Assets/home/black white Thunder logo.png", use_column_width=True)
    st.markdown("""
    **nextPay** is not just another decentralized platform—it's a revolution in how you manage and transfer Ethereum across the EVM-based blockchain ecosystem. 
    Our platform is designed to transcend the traditional limitations of cross-chain transactions, offering a seamless, secure, and intuitive experience. 

    Whether you're a DeFi enthusiast, a crypto trader, or simply someone looking to simplify their financial transactions, nextPay has something for everyone. 🌐
    """)

    # Section: Product Overview
    st.subheader("🔍 **Product Overview**")
    st.markdown("""
    nextPay is engineered with cutting-edge blockchain technology, ensuring that your Ethereum can move freely across various EVM-based blockchains without the usual hassle.
    Our platform is built to handle everything from everyday transactions to complex financial operations with ease. Here’s what makes nextPay stand out:

    - **🛡️ Anon Aadhaar Integration:** A secure, anonymous KYC process that uses Aadhaar for identity verification without compromising your privacy. 
    - **🔗 Cross-Blockchain Payments:** Seamlessly transfer Ethereum across multiple EVM-compatible chains like Ethereum, Binance Smart Chain, Polygon, and more. 
    - **🔊 Soundbox:** Stay updated with real-time audio notifications for every transaction, ensuring you never miss a beat.
    - **📅 Competition & Roadmap:** Engage with our community, track our progress, and participate in exciting challenges and events.
    - **❓ FAQs:** Got questions? We’ve got answers. Navigate to our FAQ section to learn more about how nextPay works and how it can benefit you.
    - **🤝 Get Involved:** Whether you're a developer or an end-user, there’s a place for you in the nextPay ecosystem. Discover how you can contribute to our growing community.
    """)

    # Section: Use Cases
    st.subheader("🚀 **Use Cases**")
    st.markdown("""
    nextPay isn’t just a platform—it’s a versatile tool designed to meet the diverse needs of our users. Here are some ways you can leverage nextPay:
    
    - **DeFi Investors:** Optimize your yield farming, staking, and lending activities across multiple chains without the complexity of moving funds manually.
    - **Crypto Traders:** Execute cross-chain trades with minimal fees and instant settlement times, giving you the edge in volatile markets.
    - **Everyday Users:** Simplify your daily transactions with a user-friendly interface that makes cross-chain payments as easy as sending an email.
    - **Businesses:** Integrate nextPay into your operations for secure, transparent, and cost-effective payment solutions across different blockchain networks.
    """)

    # Section: Key Benefits
    st.subheader("✨ **Key Benefits**")
    st.markdown("""
    nextPay offers unparalleled advantages over traditional cross-chain solutions:
    
    - **🚀 Seamless Integration:** nextPay fits seamlessly into your existing DeFi activities, with deep integration into the EVM ecosystem.
    - **🔐 Enhanced Security:** Our platform is built with robust security protocols, ensuring that your assets are protected at all times.
    - **⚡ Lightning-Fast Transactions:** Experience near-instant transaction speeds, even when transferring assets across different blockchains.
    - **💰 Cost-Effective:** nextPay optimizes transaction fees, ensuring that you retain more of your assets with every transfer.
    - **🔊 Real-Time Notifications:** Our Soundbox feature ensures that you’re always in the loop with instant audio alerts for every transaction.
    """)

    # Navigation Section
    st.subheader("🔍 **Explore More**")
    st.markdown("""
    Dive deeper into nextPay’s features and offerings by exploring the following sections:
    
    - [Anon Aadhaar](#anon-aadhaar) - Learn more about our anonymous KYC process.
    - [Cross-Blockchain Payments](#cross-blockchain-payments) - Discover how easy it is to transfer Ethereum across different blockchains.
    - [Soundbox](#soundbox) - Get the details on our real-time transaction notifications.
    - [Competition & Roadmap](#competition-and-roadmap) - Stay updated on our latest developments and community challenges.
    - [FAQs](#faqs) - Find answers to your most pressing questions.
    - [Get Involved](#get-involved) - Join our community and contribute to the future of decentralized finance.
    """)

    # Call to Action
    st.subheader("🎉 **Join the nextPay Revolution Today!**")
    st.markdown("""
    Whether you’re here to manage your crypto assets, explore new opportunities in DeFi, or simply learn more about the power of blockchain technology, nextPay is your go-to platform.
    Sign up today and become part of the decentralized finance revolution! 🚀
    """)


def competition_and_roadmap():
    st.title("🚀 Competition and Roadmap")

    st.subheader("🌐 Competitive Landscape")
    st.write("nextPay operates in a dynamic space with various players in the decentralized finance (DeFi) and blockchain payment sectors. Here’s how nextPay stands out from its key competitors:")

    st.subheader("🤼 Competitors")

    st.markdown("""
    ### **1. MoonPay 🌕**
    - **What They Do:** MoonPay provides a payment infrastructure for cryptocurrencies, allowing users to buy and sell crypto using traditional payment methods like credit cards and bank transfers. They also offer KYC services.
    - **Edge Over Them:** While MoonPay focuses on fiat-to-crypto solutions, nextPay differentiates itself with cross-blockchain Ethereum transfers and anonymous Aadhaar-based KYC. Our use of zk-SNARKs for privacy and real-time transaction notifications via the Soundbox offer enhanced user experience and security not available with MoonPay.

    ### **2. Ramp 🚀**
    - **What They Do:** Ramp specializes in crypto on-ramps, providing KYC services and seamless fiat-to-crypto transactions. They are known for their user-friendly interfaces and integration with various crypto platforms.
    - **Edge Over Them:** Ramp focuses on fiat on-ramps and KYC, but nextPay’s cross-blockchain payment gateway simplifies Ethereum transfers across multiple EVM-based blockchains. Additionally, our anonymous KYC process and Soundbox for instant transaction confirmations offer unique features that Ramp lacks.

    ### **3. Transak 🔄**
    - **What They Do:** Transak is a fiat-to-crypto gateway that offers KYC, AML (Anti-Money Laundering) compliance, and onboarding services for various cryptocurrencies.
    - **Edge Over Them:** Transak excels in fiat on-ramps and KYC compliance, but nextPay goes beyond with cross-blockchain transactions and real-time notifications. Our zk-SNARK-based anonymous KYC provides superior privacy.

    ### **4. Circle (USDC) 💵**
    - **What They Do:** Circle is the issuer of USDC, a leading stablecoin, and provides services like Circle Account and Circle APIs for businesses to integrate stablecoins into their operations.
    - **Edge Over Them:** Circle focuses on stablecoins and fiat-backed cryptocurrencies, whereas nextPay’s cross-blockchain payment gateway supports a broader range of EVM blockchains. Our Soundbox feature adds a real-time, interactive element that Circle’s offerings lack.

    ### **5. Trust Wallet 🔒**
    - **What They Do:** Trust Wallet is a popular mobile wallet supporting a wide range of cryptocurrencies, allowing users to buy, store, and swap tokens, with in-app KYC for fiat-to-crypto purchases.
    - **Edge Over Them:** Trust Wallet primarily serves as a storage and swapping tool with limited cross-blockchain capabilities and real-time notifications. nextPay offers a comprehensive solution with a decentralized payment gateway, anonymous KYC, and the Soundbox, providing a richer platform for cross-blockchain functionalities.
    """)

    st.subheader("🗺️ Roadmap")
    st.write("nextPay is committed to continuous innovation and expanding its features. Here's a high-level roadmap for the platform:")

    st.markdown("""
    - **Phase 1 (Current):**
        - Anon Aadhaar-based anonymous KYC
        - Cross-blockchain Ethereum transfers
        - Soundbox for real-time transaction notifications
    - **Phase 2 (Q3 2024):**
        - Integration with popular DeFi platforms
        - Expansion to additional EVM-based blockchains
        - Introduction of a native nextPay token
    - **Phase 3 (Q1 2025):**
        - Decentralized identity management system
        - Advanced financial services (lending, staking, etc.)
        - Expanded Soundbox features (customizable alerts, smart contract monitoring)
    - **Phase 4 (Q3 2025):**
        - Integration with traditional financial institutions
        - Fiat on-ramp and off-ramp capabilities
        - Governance and DAO implementation
    """)

    st.write("We are dedicated to staying ahead of the competition and continuously enhancing the nextPay platform to provide the best decentralized financial experience for our users. 🌟")

def faqs():
    st.title("❓ FAQs")

    st.subheader("Q1: How does nextPay ensure user privacy during the KYC process?")
    st.write("🔐 nextPay leverages cutting-edge zk-SNARK technology to deliver an anonymous Aadhaar-based KYC process. This means that while we verify your identity, your personal information remains confidential and secure. Only the essential verification proof is stored, ensuring maximum privacy.")

    st.subheader("Q2: What is zk-SNARK, and why is it important?")
    st.write("🛡️ zk-SNARK stands for 'Zero-Knowledge Succinct Non-Interactive Argument of Knowledge.' It's a cryptographic technique that enables one party to prove they know a specific value without disclosing the value itself. In nextPay, zk-SNARK is crucial for preserving user privacy during the KYC process, ensuring your data is protected.")

    st.subheader("Q3: Which blockchains are supported by nextPay?")
    st.write("🌍 nextPay currently supports several EVM-based blockchains, including Ethereum, Binance Smart Chain, Polygon, and Avalanche. We are actively working to expand our compatibility to include additional blockchains, providing you with broader coverage and flexibility.")

    st.subheader("Q4: How does the Soundbox feature work?")
    st.write("🔔 The Soundbox feature delivers real-time audio alerts for each transaction. Users can personalize these alerts based on their preferences for specific blockchains and transaction types, keeping you updated and in control of your financial activities.")

    st.subheader("Q5: What happens if the user is under 18?")
    st.write("🚫 If a user is under 18, nextPay will restrict access to the platform to ensure compliance with legal requirements and safeguard minors from engaging in financial activities that require legal age.")

    st.subheader("Q6: How does nextPay handle cross-blockchain transactions?")
    st.write("🔄 nextPay employs a secure cross-blockchain payment gateway to facilitate Ethereum transfers across various EVM-based blockchains. Our platform manages the entire conversion and transfer process, ensuring transactions are executed smoothly and efficiently.")

    st.subheader("Q7: What makes nextPay different from other decentralized finance platforms?")
    st.write("✨ nextPay distinguishes itself with a unique blend of anonymous Aadhaar-based KYC, cross-blockchain payment capabilities, and real-time transaction alerts through the Soundbox. This combination delivers a more secure, private, and informed financial experience compared to other DeFi platforms.")

    st.subheader("Q8: Can nextPay be integrated with other DeFi applications?")
    st.write("🔗 Absolutely! nextPay is designed to be interoperable with other DeFi applications, allowing you to leverage our features in conjunction with a variety of tools and services within the decentralized finance ecosystem.")

def get_involved():
    st.title("🌟 Get Involved with nextPay")

    st.subheader("🤝 Contribute to nextPay")
    st.write("We welcome contributions from the community to help shape the future of nextPay. Here’s how you can get involved and make an impact:")

    st.markdown("""
    1. **Fork the Repository**: Click the "Fork" button on the [nextPay GitHub repository](https://github.com/nextPay/nextPay) to create your own copy of the project. 🍴
    2. **Clone Your Fork**: Clone the repository to your local machine using:
    ```bash
    git clone https://github.com/your-username/nextPay.git
    ```
    🖥️
    3. **Set Up Development Environment**: Navigate to the project directory and install dependencies:
    ```bash
    cd nextPay
    npm install
    ```
    ⚙️
    4. **Make Changes**: Create a new branch, make your changes, and commit them. ✏️
    5. **Submit a Pull Request**: Push your changes to your fork and submit a pull request to contribute your improvements. 🔄
    """)

    st.write("We're excited to see your contributions! Thank you for being a part of the nextPay community. 🙌")

    if st.button("Visit GitHub Repository"):
        st.markdown('<a href="https://github.com/harshit340/NextPay" target="_blank">nextPay GitHub Repository</a>', unsafe_allow_html=True)

def main():
    pages = {
        "Home": home,
        "Anon Aadhaar": anon_aadhaar,
        "Cross-Blockchain Payments": cross_blockchain_payments,
        "Soundbox": soundbox,
        "Competition and Roadmap": competition_and_roadmap,
        "FAQs": faqs,
        "Get Involved": get_involved,
    }

    # Create a sidebar with a list of pages
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Select a Page", list(pages.keys()), index=0)

    # Display the selected page
    pages[selected_page]()

if __name__ == "__main__":
    main()