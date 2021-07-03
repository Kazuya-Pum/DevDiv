import json
import requests
import time
import os
import shutil
import re
from dotenv import load_dotenv
import asyncio
import itertools

from .astword.js import processor as js
from .astword.py import processor as py
from .astword.java import processor as java

load_dotenv(verbose=True)
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
access_token = os.environ.get('TOKEN')
headers = {'Authorization': f'token {access_token}'} if access_token != None else None


class Repository():
    def __init__(self, owner, repo, extension):
        self.owner = owner
        self.repo = repo
        self.extension = extension
        self.raw_words = get_repo_words(owner, repo, extension)
        self.words = separate_words(self.raw_words)


def get_sha(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}'
    res = requests.get(url, headers=headers)
    if res.ok == False:
        return None
    
    repo_info = res.json()
    default_branch = repo_info['default_branch']

    url = f'https://api.github.com/repos/{owner}/{repo}/branches/{default_branch}'
    res = requests.get(url, headers=headers)
    if res.ok == False:
        return None

    branch_info = res.json()
    return branch_info['commit']['sha']


def get_download_urls(owner, repo, path = ''):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    res = requests.get(url, headers=headers)
    if res.ok == False:
        return None
    
    items = res.json()
    download_list = {}
    for item in items:
        if item['type'] == 'dir':
            download_list.update(get_download_urls(owner, repo, item['path']))
        elif item['type'] == 'file':
            download_list[item['path'].replace('/', '_')] = item['download_url']
    
    return download_list


def separate_words(words):
    p = re.compile(r'(?<=[a-z])(?=[A-Z])|_|[0-9]|(?<=[A-Z])(?=[A-Z][a-z])')

    res = []
    for word in words:
        res.extend([w.lower() for w in p.split(word) if len(w) > 0])

    return res


async def get_file_words(path, url, extension, save_path):
    if path.endswith(extension) != True:
        return []

    loop = asyncio.get_event_loop()

    res = await loop.run_in_executor(None, lambda:requests.get(url, headers=headers))

    if res.ok == False:
        return []
    
    filepath = os.path.join(save_path, path)

    try:
        with open(filepath, 'wb') as f:
            f.write(res.content)
        if extension == '.js':
            return await loop.run_in_executor(None, js.get_words, filepath)
        elif extension == '.py':
            return await loop.run_in_executor(None, py.get_words, filepath)
        elif extension == '.java':
            return await loop.run_in_executor(None, java.get_words, filepath)
        else:
            raise Exception('Unknown extension')
    
    except Exception as e:
        print(e)
    finally:
        os.remove(filepath)
        pass


def get_repo_words(owner, repo, extension):
    save_path = os.path.join(os.path.dirname(__file__), 'repos', f'{owner}_{repo}')
    words = []

    try:
        os.makedirs(save_path, exist_ok=True)
        urls = get_download_urls(owner, repo)

        loop = asyncio.get_event_loop()
        tasks = asyncio.gather(*[get_file_words(path, url, extension, save_path) for path, url in urls.items()])

        words = loop.run_until_complete(tasks)

        return list(itertools.chain.from_iterable(words))

    finally:
        shutil.rmtree(save_path)
        pass

