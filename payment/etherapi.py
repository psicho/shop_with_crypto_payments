# API отслеживания платежей

import requests
import json


def request_payment_complete(order):
    api_key = '9b25106fb5-0421714b82-186e418bbf-2862dc57b6'
    wallet_address = order.ethereum_wallet
    order_id = order.id
    amount = order.get_total_cost()

    full_request = (f"https://etherapi.net/api/v2/.track?key="
                    f"{api_key}&address="
                    f"{wallet_address}&amount="
                    f"{amount}&tag="
                    f"{order_id}"
                    )

    response = requests.get(full_request)

    return json.loads(response.content.decode("utf-8"))['result']


def request_account_balance():
    api_key = '9b25106fb5-0421714b82-186e418bbf-2862dc57b6'

    full_request = f"https://etherapi.net/api/v2/.balance?key={api_key}"

    response = requests.get(full_request)

    return json.loads(response.content.decode("utf-8"))['result']
