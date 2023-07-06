import configparser
import os

from PyHackMD import API


def get_hachmd_token() -> str:
    CONFIG_PATH = '.\\build\\config.ini'
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config['hackmd']['token']


def get_md_names() -> list:
    SRC_PATH = '.\\src'
    MD_EXT = 'md'
    md_names = [
        os.path.join(SRC_PATH, path)
        for path in os.listdir(SRC_PATH) if path.endswith(f'.{MD_EXT}')
    ]
    return md_names


def main() -> None:
    # api = API(get_hachmd_token())
    # data = api.get_note_list()

    md_names = get_md_names()


if __name__ == '__main__':
    main()
