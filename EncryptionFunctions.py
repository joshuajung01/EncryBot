import os
import math
import string


def Encryption_Type_1(message):
    messagearr = []
    returnstr = ""
    for i in range(len(message)):
        messagearr.append(message[i])
        messagearr[i] = chr(ord(messagearr[i]) * 3)
    returnstr = returnstr.join(messagearr)
    return returnstr


def Decrypt_1(encrypted_message):
    encryp_mess_arr = []
    decrypted = ""
    for i in range(len(encrypted_message)):
        encryp_mess_arr.append(encrypted_message[i])
        encryp_mess_arr[i] = chr(int(ord(encryp_mess_arr[i]) / 3))
    decrypted = decrypted.join(encryp_mess_arr)
    return decrypted
