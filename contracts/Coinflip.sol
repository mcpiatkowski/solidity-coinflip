pragma solidity ^0.8.9;

/// @author szaleju
/// @title Simple onchain coinflip.
contract Coinflip {
    enum CoinflipStatus {
        DONE,
        OPEN,
        FLIPPING
    }

    enum Side {
        UNKNOWN,
        HEADS,
        TAILS
    }

    enum PlayerStatus {
        UNKNOWN,
        COWARD,
        JOINED
    }

    CoinflipStatus public coinflipStatus;

    address public owner;
    uint public pot;
    uint public minBet;
    uint public betAmount;
    uint public maxPlayers;
    address[] public bagOfPlayers;
    address[] public bagOfWinners;
    mapping(address => Player) public players;

    struct Player {
        Side side;
        PlayerStatus status;
    }

    event Bet(uint value, address sender);
    event Join(PlayerStatus status, address sender);

    constructor() {
        minBet = 1;
        maxPlayers = 20;
        owner = msg.sender;
        coinflipStatus = CoinflipStatus.DONE;
    }

    /// @dev This has to be one dollar. Conversion at current eth price is yet to be implemented.
    /// @param _minBet Minimum amount to start the game with.
    function setMinBet(uint _minBet) external {
        require(msg.sender == owner, "Only owner can set minimal bet amount.");
        minBet = _minBet;
    }

    /// @param _maxPlayers Set maximum number of players to join the game.
    /// @dev Can we set a length of an array with another variable in the contract?
    function setMaxPlayers(uint _maxPlayers) external {
        require(msg.sender == owner, "Only owner can set maximum number of players.");
        maxPlayers = _maxPlayers;
    }

    /// @notice Starting a game makes you automatically a participant.
    /// @param side Side of the coin to bet on.
    function start(Side side) external payable {
        require(coinflipStatus == CoinflipStatus.DONE, "Coinflip is in progress. Try to join the game.");
        require(msg.value >= minBet, "Gimme moar coins! Minimal bet is 1$.");
        require(bagOfWinners.length == 0, "There are still some winners to be paid.");
        require(bagOfPlayers.length == 0, "There are still some players from previous game.");
        coinflipStatus = CoinflipStatus.OPEN;
        betAmount = msg.value;
        _join(msg.sender, side);
        _bet(msg.value, msg.sender);
    }

    // @param side Side of the coin to bet on.
    function join(Side side) external payable {
        Player memory player = players[msg.sender];
        require(coinflipStatus == CoinflipStatus.OPEN, "Please start the game first.");
        require(bagOfPlayers.length < maxPlayers, "Maximum number of players joined the game.");
        require(player.status != PlayerStatus.JOINED, "You have already joined you greedy!");
        require(msg.value == betAmount, "Your bet needs to match current game bet amount.");
        _join(msg.sender, side);
        _bet(msg.value, msg.sender);
    }

    /// @dev There is also jackpot variable which supposed to collect some part of the bet for streak wins.
    /// @param _betAmount Amount for current game.
    /// @param player Address of the player.
    function _bet(uint _betAmount, address player) internal {
        pot += _betAmount;
        emit Bet(_betAmount, player);
    }

    // @param player Address of the player.
    // @param side Side of the coin to bet on.
    function _join(address player, Side side) internal {
        bagOfPlayers.push(player);
        players[player] = Player({side: side, status: PlayerStatus.JOINED});
        emit Join(PlayerStatus.JOINED, player);
    }
}
