from statemachine import StateMachine, State

class ClientSession(StateMachine):
    offline = State('offline', initial=True)
    login_wait = State('login_wait')
    online = State('online')

    login = offline.to(login_wait)
    logout = online.to(offline)

    def __init__(self, transport):
        self.transport = transport
        transport.session = self

    def handle_packet(self, payload):
        if self.is_login_wait:
            self.idSessions = payload["idSessions"]
            self.login_wait.to(self.online)
            return 'send',  {"packet_type": "get_value", "idSessions": self.idSessions, "keys": "id"}
        if self.is_online:
            print ("\nОтвет от сервера:", payload)


    def do_login(self):
        password = hashlib.md5(b"pass11235").hexdigest() 
        authPacket = {"packet_type": "auth_request", "login": "Fedor", "password": password}
        self.transport.send_packet(authPacket)
        self.offline.to(self.login_wait)

    def on_logout(self):
        print('do logout')

















# SESSION_OFFLINE = 0
# SESSION_ONLINE = 1

# class ClientSession(object):
#     def __init__(self):
#         self.sessionStatus = SESSION_OFFLINE

