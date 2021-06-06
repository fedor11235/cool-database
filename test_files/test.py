from moduls import Base


data = ''

db = Base.load('bd/users.json', False) #загрузить базу данных из файла 

allUsers=db.dgetall("users")


allUsers.pop(0)


# db.set(1, {"login": "Fedor", "password": "dc458bcdda74ed701e95c601b7ba618d"}) #Задать значение ключу

db.dump()
# db.get('id_str')  #получить значение по индексу
# db.append("id", "ytyt") #Добавить больше к значению ключа
# db.rem("id") #Удалить значение по индексу
# db.getall('id_str') #вернуть список всех ключей в бд

# db.deldb() #Удалить всё из базы данных
# db.dump() #сохранить базу данных из памяти в файл указанных в load

# работа со списками
#db.lcreate("PYT") #создать список и добавить в конец бд
#db.ladd("PYT", "dcssdc,  sdsd, dsdw") #добавляет значение в список
#db.lgetall("PYT") #вернуть все значения из списка
#db.lextend("PYT", "wvd vwwvvw") #расширить список последовательностью
#db.lget("PYT", 3) #вернуть значение из списка по идексу
# db.lrem("PYT") #Удалить список
# db.lpop("PYT", 3) #Удалить одно значение по индексу из списка
# db.llen("PYT") #Узнать значение списка
# db.lappend("PYT", 2, "32324244324325323242") #добавить значение к элементу по индексу из списка
# db.lcreate("PYT") #создать список и добавить в конец бд
# db.ladd("PYT", "dcssdc,  sdsd, dsdw") #добавляет значение в список
# db.lgetall("PYT") #вернуть все значения из списка
# db.lextend("PYT", "wvd vwwvvw") #расширить список последовательностью
# db.lget("PYT", 3) #вернуть значение из списка по идексу
# db.lrem("PYT") #Удалить список
# db.lpop("PYT", 3) #Удалить одно значение по индексу из списка
# db.llen("PYT") #Узнать значение списка


# работа со словарями
# db.dcreate("PYT") #создать список и добавить в конец бд
# db.dadd("PYT", ("key2",  "value2")) #добавляет значение в список
# db.dgetall("PYT") #вернуть все значения из словаря
# data = db.dget("PYT","key2") #вернуть значение по ключу
# data = db.dkeys("PYT") #вернуть все ключи из словаря
# data = db.dvals("PYT") #вернуть все значения из словаря
# data = db.dexists("PYT", "key") #определить существует ли ключь
# db.drem("PYT") #Удалить словарь со всеми данными
# db.dpop("PYT", "key2") #Удалить одно значение по ключу

print(data)











# {
#     "users":[
#         {
#             "login": "Fedor",
#             "password" :"pass11235"
#         },
#         {
#             "login": "Danil",
#             "password" :"vargi"
#         },
#         {
#             "login": "Kiril",
#             "password": "7rok7olo"
#         }
#     ]
# }

#{"users": [{"login": "Danil", "password": "1eabaea88304c48157e53c2a6f2a6ee9"}, {"login": "Kiril", "password": "07e7fcecf81bb906d86679b6f1d3c7af"}, {"login": "Rudi", "password": "dc458bcdda74ed701e95c601b7ba618d"}]}


