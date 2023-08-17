#!/usr/bin/env python3
"""IImplementing an expiring web cache and tracker"""


import requests
import time
from functools import wraps

cache = {}

def get_page(url: str) -> str:
    cache_key = f"count:{url}"
    if cache_key in cache:
        if time.time() - cache[cache_key]['time'] < 10:
            return cache[cache_key]['content']
        else:
            del cache[cache_key]

    response = requests.get(url)
    content = response.content.decode('utf-8')

    cache[cache_key] = {
        'time': time.time(),
        'content': content
    }

    return content

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
