"""
This script demonstrates sequential, single-threaded, and single-process execution of an I/O-bound task.
It fetches content from a predefined list of Django documentation URLs one by one,
using Python's standard urllib.request module.
"""
from urllib import request

from timer_utils import measure_execution_time


urls = [
    'https://docs.djangoproject.com/en/5.0/intro/tutorial01/',
    'https://docs.djangoproject.com/en/5.0/intro/tutorial02/',
    'https://docs.djangoproject.com/en/5.0/intro/tutorial03/',
    'https://docs.djangoproject.com/en/5.0/intro/tutorial04/',
    'https://docs.djangoproject.com/en/5.0/intro/tutorial05/',
    'https://docs.djangoproject.com/en/5.0/intro/tutorial06/',
    'https://docs.djangoproject.com/en/5.0/intro/tutorial07/',
    'https://docs.djangoproject.com/en/5.0/topics/db/models/',
    'https://docs.djangoproject.com/en/5.0/topics/http/urls/',
    'https://docs.djangoproject.com/en/5.0/ref/forms/api/'
]


@measure_execution_time
def single_thread_single_process():
    result = []
    for url in urls:
        print(url)
        with request.urlopen(url) as src:
            result.append(src)


if __name__ == "__main__":
    single_thread_single_process()
