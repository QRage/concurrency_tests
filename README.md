📢There are many different repositories with similar tests.
As the author, I do not claim absolute accuracy, but I want to show an example and the difference.

📜This repository contains a series of benchmarks and examples designed to investigate and compare the performance of multiprocessing and multithreading in Python. The main goal is to clearly demonstrate the impact of the Global Interpreter Lock (GIL) on CPU-intensive tasks and the efficiency of both approaches for I/O-intensive operations.

🚀 Project Goal
Performance Assessment: Measure execution time and resource usage for tasks implemented using threads and processes.

GIL Demonstration: Show how the GIL limits true parallelism of multi-threaded CPU-intensive tasks in Python.

Choosing the Optimal Strategy: Provide practical recommendations for choosing the appropriate concurrency model depending on the nature of the task (CPU-bound or I/O-bound).

# Test results:

### 1 Single thread, single process:
1_single_thread_single_process.py  
___
Performance for 'single_thread_single_process'  
CPU times: user 0.0469s,  
sys: 0.0156s,  
total: 0.0625s  
Wall time: 0.7127s
### 2 Multithreading:
2_multithreading.py  
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 2 workers...  
CPU times: user 0.0938s,  
sys: 0.0000s,  
total: 0.0938s  
Wall time: 0.6045s  
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 4 workers...  
CPU times: user 0.0312s,  
sys: 0.0000s,  
total: 0.0312s  
Wall time: 0.2777s
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 8 workers...  
CPU times: user 0.0312s,  
sys: 0.0000s,  
total: 0.0312s  
Wall time: 0.1941s
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 16 workers...  
CPU times: user 0.0625s,  
sys: 0.0000s,  
total: 0.0625s  
Wall time: 0.1117s
