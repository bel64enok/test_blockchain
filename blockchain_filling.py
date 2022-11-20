# -*- coding: utf-8 -*-

from hashlib import sha256
import json
from time import time

class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        # В self.data должна храниться информация, вроде сведений о транзакциях.
        self.data = [] if data is None else data
        self.prevHash = None # Хеш предыдущего блока
        self.nonce = 0
        self.hash = self.getHash()

    def getHash(self):

        hash = sha256()
        hash.update(str(self.prevHash).encode('utf-8'))
        hash.update(str(self.timestamp).encode('utf-8'))
        hash.update(str(self.data).encode('utf-8'))
        hash.update(str(self.nonce).encode('utf-8'))
        return hash.hexdigest()

    #хеш-функция
    def mine(self, difficulty):
        # Тут запускается цикл, работающий до тех пор, пока хеш не будет начинаться со строки
        # 0...000 длины <difficulty>.
        while self.hash[:difficulty] != '0' * difficulty:
            # Инкрементируем nonce, что позволяет получить совершенно новый хеш.
            self.nonce += 1
            # Пересчитываем хеш блока с учётом нового значения nonce.
            self.hash = self.getHash()

class Blockchain:

    def __init__(self):
        self.chain = [Block(str(int(time())))]
        # В этом свойстве будут содержаться все блоки.
        self.difficulty = 1
        self.blockTime = 30000

    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, block):
        block.prevHash = self.getLastBlock().hash
        block.hash = block.getHash()
        block.mine(self.difficulty)
        self.chain.append(block)

        self.difficulty += (-1, 1)[int(time()) - int(self.getLastBlock().timestamp) < self.blockTime]

    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            prevBlock = self.chain[i - 1]

            if (currentBlock.hash != currentBlock.getHash() or prevBlock.hash != currentBlock.prevHash):
                return False

        return True

    def __repr__(self):
        return json.dumps([{'data': item.data, 'timestamp': item.timestamp, 'nonce': item.nonce, 'hash': item.hash, 'prevHash': item.prevHash} for item in self.chain], indent=4)
