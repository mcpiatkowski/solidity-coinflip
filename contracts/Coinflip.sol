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

    function setMaxPlayers(uint _maxPlayers) public {
        maxPlayers = _maxPlayers;
    }
}

