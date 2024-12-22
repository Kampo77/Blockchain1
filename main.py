import hashlib
import time
import json

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions

    def create_merkle_root(self):
        hashes = [self.hash_transaction(tx) for tx in self.transactions]
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1])
            hashes = [self.hash_pair(hashes[i], hashes[i + 1]) for i in range(0, len(hashes), 2)]
        return hashes[0] if hashes else None

    @staticmethod
    def hash_transaction(transaction):
        tx_string = json.dumps(transaction, sort_keys=True).encode()
        return hashlib.sha256(tx_string).hexdigest()

    @staticmethod
    def hash_pair(hash1, hash2):
        combined = (hash1 + hash2).encode()
        return hashlib.sha256(combined).hexdigest()

class Block:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.merkle_root = MerkleTree(transactions).create_merkle_root()
        self.nonce = 0
        self.hash = None

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        while not self.hash or not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.previous_hash}{self.timestamp}{self.merkle_root}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("0", ["Genesis Block"])
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(previous_hash, transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def validate_blockchain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False

        return True

# Demonstration
if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)

    transactions_block1 = [
        {"sender": "Alice", "receiver": "Bob", "amount": 10},
        {"sender": "Charlie", "receiver": "Dave", "amount": 20},
        {"sender": "Eve", "receiver": "Frank", "amount": 15},
        {"sender": "Grace", "receiver": "Heidi", "amount": 25},
        {"sender": "Ivan", "receiver": "Judy", "amount": 30},
        {"sender": "Mallory", "receiver": "Niaj", "amount": 5},
        {"sender": "Oscar", "receiver": "Peggy", "amount": 40},
        {"sender": "Sybil", "receiver": "Trent", "amount": 50},
        {"sender": "Victor", "receiver": "Walter", "amount": 35},
        {"sender": "Xander", "receiver": "Yvonne", "amount": 45}
    ]

    blockchain.add_block(transactions_block1)

    transactions_block2 = [
        {"sender": "Zara", "receiver": "Alice", "amount": 60},
        {"sender": "Bob", "receiver": "Charlie", "amount": 70},
        {"sender": "Dave", "receiver": "Eve", "amount": 80},
        {"sender": "Frank", "receiver": "Grace", "amount": 90},
        {"sender": "Heidi", "receiver": "Ivan", "amount": 100},
        {"sender": "Judy", "receiver": "Mallory", "amount": 110},
        {"sender": "Niaj", "receiver": "Oscar", "amount": 120},
        {"sender": "Peggy", "receiver": "Sybil", "amount": 130},
        {"sender": "Trent", "receiver": "Victor", "amount": 140},
        {"sender": "Walter", "receiver": "Xander", "amount": 150}
    ]

    blockchain.add_block(transactions_block2)

    print("Blockchain valid:", blockchain.validate_blockchain())
