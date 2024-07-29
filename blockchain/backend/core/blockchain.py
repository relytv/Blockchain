from block import Block
from blockheader import BlockHeader
from util import hash256
import time
import json

ZERO_HASH = "0" * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesisBlock()

    def genesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        transaction = f"Код оповещения отправлен {BlockHeight}"
        merkelRoot = hash256(transaction.encode()).hex()
        bits = "ffff001f"
        blockheader = BlockHeader(VERSION, prevBlockHash, merkelRoot, timestamp, bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader.__dict__, 1, transaction).__dict__)
        print(json.dumps(self.chain, indent=4))

    def main(self):
        while True:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]["Height"] + 1
            prevBlockHash = lastBlock[0]["BlockHeader"]["blockHash"]
            self.addBlock(BlockHeight, prevBlockHash)


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()


