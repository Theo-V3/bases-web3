import json
from web3 import Web3

avalanche_url = "https://api.avax.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(avalanche_url))

#la on met les données du contrat abi + adresse
#j'ai créer un dossier pour éviter d'avoir trop de lignes inutiles : abi = json.loads('abi du token')
#je met directement l'abi dans le fichier json et j'écrit ça:
with open ("contrat.json") as f:
    avaxabi = json.load(f)
address = '0xc7198437980c041c805A1EDcbA50c1Ce5db95118'

#Pas trop capté mais bref ça lit le contrat quoi
contract = web3.eth.contract(address=address, abi=avaxabi)
print(contract)

#call fonction = lire des données sur la BC
#send fonction = écrire des données sur la BC
totalSupply = contract.functions.totalSupply().call()
print(totalSupply)

#SI MAUVAIS NOMBRE A CAUSE DES DECIMALES : faire  print(web3.fromWei(totalSupply, 'ether')) 
#ça fait la conversion en ether au lieu de Wei --> décimales à la bonne place

#Avoir le nom du token 
print(contract.functions.name().call())


