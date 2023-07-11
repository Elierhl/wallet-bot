from os import getenv

KEY = getenv('cryptocurrency_token')


CC_SEND_CRYPTO = f'https://new.cryptocurrencyapi.net/api/{KEY}/.send'
CC_GIVE_ADDRESS = f'https://new.cryptocurrencyapi.net/api/{KEY}/.give'

CG_GET_PRICE = 'https://api.coingecko.com/api/v3/simple/price'
