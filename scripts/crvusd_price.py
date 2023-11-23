from ape import Contract


def main():
    crv_usd_price_oracle = Contract("0xe5Afcf332a5457E8FafCD668BcE3dF953762Dfe7")
    crv_usd_price = crv_usd_price_oracle.price() / 10 ** 18
    print(f"Current price: {crv_usd_price}")
