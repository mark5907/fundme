from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3


DECIMAL = 8
START_PRICE = 20000000000
LOCAL_DEV_ENVS = ["development", "ganache-local"]
FORK_DEV_ENVS = ["mainnet-fork-dev", "mainnet-fork"]


def get_account():
    if network.show_active() in LOCAL_DEV_ENVS + FORK_DEV_ENVS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMAL, Web3.toWei(START_PRICE, "ether"), {"from": get_account()}
        )
    print("Deployed Mocks")
