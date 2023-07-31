import secrets

class Wallet:
    def __init__(self):
        self.address = '0x' + secrets.token_hex(20)

    def method_0(self): return 0
