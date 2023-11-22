from ape.api import AccountAPI
import pytest
from ape.contracts.base import ContractInstance
from ape import accounts, project


@pytest.fixture
def owner() -> AccountAPI:
    """Deployer of the contract."""
    return accounts.test_accounts[0]


@pytest.fixture
def coinflip(owner: AccountAPI) -> ContractInstance:
    """Coinflip contract instance."""
    return owner.deploy(project.Coinflip)
