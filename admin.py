from admin_setup import AdminDeAndSerializing


class Admin_:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    @staticmethod
    def read():
        admin_deserialize = AdminDeAndSerializing.read()
        return Admin_(admin_deserialize.name, admin_deserialize.password)
