import asyncio
def gcd(a, b):    while b:
        a, b = b, a % b    return a
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1    if m == 1:
        return 0    while a > 1:
        q = a // m        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0    if x1 < 0:
        x1 += m0    return x1
def generate_keys():
    p = 61    q = 53
    n = p * q    phi_n = (p - 1) * (q - 1)
    e = 17    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)
def simple_hash(data):    hash_value = 0
    for char in str(data):        hash_value = (hash_value * 31 + ord(char)) % 1000000007
    return hash_value
def sign(private_key, document):    d, n = private_key
    document_hash = simple_hash(document)    return pow(document_hash, d, n)
def verify(public_key, document, signature):
    e, n = public_key    document_hash = simple_hash(document)
    decrypted_hash = pow(signature, e, n)    return decrypted_hash == document_hash

class Blockchain:    def __init__(self):
        self.chain = []
        self.pending_transactions = []        self.create_block(previous_hash="1", proof=100)
    def create_block(self, proof, previous_hash):
        block = {            'index': len(self.chain) + 1,
            'transactions': self.pending_transactions,            'proof': proof,
            'previous_hash': previous_hash        }
        self.pending_transactions = []        self.chain.append(block)
        return block
    async def add_transaction(self, sender, receiver, amount, signature):        transaction = {
            'sender': sender,            'receiver': receiver,
            'amount': amount,            'signature': signature
        }        self.pending_transactions.append(transaction)
        # Simulate a delay for transaction processing        await asyncio.sleep(1)
        return self.last_block['index'] + 1
    async def verify_transaction(self, transaction):        sender_public_key = transaction['sender']
        signature = transaction['signature']        document = str(transaction)
        await asyncio.sleep(0.5)  # Simulate verification delay        return verify(sender_public_key, document, signature)
    @property
    def last_block(self):        return self.chain[-1]

class Wallet:    def __init__(self):
        self.private_key, self.public_key = generate_keys()
    def sign_transaction(self, transaction):        return sign(self.private_key, transaction)
    async def send_transaction(self, blockchain, receiver, amount):
        transaction = {            'sender': self.public_key,
            'receiver': receiver,            'amount': amount
        }        signature = self.sign_transaction(str(transaction))
        await blockchain.add_transaction(self.public_key, receiver, amount, signature)
# Asynchronous demonstration
async def main():    blockchain = Blockchain()
    wallet = Wallet()
    sender = wallet.public_key    receiver = wallet.public_key  # Assuming a self-transaction
    amount = 10
    # Sending transaction asynchronously    await wallet.send_transaction(blockchain, receiver, amount)
    blockchain.create_block(proof=200, previous_hash="hash_value")
    print("Blockchain:")    for block in blockchain.chain:
        print(block)
# Run the asynchronous main function
asyncio.run(main())
