import pytest
from bank_account import BankAccount


# Fixture: Create an account with Rs 1000
@pytest.fixture
def account():
    return BankAccount("Ali", 1000)


# Test deposit
def test_deposit(account):
    account.deposit(500)

    assert account.balance == 1500


# Test withdrawal
def test_withdraw(account):
    account.withdraw(300)

    assert account.balance == 700


# Test transaction history
def test_transaction_history(account):
    account.deposit(500)
    account.withdraw(200)

    assert account.transaction_history == [
        "Deposited: 500",
        "Withdrawn: 200"
    ]


# Test invalid deposit
def test_invalid_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-100)


# Test insufficient balance
def test_insufficient_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(1500)


# Test invalid withdrawal
def test_invalid_withdrawal(account):
    with pytest.raises(ValueError):
        account.withdraw(0)