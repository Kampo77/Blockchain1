import hashlib
import time

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions

    def create_merkle_root(self):
        pass  # TODO

class Block:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.merkle_root = None
        self.nonce = 0
        self.hash = None

    def mine_block(self, difficulty):
        pass  # TODO

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
