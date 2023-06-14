import pytest
from app.calcs import add, BankAccount, InsufficientFunds

@pytest.fixture
def zero_account():
    return BankAccount()

@pytest.fixture
def fifty_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [(2,4,6), (1,3,4), (-1,2,1), (-10,10,0)])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected

def test_new_set_init_amount(fifty_account):
    assert fifty_account.balance == 50

def test_new_default_amount(zero_account):
    assert zero_account.balance == 0

def test_deposit(zero_account):
    zero_account.deposit(50)
    assert zero_account.balance == 50

def test_withdraw():
    bank_account = BankAccount(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50

def test_interest():
    bank_account = BankAccount(100)
    bank_account.collect_interest()
    assert bank_account.balance == 100 * 1.1

@pytest.mark.parametrize("deposited, withdrew, expected",
                         [(200,100,100), (50,10,40), (50,25,25), (1200,1000,200)]
                         )
def test_bank_transact(zero_account, deposited, withdrew, expected):
    zero_account.deposit(deposited)
    zero_account.withdraw(withdrew)
    assert zero_account.balance == expected

def test_overdraw(zero_account):
    with pytest.raises(InsufficientFunds):
        zero_account.withdraw(100)