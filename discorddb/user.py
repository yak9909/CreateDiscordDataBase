import os
import json
from modules import tools


class User:
    def __init__(self, user_id, server_id=None):
        self.id = user_id
        self.server_id = server_id

        if self.server_id is None:
            self.user_default_path = "data/global_user_default.json"
            self.file_path = f"data/users/{self.id}.json"
        else:
            self.user_default_path = "data/servers/user_default.json"
            self.file_path = f"{self.server_id}/users/{self.id}.json"

        self.data = self.register()

    def create(self):
        user_default = json.load(tools.read_file(self.user_default_path))
        f = tools.read_file(self.file_path, True)
        json.dump(user_default, f, ensure_ascii=False, indent=2)
        f.close()
        return user_default

    def register(self):
        if os.path.exists(self.file_path):
            user_file = json.load(tools.read_file(self.file_path))
        else:
            user_file = self.create()

        return user_file

    def update(self):
        f = tools.read_file(self.file_path, True)
        json.dump(self.data, f, ensure_ascii=False, indent=2)

    def reload(self):
        self.data = self.register()
