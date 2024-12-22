import hashlib
import time

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions

    def create_merkle_root(self):
        hashes = [self.hash_transaction(tx) for tx in self.transactions]
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1])  # double up the last hash if odd
            hashes = [self.hash_pair(hashes[i], hashes[i + 1]) for i in range(0, len(hashes), 2)]
        return hashes[0] if hashes else None

    @staticmethod
    def hash_transaction(transaction):
        tx_string = str(transaction).encode()
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
        self.merkle_root = None
        self.nonce = 0
        self.hash = None
    def calculate_hash(self):
        block_data = (f"{self.previous_hash}"
                      f"{self.timestamp}"
                      f"{self.merkle_root}"
                      f"{self.nonce}")
        return hashlib.sha256(block_data.encode()).hexdigest()
    def mine_block(self, difficulty):
        self.merkle_root = MerkleTree(self.transactions).create_merkle_root()
        target = "0" * difficulty
        while True:
            self.hash = self.calculate_hash()
            if self.hash[:difficulty] == target:
                break
            self.nonce += 1

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty

    def create_genesis_block(self):
        pass  # TODO

    def add_block(self, transactions):
        pass  # TODO

    def validate_blockchain(self):
        pass  # TODO

# TODO: demonstraiton of work below 
