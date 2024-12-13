from mnemonic import Mnemonic
from bip32 import BIP32
from eth_account import Account
from web3 import Web3
import time  # Import time for sleep functionality
import requests  # Import requests to handle exceptions

# Create a Mnemonic object for English
mnemo = Mnemonic("english")

# Connect to Infura
infura_url = "https://mainnet.infura.io/v3/1e1edc00c0df4051b5b857c2d4f4d286"  # Replace with your Infura Project ID
web3 = Web3(Web3.HTTPProvider(infura_url))

while True:  # Infinite loop
    # Generate a 12-word mnemonic
    mnemonic_phrase = mnemo.generate(strength=128)  # 128 bits = 12 words
    print("Mnemonic Phrase:", mnemonic_phrase)

    # Derive seed from mnemonic
    seed = mnemo.to_seed(mnemonic_phrase)

    # Create BIP32 instance
    bip32 = BIP32.from_seed(seed)

    # Derive the first account (m/44'/60'/0'/0/0)
    private_key = bip32.get_privkey_from_path("m/44'/60'/0'/0/0")
    account = Account.from_key(private_key)

    # Get the wallet address
    wallet_address = account.address
    print("Wallet Address:", wallet_address)

    # Check the balance with error handling
    while True:  # Retry loop for balance checking
        try:
            balance_wei = web3.eth.get_balance(wallet_address)
            balance_eth = web3.from_wei(balance_wei, 'ether')  # Updated method name
            print("Wallet Balance (ETH):", balance_eth)

            # Check if balance is greater than 0
            if balance_eth > 0:
                # Save the mnemonic to a file named keys.txt
                with open("keys.txt", "a") as f:  # Append to the file
                    f.write(f"Mnemonic Phrase: {mnemonic_phrase}, Wallet Address: {wallet_address}, Balance: {balance_eth} ETH\n")
                print("Mnemonic saved to keys.txt and program will stop.")
                break  # Exit the loop
            break  # Exit the retry loop if balance check is successful

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Check for 429 error
                print("Rate limit exceeded. Retrying in 10 seconds...")
                time.sleep(10)  # Wait before retrying
            else:
                print("An error occurred:", e)
                break  # Exit the retry loop on other errors
