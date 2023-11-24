__all__ = ("CoinSide", "PlayerStatus", "CoinflipStatus")

from collections import namedtuple

CoinSide = namedtuple("coin_side", ["heads", "tails", "unknown"])
PlayerStatus = namedtuple("player_status", ["coward", "joined", "unknown"])
CoinflipStatus = namedtuple("coinflip_status", ["done", "open", "flipping"])
