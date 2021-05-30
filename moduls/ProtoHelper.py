import random
# packetTypeEncoders = {
#     'auth_request': lambda x: x**2, #запрос авторизации #нечётные клиента и чётные от сервера
#     'auth_response':'', #ответ авторизации
#     'get_request':'', #запрос на чтение данных
#     'get_response':'', #ответ на чтение данных
# }


packetTypes = {
    "auth_request": 0x0001, #запрос авторизации #нечётные клиента и чётные от сервера
    "auth_response":0x8001, #ответ авторизации
    "get_request": 0x0002, #запрос на чтение данных
    "get_response": 0x2001, #ответ на чтение данных
}



def BuildProtoString(in_str, out_len): 
        out_str = bytearray(out_len)
        in_str = bytearray(str(in_str), encoding = "utf-8")
        out_str[0:len(in_str)] = in_str
        return out_str


def Decode(packetType, payloadBin):

    payload=''
    if packetType == "auth_request":

        idiDecimal = int.from_bytes(payloadBin[0:2],"big")
        idi = hex(idiDecimal)

        payload = payloadBin.decode("utf-8")
        login = payload[2:30].replace("\x00", "")
        password = payload[32:60].replace("\x00", "")


        payload = {"idi":idi, "login": login, "password": password}

    if packetType == "auth_response":

        idiDecimal = int.from_bytes(payloadBin[0:2],"big")
        idi = hex(idiDecimal)
        rand = payloadBin[2:30].decode("utf-8")
        rand = rand.replace("\x00", "")
        response = payloadBin[32:60].decode("utf-8")
        response = response.replace("\x00", "")

        payload={"idi":idi, "rand": rand, "response": response}

    if packetType=="get_request":
        
        idiDecimal = int.from_bytes(payloadBin[0:2],"big")
        idi = hex(idiDecimal)

        number = payloadBin[2:30].decode("utf-8")
        number = number.replace("\x00", "")
        key = payloadBin[32:60].decode("utf-8")
        key = key.replace("\x00", "")

        payload={"idi":idi, "number": number, "key": key}

    if packetType=="get_response":
        idiDecimal = int.from_bytes(payloadBin[0:2],"big")
        idi = hex(idiDecimal)
        rand = payloadBin[2:30].decode("utf-8")
        rand = rand.replace("\x00", "")
        response = payloadBin[32:60].decode("utf-8")
        response = response.replace("\x00", "")

        payload={"idi":idi, "rand": rand, "response": response}


    return payload


#2байта-айди пакета, 30 байт логин, 30 байт пароль
# исли мы знаем как строка кончается то мы терминируем
def Encode(packetType, payload):
    payloadBin = b''
    if packetType == "auth_request":
        login = payload["login"]
        password = payload["password"]
        payloadBin = BuildProtoString(login, 30) + BuildProtoString(password, 31)
    
    if packetType == "auth_response":
        rand=random.random()
        payloadBin = BuildProtoString(rand, 30) + BuildProtoString(payload, 31)

    if packetType=="get_request":
        # number = bytearray (payload[0], encoding = "utf-8")
        # key = bytearray (payload[1], encoding = "utf-8")
        # var = b"\x0002" + number + key
        number = payload["number"]
        key = payload["key"]
        payloadBin = BuildProtoString(number, 30) + BuildProtoString(key, 31)

    if packetType=="get_response":
        rand=random.random()
        # var = bytearray (str(rand), encoding = "utf-8")+bytearray (payload, encoding = "utf-8")
        payloadBin = BuildProtoString(rand, 30) + BuildProtoString(payload, 31)


    return packetTypes[packetType].to_bytes(2, "big") + payloadBin
    
