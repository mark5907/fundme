from scripts.helper_scripts import get_account, LOCAL_DEV_ENVS
from scripts.deploy import deploy_fund_me
import pytest
from brownie import network


def test_price():
    account = get_account()
    fund_me = deploy_fund_me()

    px = fund_me.getEntranceFee()
    print(f"===> price = {px}")


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_DEV_ENVS:
        pytest.skip("only for local testing")
