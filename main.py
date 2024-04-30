import json
import hashlib
import os

def validate_transaction(transaction):
    """
    Function to validate a transaction.
    You can implement your own transaction validation logic here.
    For simplicity, this function always returns True.
    """
    return True

def calculate_transaction_hash(transaction):
    """
    Function to calculate the hash of a transaction.
    This hash can be used as the transaction ID (txid).
    """
    transaction_string = json.dumps(transaction, sort_keys=True)
    return hashlib.sha256(transaction_string.encode()).hexdigest()

def mine_block(transactions):
    """
    Function to mine a block from a list of transactions.
    """
    # Construct the block header
    block_header = "Difficulty Target: 0000ffff00000000000000000000000000000000000000000000000000000000"

    # Serialize the coinbase transaction
    coinbase_transaction = {
        "txid": "coinbase_txid",
        "inputs": [],
        "outputs": [{"value": 50, "address": "miner_address"}]  # Coinbase reward
    }

    # Initialize the list of transaction IDs (txids)
    txids = [coinbase_transaction['txid']]

    # Mine the block
    for transaction in transactions:
        if validate_transaction(transaction):
            txid = calculate_transaction_hash(transaction)
            txids.append(txid)

    return block_header, coinbase_transaction, txids

def main():
    """
    Main function to process transactions and mine a block.
    """
    # Read transaction files from the mempool folder
    mempool_path = "./mempool/"
    transactions = []

    # Loop through each transaction file in the mempool folder
    for filename in os.listdir(mempool_path):
        with open(os.path.join(mempool_path, filename), "r") as file:
            transaction = json.load(file)
            transactions.append(transaction)

    # Mine the block
    block_header, coinbase_transaction, txids = mine_block(transactions)

    # Write the block data to output.txt
    with open("output.txt", "w") as output_file:
        output_file.write(block_header + "\n")
        output_file.write(json.dumps(coinbase_transaction) + "\n")
        for txid in txids:
            output_file.write(txid + "\n")

if __name__ == "__main__":
    main()
