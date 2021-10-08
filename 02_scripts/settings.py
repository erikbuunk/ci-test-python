import os
import json


"""Load Config File"""
cur_dir = os.path.dirname(os.path.realpath(__file__))
print(cur_dir)
with open(os.path.join(cur_dir, "config.json")) as config_file:
    config = json.load(config_file)
