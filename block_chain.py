import hashlib


class BlockChain:

    def __init__(self, block):
        self.block = block
        self.chain = []
        self.construct_genesis()

    def construct_block(self, proof_no, prev_hash, data):
        block = self.block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=data
        )

        self.chain.append(block)
        return block

    def construct_genesis(self):
        genesis_block = self.construct_block(proof_no=0, prev_hash=0, data=0)

        return genesis_block

    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.calculate_hash() != block.prev_hash:
            return False
        elif prev_block.timestamp and block.timestamp:
            if prev_block.timestamp > block.timestamp:
                return False

        return True

    def proof_of_work(self, last_proof):
        '''A simple algorithm indentifies a number Y such that hash(XY)
            contains 4 leading zeroes
            X is the previous Y
            Y is the new proof
            '''
        proof_no = 0
        while self.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    def verifying_proof(self, proof, last_proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == '0000'

    @property
    def last_block(self):
        return self.chain[-1]
