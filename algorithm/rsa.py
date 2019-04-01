from .gcd import ext_gcd
from .montgomery import exp_mode

big_prime = 3889


class RSAKey:
    """
    密钥格式
    """

    def __init__(self, n, component):
        self.component = component
        self.n = n


class RSAPublicKey(RSAKey):
    def encrypt(self, data):
        return exp_mode(data, self.component, self.n)


class RSAPrivateKey(RSAKey):
    def decrypt(self, data):
        return exp_mode(data, self.component, self.n)


def generate_key(prime_1, prime_2):
    """
    生成rsa密钥对
    """
    big_int = prime_1 * prime_2
    # 公开的 难以分解
    phi = (prime_1 - 1) * (prime_2 - 1)
    # 因难以分解而 难以获得
    # 互质整数的欧拉函数
    _, private_key, _ = ext_gcd(big_prime, phi)
    # 因phi难以获得 而难以获得
    return RSAPublicKey(big_int, big_prime), RSAPrivateKey(big_int, private_key)
