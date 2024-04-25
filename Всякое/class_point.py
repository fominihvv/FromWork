class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    __server_count = 0

    def __init__(self):
        self.buffer = []
        Server.__server_count += 1
        self.ip = Server.__server_count
        self.router = None

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
                (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);"""
        self.router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
                и очищает входной буфер;"""
        result = self.buffer.copy()
        self.buffer.clear()
        return result

    def get_ip(self):
        """возвращает свой IP-адрес."""
        return self.ip


class Router:

    def __init__(self):
        self.buffer = []
        self.server = {}

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый
        сервер соединен только с одним роутером);"""
        self.server[server.get_ip()] = server
        server.router = self

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера;"""
        if server.get_ip() in self.server:
            del self.server[server.get_ip()]
            server.router = None

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
        (после отправки буфер должен очищаться)."""
        while self.buffer:
            msg = self.buffer.pop()
            if msg.ip in self.server:
                self.server[msg.ip].buffer.append(msg)
