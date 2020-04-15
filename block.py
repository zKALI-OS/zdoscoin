import hashlib


class Block:

    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp

    def calculate_hash(self):
        block_of_string = (
            f'{{{self.index}}}'
            f'{{{self.proof_no}}}'
            f'{{{self.prev_hash}}}'
            f'{{{self.data}}}'
            f'{{{self.timestamp}}}'
        )

        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return (
            f'{{{self.index}}}-'
            f'{{{self.proof_no}}}-'
            f'{{{self.prev_hash}}}-'
            f'{{{self.data}}}-'
            f'{{{self.timestamp}}}'
        )
