from blockchain_filling import Block
from blockchain_filling import Blockchain
from time import time

JeChain = Blockchain()

# Добавим новый блок
JeChain.addBlock(Block(str(int(time())), ({"from": "John", "to": "Bob", "amount": 100})))
# (Это - всего лишь интересный эксперимент, для создания настоящей криптовалюты обычно нужно сделать намного больше, чем сделали мы).

# Вывод обновлённого блокчейна
print(JeChain)