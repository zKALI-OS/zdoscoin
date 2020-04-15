import pytest

from fcc_coin.block_chain import BlockChain
from fcc_coin.block import Block


@pytest.fixture
def block_chain():
    return BlockChain(Block)


def test_can_be_instantiated(block_chain):
    assert isinstance(block_chain, BlockChain)


def test_creates_genesis_block(block_chain):
    genesis_block = block_chain.chain[0]

    assert genesis_block.proof_no == 0
    assert genesis_block.prev_hash == 0
    assert genesis_block.data == 0


def test_can_add_new_blocks_to_chain(block_chain):
    block = block_chain.construct_block(0, 0, 0)

    assert block_chain.chain[1] == block


def test_block_validity_true_if_2_consecutive_blocks_are_valid(block_chain):
    prev_block = block_chain.construct_block(0, 0, 0)
    prev_hash = prev_block.calculate_hash()
    block = block_chain.construct_block(0, prev_hash, 0)

    assert BlockChain.check_validity(block, prev_block) is True


def test_block_validity_false_if_2_consective_blocks_are_invalid(block_chain):
    prev_block = block_chain.construct_block(0, 0, 0)
    prev_hash = prev_block.calculate_hash()
    block = block_chain.construct_block(0, prev_hash, 0)

    prev_block.data = 1

    assert BlockChain.check_validity(block, prev_block) is False


def test_verifying_proof_checks_hash_contains_4_leading_zeroes(block_chain):
    assert block_chain.verifying_proof(0, 0) is False
    assert block_chain.verifying_proof(69732, 0) is True


def test_proof_of_work_uses_verifying_proof_and_returns_proof_no(block_chain):
    proof_no = block_chain.proof_of_work(0)

    assert proof_no == 69732


def test_last_block_returns_last_block_in_chain(block_chain):
    genesis_block = block_chain.chain[0]

    assert block_chain.last_block == genesis_block

    next_block = block_chain.construct_block(0, 0, 0)

    assert block_chain.last_block == next_block
