from modules import ProtoHelper

class TransportController():
    def __init__(self, sock):
        self.sock = sock
        self.session = None
        self.tail = None

    def send_packet(self, packet):
        dataTx = ProtoHelper.build_transport_frame(packet["packet_type"], packet)
        self.sock.send(dataTx)

    def on_recv(self, dataRx):
        rx_tail, packet, rx_rest = ProtoHelper.parse_transport_frame(self.tail+dataRx)
        self.tail = rx_tail
        reply_action, reply_packet = self.session.handle_packet(packet)

        if reply_action == 'send':
            dataTx = ProtoHelper.build_transport_frame(reply_packet["packet_type"], reply_packet)
            self.sock.send(dataTx)

        if reply_action == 'pass':
            pass


    # def handle_packet(self, payload):
    #     if self.is_login_wait:
    #         self.idSessions = payload["idSessions"]
    #         self.login_rsp()
    #     if self.is_online:
    #         getPayloadDict = {"idSessions": self.idSessions, "keys": "id"}
    #         dataGet = build_data("get_request", getPayloadDict)
    #         self.sock.send(dataGet)


    # def on_login(self):
    #     password = hashlib.md5(b"pass11235").hexdigest() 
    #     authPayloadDict = {"login":"Fedor", "password": password} 
    #     dataAuth = build_data("auth_request", authPayloadDict)
    #     self.sock.send(dataAuth)

    # def on_logout(self):
    #     print('do logout')