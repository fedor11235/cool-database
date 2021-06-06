#с клиента
def funcData():
    var = {"var0 ": 0, "var2" : "some string," "var1" : ["listiteпэк", "listitem2",5]}
    
    varBytes = json.dumps(var).encode("utf-8")
    checksum=CRC16.Crc16(varBytes)

    length = len(varBytes)

    lengtOne = length // 256
    lengthTwo = length % 256

    

    if lengtOne > 256:
        print("Введенные данные превышают допустимый размер")
        exit()

    authPayloadDict = {"login":"Fefe333ershe", "password":"44"}
    # data = [3, lengtOne, lengthTwo, var]
    data = ProtoHelper.Encode("auth_request", authPayloadDict)


    #data = json.dumps(data).encode('utf-8')

    # checksum = 0
    # for ch in data:
    #     checksum += ch
    print("контрольная сумма: ", checksum)

    #data = [checksum/2, 3, lengtOne, lengthTwo, var, checksum/2]
    #data = json.dumps(data).encode('utf-8')

    return (data)


#с сервера
def funcData(data):
    print("\nЧто пришло: ", data)
    data = json.loads(data)

    clientCheksum=data[0]+data[5]

    print("\nПришедшая контрольная сумма: ", clientCheksum)

    dataBytes = json.dumps(data).encode("utf-8")
    checksum = 0
    for ch in dataBytes:
        checksum += ch
    print("\nВычесленная контрольная сумма: ", checksum)

    if (clientCheksum!=checksum):
        print("\nКонтрольные суммы не совпадают")
        mess = "Ошибка в пакете".encode('utf-8')
        return(mess)

    print("\nВыделили нужную инфу: ", data[3])

    mess = "Мы получили ваше сообщение!!!".encode("utf-8")

    return mess