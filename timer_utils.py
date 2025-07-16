import time
import functools


def measure_execution_time(func):
    """
    A decorator that measures the Wall time and CPU time of a method execution,
    simulating the output of %%time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wall_start = time.perf_counter()
        cpu_start = time.process_time()

        result = func(*args, **kwargs)

        wall_end = time.perf_counter()
        cpu_end = time.process_time()

        wall_time_taken = wall_end - wall_start
        cpu_time_taken = cpu_end - cpu_start

        print(f"\n--- Performance for '{func.__name__}' ---")
        print(f"CPU times: user {cpu_time_taken:.4f}s, sys: [Not directly captured by process_time in this granular way], total: {cpu_time_taken:.4f}s")
        print(f"Wall time: {wall_time_taken:.4f}s")
        print("--------------------------------------")

        return result
    return wrapper


def get_execution_time(func, *args, **kwargs):
    """
    Executes a method and returns its execution time.
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time