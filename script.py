import os
import time
from web3 import Web3, HTTPProvider
import requests
from html.parser import HTMLParser
import pdb
import datetime

infura_key = os.environ['WEB3_INFURA_PROJECT_ID']
etherscan_api_key = os.environ["ETHERSCAN_API_KEY"]
punks_address = "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb"

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + infura_key))
punks_contract = Web3.toChecksumAddress(punks_address)
ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"punksOfferedForSale","outputs":[{"name":"isForSale","type":"bool"},{"name":"punkIndex","type":"uint256"},{"name":"seller","type":"address"},{"name":"minValue","type":"uint256"},{"name":"onlySellTo","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"enterBidForPunk","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"},{"name":"minPrice","type":"uint256"}],"name":"acceptBidForPunk","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"addresses","type":"address[]"},{"name":"indices","type":"uint256[]"}],"name":"setInitialOwners","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"withdraw","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"imageHash","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"nextPunkIndexToAssign","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"punkIndexToAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"punkBids","outputs":[{"name":"hasBid","type":"bool"},{"name":"punkIndex","type":"uint256"},{"name":"bidder","type":"address"},{"name":"value","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"allInitialOwnersAssigned","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"allPunksAssigned","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"buyPunk","outputs":[],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"punkIndex","type":"uint256"}],"name":"transferPunk","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"withdrawBidForPunk","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"punkIndex","type":"uint256"}],"name":"setInitialOwner","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"},{"name":"minSalePriceInWei","type":"uint256"},{"name":"toAddress","type":"address"}],"name":"offerPunkForSaleToAddress","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"punksRemainingToAssign","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"},{"name":"minSalePriceInWei","type":"uint256"}],"name":"offerPunkForSale","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"getPunk","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"pendingWithdrawals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"punkNoLongerForSale","outputs":[],"payable":false,"type":"function"},{"inputs":[],"payable":true,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"punkIndex","type":"uint256"}],"name":"Assign","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"punkIndex","type":"uint256"}],"name":"PunkTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"minValue","type":"uint256"},{"indexed":true,"name":"toAddress","type":"address"}],"name":"PunkOffered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":true,"name":"fromAddress","type":"address"}],"name":"PunkBidEntered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":true,"name":"fromAddress","type":"address"}],"name":"PunkBidWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":true,"name":"fromAddress","type":"address"},{"indexed":true,"name":"toAddress","type":"address"}],"name":"PunkBought","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"}],"name":"PunkNoLongerForSale","type":"event"}]'
contract = w3.eth.contract(punks_contract, abi=ABI)
years_dormant = 1


alchemy_query = "https://eth-mainnet.g.alchemy.com/nft/v2/demo/getOwnersForCollection/?contractAddress="
alchemy_query += punks_address
addresses = requests.get(alchemy_query).json()['ownerAddresses']


inactive = []

def _more_than_n_years_ago(timestamp):
  time_between = datetime.datetime.now() - datetime.datetime.fromtimestamp(int(timestamp))
  return time_between.days > (years_dormant * 365)

def _get_internal_txns(addy):
  etherscan =  "https://api.etherscan.io/api?module=account&action=tokentx&page=1&offset=100&startblock=0&endblock=99999999&sort=desc"
  etherscan += "&contractaddress=" + punks_address
  etherscan += "&apikey=" + etherscan_api_key
  etherscan += "&address=" + addy
  response = requests.get(etherscan)
  return response.json()['result'][0]

def _interal_txn_more_than_n_years_ago(addy):
  txn = _get_internal_txns(addy)
  return _more_than_n_years_ago(txn['timeStamp'])



for i, addy in enumerate(addresses):
  try:
    etherscan  = "https://api.etherscan.io/api?module=account&action=txlist&startblock=0&endblock=99999999&page=1&offset=10&sort=desc"
    etherscan += "&apikey=" + etherscan_api_key
    addy = Web3.toChecksumAddress(addy)
    etherscan += f'&address={addy}'
    resp = requests.get(etherscan)
    txns = resp.json()['result']
     
    # check for related addresses and internal transactions (e.g. transferPunk)
    if _more_than_n_years_ago(txns[0]['timeStamp']):
      inactive.append(addy)
      print('longer than {} years for {}'.format(years_dormant, addy))

  except:
    # Check for internal transactions
    try:
      if len(resp.json()['result']) == 0:
        more_than_n_years = _interal_txn_more_than_n_years_ago(addy)
        if more_than_n_years:
          inactive.append(addy)
    except ValueError:
      print('error for ' + etherscan)
      print(i)
        


total_punks_lost = 0


for i, addy in enumerate(inactive):
  punks_held = contract.functions.balanceOf(addy).call()
  total_punks_lost += punks_held
  print(f'{addy} holds {punks_held}')

print(total_punks_lost)


   
