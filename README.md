
# Metamask Brute-Force Project

This repository contains a Python-based script used to perform brute-force attacks on Metamask wallets. The script attempts various combinations to gain unauthorized access to Metamask accounts. **This project is intended for educational purposes only. Please use this script only with the appropriate authorization from the account owner.** 

## Features
- Automatic password and private key trials for Metamask wallets.
- Customizable options for brute-force settings.
- Integration with common password patterns.
- Logging of attempted accesses.

## Requirements
- Python (latest version, 3.x)
- `mnemonic` library: For managing mnemonic codes.
- `bip32` library: For BIP32 (Bitcoin Improvement Proposal 32) wallet management.
- `eth_account` library: For Ethereum wallet operations.
- `web3` library: For Ethereum network operations.
- `requests` library: For handling HTTP operations and exceptions.

```bash
# Clone the repository
git clone https://github.com/ottomanturkss/metamask-brute-force.git

# Install the required libraries
pip install mnemonic bip32-python eth-account web3 requests
```

## Usage
1. After cloning the repository:
   ```bash
   cd metamask-brute-force
   ```

2. Configure the script:
   - Update the Infura connection information in the script with your `YOUR_INFURA_ID`:
     ```python
     infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_ID"
     ```
   - Set target Metamask wallets and brute-force settings.
   - Adjust password patterns and attempts to suit your needs.

3. Run the script:
   ```bash
   python brute_force.py
   ```

4. **Important Notes:**
   - This project is provided for educational purposes only.
   - **No responsibility is taken for any misuse of this script.**
   - Unauthorized use of this tool is illegal and unethical.
   - Infura API ID is required to use this script. Obtain an Infura account and replace the `YOUR_INFURA_ID` in the script with your own Infura API ID.
   - The script automatically scans Metamask wallets for private keys and halts operation upon finding a wallet with a non-zero balance. The discovered private keys are saved in `keys.txt`.

## Warning
- This script is for educational and research purposes only.
- Unauthorized use of this tool is illegal and unethical.
- Misuse of this script can lead to legal and ethical consequences.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
For reviews or questions, you can contact the repository owner via email or onur.altun@yahoo.com

## Donations
If you found this project useful and wish to support it, you can donate to the following addresses:
- **BTC**: bc1qj224dp8zcpvh0mc5qvwlu53u7vhsl3qef9yz2c
- **ETH**: 0xCcEd5136D711238c4d8089285BcB6BE282a46315
- **DOT**: 15ZgdnmYPsdYk5Z2oatj58Rxop8ZJV4qboLVvviv1bqCBUFG
- **TRX**: TGf4Kgvx9rmj9vqjWajEQEevGcEGwWWrvF
- **SOL**: 3wLYGco5ybKob6LeaN2XT1nfdzFr4N9egFqmiXueueWU
- **BNB**: 0xCcEd5136D711238c4d8089285BcB6BE282a46315
- **XRP**: rDM7BrvfoKKiwQSgV7qGCConA137AyzmRC
