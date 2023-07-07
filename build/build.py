import configparser
import os
from typing import List

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

    title = lines_ori[0].lstrip('# ').rstrip('\n')
    content = ''.join(lines_mod)
    return {title: content}


def create_or_update_hackmd(api: API, notes: List[dict], md_content: dict):
    existed = False
    title, content = list(md_content.items())[0]
    for note in notes:
        if note['title'] == title:
            existed = True
            note_id = note['id']
            break

    if existed:
        api.update_note(
            note_id=note_id,
            content=content
        )
    else:
        api.create_note(
            title=title,
            content=content,
            read_permission='guest',
            write_permission='owner'
        )


def main() -> None:
    api = API(get_hachmd_token())
    notes = api.get_note_list()

    md_paths = get_md_paths()
    for path in md_paths:
        md_content = link_repo_imgs(path)
        create_or_update_hackmd(api, notes, md_content)


if __name__ == '__main__':
    main()
