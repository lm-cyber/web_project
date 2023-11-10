import json
from werkzeug.security import generate_password_hash, check_password_hash
import sys


class AdminDeAndSerializing:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def fromJson(json_dct):
        return AdminDeAndSerializing(json_dct["name"], json_dct["password"])

    @staticmethod
    def read():
        json_str = ""
        with open("admin_config.json", "r") as json_file:
            json_str = json_file.read()
        return AdminDeAndSerializing.fromJson(json.loads(json_str))

    def write(self):
        with open("admin_config.json", "w") as json_file:
            json_file.write(self.toJSON())

    @staticmethod
    def setUp(name: str, password: str):
        hash_pass = str(generate_password_hash(password))
        admin = AdminDeAndSerializing(name, hash_pass)
        admin.write()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("not rigth args")
        exit(1)
    AdminDeAndSerializing.setUp(sys.argv[1], sys.argv[2])
    print("setup new password and name")
