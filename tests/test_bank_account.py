import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)

@pytest.fixture
def target_account():
    return BankAccount(100)

def test_initial_balance():
    account = BankAccount(100)
    assert account.balance == 100
    with pytest.raises(ValueError):
        account = BankAccount(-50)

def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150
    with pytest.raises(ValueError):
        start_account.deposit(-1)

def test_withdraw(start_account):
    start_account.withdraw(50)
    assert start_account.balance == 50
    with pytest.raises(ValueError):
        start_account.withdraw(0)
    with pytest.raises(ValueError):
        start_account.withdraw(-10)
    with pytest.raises(ValueError):
        start_account.withdraw(1000)

def test_transfer(start_account, target_account):
    start_account.transfer_to(target_account, 50)
    assert start_account.balance == 50
    assert target_account.balance == 150
    with pytest.raises(ValueError):
        start_account.transfer_to("not an account", 10)
    with pytest.raises(ValueError):
        start_account.transfer_to(target_account, 1000)
    with pytest.raises(ValueError):
        start_account.transfer_to(target_account, -1)
    with pytest.raises(ValueError):
        start_account.transfer_to(target_account, 0)