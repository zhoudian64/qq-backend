import hashlib
def get_md5(m):
    h = hashlib.md5()
    h.update(m.encode('utf-8'))
    return h.hexdigest()
#字符串作为参数，返回md5值