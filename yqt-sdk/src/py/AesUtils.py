# -*- coding=utf-8-*-
# Autrhor: YQT by pengfei.he
from Crypto.Cipher import AES
import os
from Crypto import Random
import base64
from binascii import b2a_hex, a2b_hex


"""
银企通 aes加密算法
padding : PKCS5
"""

class AESUtil:

    __BLOCK_SIZE_16 = BLOCK_SIZE_16 = AES.block_size

    @staticmethod
    def encryt(str, key):
        cipher = AES.new(key, AES.MODE_ECB)
        x = AESUtil.__BLOCK_SIZE_16 - (len(str) % AESUtil.__BLOCK_SIZE_16)
        if x != 0:
            str = str + chr(x)*x
        msg = cipher.encrypt(str)
        # msg = base64.urlsafe_b64encode(msg).replace('=', '')
        msg = b2a_hex(msg)
        return msg

    @staticmethod
    def decrypt(enStr, key):
        cipher = AES.new(key, AES.MODE_ECB)
        enStr += (len(enStr) % 4)*"="
        # decryptByts = base64.urlsafe_b64decode(enStr)
        decryptByts = a2b_hex(enStr)

        msg = cipher.decrypt(decryptByts)
        paddingLen = ord(msg[len(msg)-1])
        return msg[0:-paddingLen]

