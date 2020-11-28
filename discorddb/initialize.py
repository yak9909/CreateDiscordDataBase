import os
import json


def write(obj, fp):
    f = open(fp, mode="w+", encoding="utf-8")
    json.dump(obj, f, ensure_ascii=False, indent=2)
    f.close()


def init(root):
    if not os.path.exists(f"{root}data"):
        os.mkdir(f"{root}data")
        os.mkdir(f"{root}data/servers")
    global_user_default = {"this": "global-user"}
    user_default = {"this": "local-user"}
    server_default = {"this": "server"}
    write(global_user_default, f"{root}data/user-default.json")
    write(user_default, f"{root}data/servers/user-default.json")
    write(server_default, f"{root}data/servers/server-default.json")
