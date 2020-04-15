
import pytest

from fcc_coin.block import Block


@pytest.fixture
def zero_block():
    return Block(0, 0, 0, 0, 0)


def test_block_can_be_instantiated(zero_block):
    assert isinstance(zero_block, Block)


def test_calculate_hash(zero_block):
    hash = "15e8d1deeb2d39979fc46431b914d5731197637450bb76dd297fe9fb5ea0de7a"

    assert zero_block.calculate_hash() == hash
