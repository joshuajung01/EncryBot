import os
import math
import string
import math
import random


def encrypter(message):
    key = random.randint(1, 3)
    if key == 1:
        return Encryption_Type_1(message), 1

    elif key == 2:
        return Encryption_Type_2(message), 2

    elif key == 3:
        return Encryption_Type_3(message), 3


def Encryption_Type_1(message):
    messagearr = []
    returnstr = ""
    for i in range(len(message)):
        messagearr.append(message[i])
        messagearr[i] = chr(ord(messagearr[i]) * 3)
    returnstr = returnstr.join(messagearr)
    return returnstr


def Encryption_Type_2(message):
    messagearr = []
    returnstr = ""
    for i in range(len(message)):
        messagearr.append(message[i])
        messagearr[i] = chr((ord(messagearr[i]) + 3) * 2)
    returnstr = returnstr.join(messagearr)
    return returnstr


def Encryption_Type_3(message):
    messagearr = []
    returnstr = ""
    for i in range(len(message)):
        messagearr.append(message[i])
        messagearr[i] = chr(ord(messagearr[i]) * 4 - 63)
    returnstr = returnstr.join(messagearr)
    return returnstr


def decrypter(message, key):
    if key == 1:
        return Decrypt_1(message)
    elif key == 2:
        return Decrypt_2(message)
    elif key == 3:
        return Decrypt_3(message)


def Decrypt_1(encrypted_message):
    encryp_mess_arr = []
    decrypted = ""
    for i in range(len(encrypted_message)):
        encryp_mess_arr.append(encrypted_message[i])
        encryp_mess_arr[i] = chr(int(ord(encryp_mess_arr[i]) / 3))
    decrypted = decrypted.join(encryp_mess_arr)
    return decrypted


def Decrypt_2(encrypted_message):
    encryp_mess_arr = []
    decrypted = ""
    for i in range(len(encrypted_message)):
        encryp_mess_arr.append(encrypted_message[i])
        encryp_mess_arr[i] = chr(int(ord(encryp_mess_arr[i]) / 2 - 3))
    decrypted = decrypted.join(encryp_mess_arr)
    return decrypted


def Decrypt_3(encrypted_message):
    encryp_mess_arr = []
    decrypted = ""
    for i in range(len(encrypted_message)):
        encryp_mess_arr.append(encrypted_message[i])
        encryp_mess_arr[i] = chr(int((ord(encryp_mess_arr[i]) + 63) / 4))
    decrypted = decrypted.join(encryp_mess_arr)
    return decrypted
