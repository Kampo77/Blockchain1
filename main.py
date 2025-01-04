import time
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash="1", proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time.time()),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

# Demonstration
if __name__ == "__main__":
    blockchain = Blockchain()
    
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.create_block(proof=200, previous_hash="hash_value")

    blockchain.add_transaction("Charlie", "Dave", 20)
    blockchain.create_block(proof=300, previous_hash="hash_value")

    print("Blockchain:")
    for block in blockchain.chain:
        print(block)
