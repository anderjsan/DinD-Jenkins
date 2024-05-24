import os
import json

class FileManager():
    def __init__(self, project):
        self.project = project
        self.path = f".version/.{project}"
        self.log_path = f".version/log/.{project}_log"
        
    def read_last_version(self, project):
        try:
            with open(f".version/.{project}", "r") as f:
                if not f.read():
                    return "0.0.0"
                f.seek(0)
                return f.readline().strip()
        except FileNotFoundError:
            with open(f".version/.{project}", "w") as f:
                f.write("0.0.0")
            return "0.0.0"
        except Exception as e:
            print(f"Error in read_last_version: {e}")
        
    def write_new_version(self, new_version):
        try:
            with open(self.path, "w") as f:
                f.write(new_version)
            self.version = new_version
        except Exception as e:
            print(f"Error in write_new_version: {e}")
    
    def read_commit_logs(self):
        try:
            with open(self.log_path, "r", encoding='utf-8') as json_file:
                if not json_file.read(1):
                    return []
                json_file.seek(0)
                return json.load(json_file)
        except FileNotFoundError:
            with open(self.log_path, "w") as f:
                json.dump([], f)
            return []
        except Exception as e:
            print(f"Error in read_commit_logs: {e}")
    
    def write_commit_logs(self, logs):
        try:
            with open(self.log_path, "w") as json_file:
                json.dump(logs, json_file, indent=4)
        except Exception as e:
            print(f"Error in write_commit_logs: {e}")