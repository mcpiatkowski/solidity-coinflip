from typing import List

import pytest
from ape.api import AccountAPI
from ape.contracts.base import ContractInstance
from ape.exceptions import ContractLogicError


def test_deployed(coinflip: ContractInstance, owner: AccountAPI) -> None:
    """Test if contract is deployed as expected."""
    assert coinflip.minBet() == 1
    assert coinflip.owner() == owner
    assert coinflip.maxPlayers() == 20
    assert coinflip.coinflipStatus() == 0


def test_set_max_players_by_owner(coinflip: ContractInstance, owner: AccountAPI) -> None:
    """Test max players set by the owner."""
    assert coinflip.maxPlayers() == 20
    coinflip.setMaxPlayers(25, sender=owner)
    assert coinflip.maxPlayers() == 25


def test_set_max_players_by_player(coinflip: ContractInstance, players: List[AccountAPI]):
    """Test max players set by a player."""
    assert coinflip.maxPlayers() == 20
    with pytest.raises(ContractLogicError) as err:
        coinflip.setMaxPlayers(25, sender=players[0])
    assert err.value.args[0] == "Only owner can set maximum number of players."
