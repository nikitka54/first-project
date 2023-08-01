import secrets

class Wallet:
    def __init__(self):
        self.address = '0x' + secrets.token_hex(20)

    def method_0(self): return 0

    def method_1(self): return 1

    def method_2(self): return 2
