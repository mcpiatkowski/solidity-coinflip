from typing import List
from contract_typing import CoinSide, PlayerStatus, CoinflipStatus

import pytest
from ape import accounts, project
from ape.api import AccountAPI
from ape.contracts.base import ContractInstance


@pytest.fixture
def owner() -> AccountAPI:
    """Deployer of the contract."""
    return accounts.test_accounts[0]


@pytest.fixture
def hacker() -> AccountAPI:
    """Contract hacker."""
    return accounts.test_accounts[9]


@pytest.fixture
def player_one() -> AccountAPI:
    """Player number one."""
    return accounts.test_accounts[1]


@pytest.fixture
def player_two() -> AccountAPI:
    """Player number two."""
    return accounts.test_accounts[2]


@pytest.fixture
def player_three() -> AccountAPI:
    """Player number three."""
    return accounts.test_accounts[3]


@pytest.fixture
def players(player_one, player_two, player_three) -> List[AccountAPI]:
    """Players to join the game."""
    return [
        player_one,
        player_two,
        player_three
    ]


@pytest.fixture
def player_status() -> PlayerStatus:
    """Numeric representation of the player status."""
    return PlayerStatus(unknown=0, coward=1, joined=2)


@pytest.fixture
def coinflip_status() -> CoinflipStatus:
    """Numeric representation of the game status."""
    return CoinflipStatus(done=0, open=1, flipping=2)


@pytest.fixture
def coin_side() -> CoinSide:
    """Numeric representation of the coin side."""
    return CoinSide(unknown=0, heads=1, tails=2)


@pytest.fixture
def coinflip(owner: AccountAPI) -> ContractInstance:
    """Coinflip contract instance."""
    return owner.deploy(project.Coinflip)


@pytest.fixture
def middle_game(coinflip: ContractInstance, coin_side: CoinSide, players: List[AccountAPI]):
    """Coinflip contract with game opened."""
    coinflip.start(coin_side.heads, sender=players[0], value=10)
    coinflip.join(coin_side.tails, sender=players[1], value=10)
    coinflip.join(coin_side.heads, sender=players[2], value=10)
    return coinflip
