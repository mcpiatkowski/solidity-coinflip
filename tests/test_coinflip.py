from ape.api import AccountAPI
from ape.contracts.base import ContractInstance


# def test_deployed(owner: AccountAPI, coinflip: ContractInstance) -> None:
#
#     account = coinflip.owner()
#     assert account == owner


def test_deployed(coinflip: ContractInstance, owner: AccountAPI) -> None:
    """Test if contract is deployed as expected."""
    assert coinflip.minBet() == 1
    assert coinflip.owner() == owner
    assert coinflip.maxPlayers() == 20
    assert coinflip.coinflipStatus() == 0
