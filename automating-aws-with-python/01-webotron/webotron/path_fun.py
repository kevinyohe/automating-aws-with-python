# coding: utf-8
from pathlib import Path
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'webotron/')
get_ipython().run_line_magic('ls', '')
pathname = "site"
path = Path(pathname)
path
path.resove()
path.resolve()
path.iterdir()
list(path.iterdir())
path.is_dir()
path.is_file()
def handle_directory(targert):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p)
        
handle_directory("site")
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p)
        
handle_directory("site")
handle_directory(path)
path.relative_to(root)
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p)
        
get_ipython().run_line_magic('SAVE', '')
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'path_fun.py')
get_ipython().run_line_magic('pinfo', '%save')
get_ipython().run_line_magic('save', 'path_fun.py')
