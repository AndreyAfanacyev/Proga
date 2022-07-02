import re
import sys
import requests
from urllib.request import urlopen
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader


def url_hook(some_str):
    if not some_str.startswith(("http", "https")):
        raise ImportError
    # переделано на requests:
    # with urlopen(some_str) as page:
    #     data = page.read().decode("utf-8")
    resp = requests.get(some_str) # запрос к серверу
    data = resp.text # ответ сервера (список py-файлов - модулей)
    filenames = re.findall("[a-zA-Z_][a-zA-Z0-0_]*.py", data)
    modnames = {name[:-3] for name in filenames}
    return URLFinder(some_str, modnames)

sys.path_hooks.append(url_hook)


class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available
        
    def find_spec(self, name, target=None):
        if name in self.available:
            origin = "{}/{}.py".format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)
        
        else:
            return None


class URLLoader:
    def create_module(self, target):
        return None
    
    def exec_module(self, module):
        # with urlopen() as page:
        #    source = page.read()
        resp = requests.get(module.__spec__.origin)
        source = resp.text
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)
