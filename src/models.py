class Courier:
    def __init__(self, login, password, first_name):
        self.login = login
        self.password = password
        self.first_name = first_name


class Order:
    def __init__(self, color=None):
        self.color = color