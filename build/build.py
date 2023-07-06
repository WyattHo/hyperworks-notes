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
        lines_ori = f.readlines()

    lines_mod = []
    for line_ori in lines_ori:
        if '<img src' in line_ori:
            line_mod = line_ori.replace('../', repo_url)
            line_mod = line_mod.replace('.png', f'.png{url_suf}')
            lines_mod.append(line_mod)
        else:
            lines_mod.append(line_ori)
    
    title = os.path.basename(md_path_ori).capitalize().rstrip('.md')
    content = ''.join(lines_mod)
    return {title: content}


def main() -> None:
    md_paths = get_md_paths()
    for path in md_paths:
        md_content = link_repo_imgs(path)

    # api = API(get_hachmd_token())
    # notes = api.get_note_list()


if __name__ == '__main__':
    main()
