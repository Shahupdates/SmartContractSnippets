
// This is a simple ERC721 non-fungible token (NFT) implementation.
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC721.sol";

contract SimpleERC721 is ERC721 {
    uint256 private _tokenIdCounter;

    constructor() ERC721("SimpleERC721", "S721") {}

    function _baseURI() internal pure override returns (string memory) {
        return "https://my-json-server.typicode.com/demo/";
    }

    function mint(address to) public {
        _mint(to, _tokenIdCounter);
        _tokenIdCounter++;
    }
}
