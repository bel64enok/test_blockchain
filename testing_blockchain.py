from blockchain_filling import Block
from blockchain_filling import Blockchain
from time import time


JeChain = Blockchain()

# Добавим новый блок
JeChain.addBlock(Block(str(int(time())), ({"from": "John", "to": "Bob", "amount": 100})))
JeChain.addBlock(Block(str(int(time())), ({"from": "Bob", "to": "John", "amount": 200})))
JeChain.addBlock(Block(str(int(time())), ({"from": "Ken", "to": "John", "amount": 200})))
# (Это - всего лишь интересный эксперимент, для создания настоящей криптовалюты обычно нужно сделать намного больше, чем сделали мы).

# Вывод обновлённого блокчейна
print(JeChain)

for_json = (f"{JeChain}")

import csv

cols = ['']

data = [
    {'': for_json}
]
# Необходимо указать путь до файла
path = "/Users/i.shutikhin/Desktop/test_blockchain/csv.numbers"
with open(path, 'w') as f:
    wr = csv.DictWriter(f, fieldnames = cols)
    wr.writeheader()
    wr.writerows(data)