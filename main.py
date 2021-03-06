import algorithm.rsa as rsa
import algorithm.md5 as md5
import hug
import algorithm.des as des
# import algorithm.aes as aes


@hug.post()
def rsa_encrypt_numbers(data: hug.types.number,
                        p: hug.types.number = None,
                        q: hug.types.number = None):
    if p is None and q is None:
        p = 106697219132480173106064317148705638676529121742557567770857687729397446898790451577487723991083173010242416863238099716044775658681981821407922722052778958942891831033512463262741053961681512908218003840408526915629689432111480588966800949428079015682624591636010678691927285321708935076221951173426894836169
        q = 144819424465842307806353672547344125290716753535239658417883828941232509622838692761917211806963011168822281666033695157426515864265527046213326145174398018859056439431422867957079149967592078894410082695714160599647180947207504108618794637872261572262805565517756922288320779308895819726074229154002310375209
        private_key, public_key = rsa.generate_key(p, q)
    elif p is not None and q is not None:
        private_key, public_key = rsa.generate_key(p, q)
    else:
        # f**k U
        pass
    hashed_numbers = private_key.encrypt(data)
    return str(hashed_numbers)


@hug.post()
def rsa_decrypt_numbers(data: hug.types.number,
                        p: hug.types.number = None,
                        q: hug.types.number = None):
    if p is None and q is None:
        p = 106697219132480173106064317148705638676529121742557567770857687729397446898790451577487723991083173010242416863238099716044775658681981821407922722052778958942891831033512463262741053961681512908218003840408526915629689432111480588966800949428079015682624591636010678691927285321708935076221951173426894836169
        q = 144819424465842307806353672547344125290716753535239658417883828941232509622838692761917211806963011168822281666033695157426515864265527046213326145174398018859056439431422867957079149967592078894410082695714160599647180947207504108618794637872261572262805565517756922288320779308895819726074229154002310375209
        private_key, public_key = rsa.generate_key(p, q)
    elif p is not None and q is not None:
        private_key, public_key = rsa.generate_key(p, q)
    else:
        # f**k U
        pass
    de_data = public_key.decrypt(data)
    return str(de_data)


@hug.post()
def md5_text(data: hug.types.text):
    de_data = md5.get_md5(data)
    return str(de_data)


@hug.post()
def des_encrypt_text(data: hug.types.text, key: hug.types.text):
    de_data = des.encrypt_str(data, key)
    return str(de_data)


@hug.post()
def des_decrypt_text(data: hug.types.text, key: hug.types.text):
    de_data = des.decrypt_str(data, key)
    return str(de_data)

#
# @hug.post()
# def aes_encrypt_text(data: hug.types.text, key: hug.types.text):
#     de_data = aes.Aes_encrypt_str(data, key)
#     return str(de_data)
#
#
# @hug.post()
# def aes_decrypt_text(data: hug.types.text, key: hug.types.text):
#     de_data = aes.Aes_decrypt_str(data, key)
#     return str(de_data)
