import base64

from Crypto.Cipher import AES


def add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)  # 返回bytes


# 补长度
def Aes_encrypt_str(message, key):
    method = AES.new(add_to_16(key), AES.MODE_ECB)
    k = str(base64.encodebytes(method.encrypt(add_to_16(message))), encoding='utf8').replace('\n', '')
    return k


# 参数为明文和秘钥，返回密文
def Aes_decrypt_str(code, key):
    method = AES.new(add_to_16(key), AES.MODE_ECB)
    m = str(method.decrypt(base64.decodebytes(bytes(code, encoding='utf8'))).rstrip(b'\0').decode("utf8"))
    return m
# 参数为密文和秘钥，返回明文

# Encrypt=Aes_encrypt_str("123456789","123456")
# print(Encrypt)
# Decrypt = Aes_decrypt_str(Encrypt,"123456")
# print(Decrypt)
