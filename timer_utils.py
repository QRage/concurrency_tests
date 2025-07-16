import time
import functools
import inspect
import os


def measure_execution_time(func):
    """
    A decorator that measures the Wall time and CPU time of a method execution,
    simulating the output of %%time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        caller_frame = inspect.stack()[1]
        wall_start = time.perf_counter()
        cpu_times_start = os.times()

        result = func(*args, **kwargs)

        wall_end = time.perf_counter()
        cpu_times_end = os.times()

        wall_time_taken = wall_end - wall_start
        user_time_taken = cpu_times_end.user - cpu_times_start.user
        system_time_taken = cpu_times_end.system - cpu_times_start.system
        total_cpu_time_taken = user_time_taken + system_time_taken

        print(f"\n--- Performance for '{func.__name__}' ---")
        print(f"CPU times: user {user_time_taken:.4f}s, sys: {system_time_taken:.4f}s, total: {total_cpu_time_taken:.4f}s")
        print(f"Wall time: {wall_time_taken:.4f}s")
        print("--------------------------------------")

        return result
    return wrapper
