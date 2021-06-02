from moduls import ProtoHelper
import hashlib

# dictsLog = {"login": "Fefe333ershe", "password": "44"}
# dictsKey = {"number": 4, "keys": "Fefe, opo, uou, tot"}

# auth_requestEn = ProtoHelper.Encode("auth_request", dictsLog)
# auth_requestDec = ProtoHelper.Decode("auth_request", auth_requestEn)

# auth_responseEn = ProtoHelper.Encode("auth_response", "All right auth")
# auth_responseDec = ProtoHelper.Decode("auth_response", auth_responseEn)

# get_requestEn = ProtoHelper.Encode("get_request", dictsKey)
# get_requestDec = ProtoHelper.Decode("get_request", get_requestEn)

# get_responseEn = ProtoHelper.Encode("get_response", "All right get")
# get_responseDec = ProtoHelper.Decode("get_response", get_responseEn)

# hash_object = hashlib.md5(b'7rok7olo').hexdigest()
# print(hash_object)


# print(auth_requestDec)
# print(auth_responseDec)
# print(get_requestDec)
# print(get_responseDec)

# login = "Fedor"
# password = "07e7fcecf81bb906d86679b6f1d3c7af"

# payloadBin = ProtoHelper.BuildProtoString(login, 30) + ProtoHelper.BuildProtoString(password, 0)
# payload=0x0001.to_bytes(2, "big") + payloadBin
string = "id_str entities full_text created_at"
lst = string.split(" ")#разбиение строки на массив

print(lst)
print(lst2)
ertyuiop[]';lkjhgfdsazxcvbnm,.qwertyuiop[]';lkjhgfdsazxcvbnm

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

# [0, 1, 68, 97, 110, 105, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 101, 97, 98, 97, 101, 97, 56, 56, 51, 48, 52, 99, 52, 56, 49, 53, 55, 101, 53, 51, 99, 50, 97, 54, 102, 50, 97, 54, 101, 101, 57]
# [0, 1, 68, 97, 110, 105, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 101, 97, 98, 97, 101, 97, 56, 56, 51, 48, 52, 99, 52, 56, 49, 53, 55, 101, 53, 51, 99, 50, 97, 54, 102, 50, 97, 54, 101, 101, 57]

# {
#     "users":[
#         {
#             "login": "Fedor",
#             "password" :"dc458bcdda74ed701e95c601b7ba618d"
#         },
#         {
#             "login": "Danil",
#             "password" :"1eabaea88304c48157e53c2a6f2a6ee9"
#         },
#         {
#             "login": "Kiril",
#             "password": "07e7fcecf81bb906d86679b6f1d3c7af"
#         }
#     ]
# }




#  {'entities': "1116570031511359489{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}1116570031511359489{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}1116570031511359489{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}1116570031511359489{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 
#      'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}"} 

# {'entities': "[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}"}

# {'display_text_range': "[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]", 'entities': "[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}[0, 73]{'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'jurafsky', 'name': 'Dan Jurafsky', 'id': 14968475, 'id_str': '14968475', 'indices': [0, 9]}], 'urls': []}"} !!!!