from QuickStart_Rhy.NetTools.NormalDL import normal_dl
from QuickStart_Rhy import headers, qs_default_console, qs_info_string, qs_error_string
import requests
import re
import os

rt_url = 'https://folk.idi.ntnu.no/weifengl/'
url = rt_url + 'ticoh.html'

html = requests.get(url, headers=headers).text
pages = set(re.findall('<a.*?href="(.*?)".*?>', html, re.S))

def dfs(cur_dir: str):
    res = []
    ls = os.listdir(cur_dir) if cur_dir else os.listdir()
    if cur_dir:
        cur_dir += '/'
    for f in ls:
        if os.path.isfile(cur_dir + f):
            res.append(cur_dir + f)
        elif os.path.isdir(cur_dir + f):
            res += dfs(cur_dir + f)
    return res

done_ls = dfs('')

for page in pages:
    page = page.strip()
    if '#' in page:
        page = page.split('#')[0]
    if page.startswith('http') or page.startswith('bibtex.html') or page in done_ls:
        continue
    qs_default_console.print(qs_info_string, f'Start: {page}')
    normal_dl(rt_url + page, set_name=page)
    done_ls.append(page)

