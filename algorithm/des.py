import pyDes
import base64


# 加密
def encrypt_str(message, key):
    if len(key) > 8:
        key = key[:8]
    elif len(key) < 8:
        key = key + ''.join(['0']*(8-len(key)))
    # 加密方法
    method = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    # 执行加密码
    k = method.encrypt(message)
    # 转base64编码并返回
    return base64.b64encode(k).decode('utf-8')


# 明文和秘钥作为参数，返回密文

# 解密
def decrypt_str(code, key):
    if len(key) > 8:
        key = key[:8]
    elif len(key) < 8:
        key = key + ''.join(['0']*(8-len(key)))
    method = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    # 对base64编码解码
    k = base64.b64decode(code)
    # 再执行Des解密并返回
    return method.decrypt(k).decode('utf-8')
# 密文和秘钥作为参数，返回明文
