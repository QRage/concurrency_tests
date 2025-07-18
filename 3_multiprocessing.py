"""
This script demonstrates the same I/O-bound task, but using a multiprocessing approach (multiprocessing.Pool).
It creates separate processes for each HTTP request, and performs parallel page loading. This approach
is less efficient for network (I/O-bound) tasks due to the overhead of creating processes and
transferring data between them.
The script also measures performance with 2, 4, 8, and 16 processes.
"""
from urllib import request
from multiprocessing import Pool, cpu_count

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
    'https://docs.djangoproject.com/en/5.0/ref/forms/api/',
]


def fetch_url_content(url):
    with request.urlopen(url) as src:
        return src.read()


@measure_execution_time
def multi_process_pool_map(num_workers):
    print(f"Starting multi-processing (Pool.map) URL fetching with {num_workers} workers...")
    with Pool(processes=num_workers) as pool:
        results = pool.map(fetch_url_content, urls)
    return results


if __name__ == "__main__":
    print("--- Running multiprocessing Pool.map tests ---")

    multi_process_pool_map(2)
    multi_process_pool_map(4)
    multi_process_pool_map(cpu_count())     # 8 in my case of using i7-7700k
    multi_process_pool_map(16)
