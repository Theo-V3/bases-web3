import json
from web3 import Web3

avalanche_url = "https://api.avax.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(avalanche_url))

with open ('contrat.json') as g:
    abi = json.load(g)
address2 = ("0xc7198437980c041c805A1EDcbA50c1Ce5db95118")

contract = web3.eth.contract(abi=abi, address=address2)
balance = contract.functions.balanceOf('0xED2a7edd7413021d440b09D654f3b87712abAB66').call()
print(balance)