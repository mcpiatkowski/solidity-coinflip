from typing import List

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
def coinflip(owner: AccountAPI) -> ContractInstance:
    """Coinflip contract instance."""
    return owner.deploy(project.Coinflip)
