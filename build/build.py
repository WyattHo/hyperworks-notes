import configparser
from PyHackMD import API


def get_hachmd_token() -> str:
    CONFIG_PATH = '.\\build\\config.ini'
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config['hackmd']['token']


api = API(get_hachmd_token())
data = api.get_note_list()
