"""
This script demonstrates the execution of an I/O-bound task using multithreading via
concurrent.futures.ThreadPoolExecutor. It loads the content of several Django
documentation pages in parallel using HTTP requests, which allows for a significant
reduction in overall execution time because threads do not block while waiting for a
response from the network.
The script tests performance with different numbers of threads (2, 4, 8, 16).
"""
from urllib import request
from concurrent.futures import ThreadPoolExecutor

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


def fetch_url_content(url):
    with request.urlopen(url) as src:
        content = src.read()
        return content


@measure_execution_time
def multi_thread_executor_map(num_workers):
    print(f"Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with {num_workers} workers...")
    all_results = []
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results_iterator = executor.map(fetch_url_content, urls)
        all_results = list(results_iterator)
    return all_results

if __name__ == "__main__":
    print("--- Running ThreadPoolExecutor.map tests ---")

    multi_thread_executor_map(2)
    multi_thread_executor_map(4)
    multi_thread_executor_map(8)
    multi_thread_executor_map(16)
