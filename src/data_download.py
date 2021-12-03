import requests

url = 'https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z'

local_filename =  'data/posts.7z'
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)