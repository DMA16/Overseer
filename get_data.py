import json


def __read_sw__(path:str)->dict:
    with open(path, "r", encoding="utf8") as sw_file:
        return sw_file.readlines()


def __read_env__(path:str)->dict:
    with open(path,"r") as conf_file:
        return json.loads(conf_file.read())



env = __read_env__("data/env.json")
tg_token = env["TG_TOKEN"]
swearings = __read_sw__("data/swearings.txt")
chat_id = env["CHAT_ID"]