import json
import sys


# print([50, 100, 76, 72, 41]) #байты от (0 до 256) 
# print(bytes([50, 100, 76, 72, 41])) #b'2dLH)'
# print('bytes Байты'.encode('utf-8')) #b'bytes \xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'
# print(bytes('bytes Байты', encoding = 'utf-8'))

#length=sys.getsizeof(var) #возвращает дополнительные байты + нормальные


var = {'var0' : 0,   'var2' : 'some string', 'var1' : ['ПЭК','listitem2',5]}

varBytes = json.dumps(var).encode('utf-8') 
length = len(varBytes)

lengtOne = length // 256
lengthTwo = length % 256

if lengtOne > 256:
    print("Введенные данные превышают допустимый размер")
    exit()



data = [3, lengtOne, lengthTwo, var]
data = json.dumps(data).encode('utf-8')

print(data)


