import os
import json
from discorddb import tools, initialize


class Server:
    def __init__(self, guild_id, root="../"):
        self.root = root
        self.id = guild_id
        if self.id == 0:
            return

        initialize.init(self.root)

        self.dir_path = f"data/servers/{self.id}"

        self.logs_dir_path = f"{self.dir_path}/logs"
        self.users_dir_path = f"{self.dir_path}/users"
        self.data_path = f"{self.dir_path}/data.json"
        self.server_default_path = "data/servers/server-default.json"

        self.data = self.register()

    def create_server_dir(self):
        os.mkdir(self.dir_path)
        os.mkdir(self.logs_dir_path)
        os.mkdir(self.users_dir_path)
        server_default = json.load(tools.read_file(self.server_default_path))
        f = tools.read_file(self.data_path, True)
        json.dump(server_default, f, ensure_ascii=False, indent=2)
        f.close()
        return server_default

    def register(self):
        if os.path.exists(self.dir_path):
            server_data = json.load(tools.read_file(self.data_path))
        else:
            server_data = self.create_server_dir()
        return server_data
    
    def update_channel(self, channel):
        for channel_logs in os.listdir(f"{self.logs_dir_path}"):
            channel_id = channel_logs.split(".")[0]
            if channel_id == str(channel.id):
                return True

        os.mkdir(f"{self.logs_dir_path}/{channel.id}")
        return False
    
    async def create_log(self, messages: list):
        for message in messages:
            self.update_channel(message.channel)
            if not os.path.exists(f"{self.logs_dir_path}/{message.channel.id}/files"):
                os.mkdir(f"{self.logs_dir_path}/{message.channel.id}/files")
            for i, v in enumerate(message.attachments):
                os.mkdir(f"{self.logs_dir_path}/{message.channel.id}/files/{message.id}")
                file_extension = v.filename.split('.')[-1]
                
                f = open(
                    f"{self.logs_dir_path}/{message.channel.id}/"
                    f"files/{message.id}/{i}.{message.id}.{file_extension}",
                    mode="wb+"
                )
                await v.save(f)
            
            message_file = f"{self.logs_dir_path}/{message.channel.id}/{message.id}.txt"
            log_file = f"{self.logs_dir_path}/{message.channel.id}.txt"

            if message.content:
                tools.add_line(message_file, f"{message.author} | {message.author.id}\n{message.content}")
                tools.add_line(log_file, f"({message.channel.name}){message.author}: {message.content}\n\n")
            else:
                tools.add_line(message_file, f"{message.author} | {message.author.id}\n(File)")
                tools.add_line(log_file, f"({message.channel.name}){message.author}: (File)\n\n")

    def update(self):
        f = tools.read_file(self.data_path, True)
        json.dump(self.data, f, ensure_ascii=False, indent=2)

    def reload(self):
        self.data = self.register()
