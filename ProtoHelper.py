import random
# packetTypeEncoders = {
#     'auth_request': lambda x: x**2, #запрос авторизации #нечётные клиента и чётные от сервера
#     'auth_response':'', #ответ авторизации
#     'get_request':'', #запрос на чтение данных
#     'get_response':'', #ответ на чтение данных
# }


# маскировать, задаёт старший байт
packetTypes = {
    'auth_request': 0x0001, #запрос авторизации #нечётные клиента и чётные от сервера
    'auth_response':0x8001, #ответ авторизации
    'get_request': 0x0002, #запрос на чтение данных
    'get_response': 0x2001, #ответ на чтение данных
}



def build_proto_string(in_str, out_len): 
        out_str = bytearray(out_len)
        in_str = bytearray(in_str, encoding = 'utf-8')
        out_str[0:len(in_str)] = in_str
        return out_str


def Decode(packetType, payload):


    if packetType == 'auth_request':
        pass
    
    login = payload[3:30]
    password = payload[33:-1]
    idi = payload[0:3]

    print(login, "login")
    print(password, "password")
    print(idi, "idi")
    
    var = [idi, login, password]
    return var


#2байта-айди пакета, 30 байт логин, 30 байт пароль
# исли мы знаем как строка кончается то мы терминируем
def Encode(packetType, payload):
    payloadBin = b''
    if packetType == 'auth_request':
        login = payload['login']
        password = payload['password']
        payloadBin = build_proto_string(login, 30) + build_proto_string(password, 31)
    
    if packetType == 'auth_response':
        rand=random.random()
        var = bytearray (str(rand), encoding = 'utf-8')+bytearray (payload, encoding = 'utf-8')
        return var

    if packetType=='get_request':
        number = bytearray (payload[0], encoding = 'utf-8')
        key = bytearray (payload[1], encoding = 'utf-8')

        var = b'\x0002' + number + key
        return var

    if packetType=='get_response':
        rand=random.random()
        var = bytearray (str(rand), encoding = 'utf-8')+bytearray (payload, encoding = 'utf-8')
        return var

    return packetTypes[packetType].to_bytes(2, 'big') + payloadBin
    
