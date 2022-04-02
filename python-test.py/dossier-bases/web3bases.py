import json
from web3 import Web3

#Se connecter à la blockchain (Avalanche)
avalanche_url = "https://api.avax.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(avalanche_url))

#Vérifier si elle est bien connectée
allo = web3.isConnected()
print(allo)

#Afficher le dernier block de la C-chain
block = web3.eth.blockNumber
print(block)

#Afficher le nombre d'avax présents dans une adresse --> en conversion ether. car sinon en Wei --> 18 décimales et impossible à lire
benj = web3.toChecksumAddress("0x92ff72fc3f3e59ad56c53ac35e6b403cb12ee069")
balance = web3.fromWei(web3.eth.getBalance(benj), 'ether')
print("balance :", balance) 

#Pour se connecter à un SC on a besoin d'une ABI et d'une adresse.
#la on met les données du contrat abi + adresse
#j'ai créer un dossier pour éviter d'avoir trop de lignes inutiles : abi = json.loads('abi du token')
#je met directement l'abi dans le fichier json et j'écrit ça:
with open ("contrat.json") as f:
    avaxabi = json.load(f)
adress = "0x4f60a160D8C2DDdaAfe16FCC57566dB84D674BD6" 

contract = web3.eth.contract(address=adress, abi=avaxabi)

totalSupply = contract.functions.totalSupply().call()
print(contract.functions.name().call())
print(contract.functions.symbol().call())
print(web3.fromWei(totalSupply, 'ether'))
 

