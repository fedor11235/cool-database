from moduls import ProtoHelper

dictsLog = {"login": "Fefe333ershe", "password": "44"}
dictsKey = {"number": 4, "key": "Fefe, opo, uou, tot"}

auth_requestEn = ProtoHelper.Encode("auth_request", dictsLog)
auth_requestDec = ProtoHelper.Decode("auth_request", auth_requestEn)

auth_responseEn = ProtoHelper.Encode("auth_response", "All right auth")
auth_responseDec = ProtoHelper.Decode("auth_response", auth_responseEn)

get_requestEn = ProtoHelper.Encode("get_request", dictsKey)
get_requestDec = ProtoHelper.Decode("get_request", get_requestEn)

get_responseEn = ProtoHelper.Encode("get_response", "All right get")
get_responseDec = ProtoHelper.Decode("get_response", get_responseEn)


print(auth_requestDec)
print(auth_responseDec)
print(get_requestDec)
print(get_responseDec)

