from wallet.core import Wallet

def test_address():
    w = Wallet()
    assert w.address.startswith('0x')
