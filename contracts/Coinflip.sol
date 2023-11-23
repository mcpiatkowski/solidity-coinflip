pragma solidity ^0.8.9;


contract Coinflip {
    enum CoinflipStatus {
        DONE,
        OPEN,
        FLIPPING
    }

    CoinflipStatus public coinflipStatus;

    address public owner;

    uint public minBet;
    uint public maxPlayers;

    constructor() {
        minBet = 1;
        maxPlayers = 20;
        owner = msg.sender;
        coinflipStatus = CoinflipStatus.DONE;
    }

    function setMinBet(uint _minBet) external {
        require(msg.sender == owner, "Only owner can set minimal bet amount.");
        minBet = _minBet;
    }

    function setMaxPlayers(uint _maxPlayers) external {
        require(msg.sender == owner, "Only owner can set maximum number of players.");
        maxPlayers = _maxPlayers;
    }
}
