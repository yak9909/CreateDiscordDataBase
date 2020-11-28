import json
import os


def load_config() -> dict:
    file_path = "config.json"
    if os.path.exists("dev_config.json"):
        file_path = "dev_config.json"

    config_file = open(file_path, mode="r+", encoding="utf-8")
    return json.load(config_file)


def read_file(file_path, write=False):
    mode = "r+"
    if write:
        mode = "w+"

    file = open(file_path, mode=mode, encoding="utf-8")
    return file


def add_line(file_path, txt):
    file = open(file_path, mode="a", encoding="utf-8")
    file.write(txt)
    file.close()
