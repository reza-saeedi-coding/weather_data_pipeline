import json
import os
def save_to_json(data:list, file_path:str):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = []
    combined_data = existing_data + data

    with open(file_path, "w") as f:
        json.dump(combined_data, f, indent =4)
