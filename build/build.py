import configparser
import os

from PyHackMD import API


def get_hachmd_token(config_path: str = '.\\build\\config.ini') -> str:
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['hackmd']['token']


def get_md_paths(src_path: str = '.\\src') -> list:
    md_paths = [
        os.path.join(src_path, path)
        for path in os.listdir(src_path) if path.endswith('.md')
    ]
    return md_paths


def link_repo_imgs(
        md_path_ori: str,
        repo_url: str = 'https://github.com/WyattHo/hyperworks-notes/blob/main/',
        url_suf: str = '?raw=true') -> None:

    with open(md_path_ori, 'r') as f:
        conts_ori = f.readlines()

    conts_new = []
    for cont_ori in conts_ori:
        if '<img src' in cont_ori:
            cont_new = cont_ori.replace('../', repo_url)
            cont_new = cont_new.replace('.png', f'.png{url_suf}')
        else:
            cont_new = cont_ori
        conts_new.append(cont_new)

    md_path_new = md_path_ori.replace('src', 'build')
    with open(md_path_new, 'w') as f:
        f.writelines(conts_new)


def main() -> None:
    # api = API(get_hachmd_token())
    # data = api.get_note_list()

    md_paths = get_md_paths()
    list(map(link_repo_imgs, md_paths))  # Didn't work if no list()


if __name__ == '__main__':
    main()
