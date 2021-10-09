import infura

ifr = infura.Client(
    project_id='aaf2bdc4b77a4c669735736d82839e50',
    project_secret='32b046ab81414aff82a274dd650fb2f0',
    network='ropsten',
    cache_expire_after=5,
)

gas_price = ifr.eth_get_gas_price()

balance = ifr.eth_get_balance('0xcDA0D6adCD0f1CCeA6795F9b1F23a27ae643FE7C')
print(balance)
