import ProtoHelper

dictsLog = ["Fefe333ershe", "44"]
dictsKey = [4, "Fefe, opo, uou, tot"]

auth_requestEn = ProtoHelper.Encode("auth_request", dictsLog)
auth_requestDec = ProtoHelper.Decode("auth_request", auth_requestEn)

auth_responseEn = ProtoHelper.Encode("auth_response", dictsLog)


print(auth_requestEn)
print(auth_requestDec)

print(auth_responseEn)