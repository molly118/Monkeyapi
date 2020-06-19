# coding=utf-8

from Crypto.Cipher import AES
import time
import base64

key = 'iib85f0e918yuco^'.encode('utf-8')
iv = '%ialq$&thcnzhq8i'.encode('utf-8')
mode = AES.MODE_CBC
# cipher = AES.new(key, mode, iv)


def get_time_stamp():
    real_stamp = time.time()
    intreal_stamp = int(round(real_stamp * 1000))
    return str(intreal_stamp)


def padding_16():
    text = get_time_stamp()
    # text = str('123')
    if len(text.encode('utf-8')) % 16:
        padding = 16 - (len(text.encode('utf-8')) % 16)
    else:
        padding = 0
    text = text + ('\3' * padding)
    return text


def encrypt():
    text = padding_16().encode('utf-8')
    cipher = AES.new(key, mode, iv)
    cipher_text = cipher.encrypt(text)
    return base64.standard_b64encode(cipher_text).decode('utf-8')


def decrypt():
    text = encrypt()
    cipher = AES.new(key, mode, iv)
    decode_text = base64.standard_b64decode(text)
    plain_text = cipher.decrypt(decode_text)
    # print(plain_text)
    # print(bytes.decode(plain_text))
    return bytes.decode(plain_text).rstrip('\3')

print(encrypt())
print('--------------------------------')
# print(decrypt())
# print(get_time_stamp())