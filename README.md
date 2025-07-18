📢There are many different repositories with similar tests.
As the author, I do not claim absolute accuracy, but I want to show an example and the difference.

📜Testing was performed on an Intel i7-7700k (4 cores, 8 threads).
Goal: compare the performance of three approaches to handling an I/O-bound task — loading several pages from the official Django documentation.

## Test results:

### 1 Single thread, single process:
1_single_thread_single_process.py  
___
Performance for 'single_thread_single_process'  
CPU times:  
user 0.0469s,  
sys: 0.0156s,  
total: 0.0625s  
Wall time: 0.7127s
### 2 Multithreading:
2_multithreading.py  
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 2 workers...  
CPU times:  
user 0.0938s,  
sys: 0.0000s,  
total: 0.0938s  
Wall time: 0.6045s  
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 4 workers...  
CPU times:  
user 0.0312s,  
sys: 0.0000s,  
total: 0.0312s  
Wall time: 0.2777s
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 8 workers...  
CPU times:  
user 0.0312s,  
sys: 0.0000s,  
total: 0.0312s  
Wall time: 0.1941s
___
Starting multi-threaded (ThreadPoolExecutor.map) URL fetching with 16 workers...  
CPU times:  
user 0.0625s,  
sys: 0.0000s,  
total: 0.0625s  
Wall time: 0.1117s

### 3 Muptiprocessing
3_multiprocessoring.py
___
Starting multi-processing (Pool.map) URL fetching with 2 workers...  
CPU times:  
user 0.0000s,  
sys: 0.0156s,  
total: 0.0156s  
Wall time: 0.7640s

Starting multi-processing (Pool.map) URL fetching with 4 workers...  
CPU times:  
user 0.0000s,  
sys: 0.0000s,  
total: 0.0000s  
Wall time: 0.4401s

Starting multi-processing (Pool.map) URL fetching with 8 workers...  
CPU times: user 0.0000s,  
sys: 0.0156s,  
total: 0.0156s  
Wall time: 0.4328s

Starting multi-processing (Pool.map) URL fetching with 16 workers...  
CPU times:  
user 0.0000s, sys: 0.0000s, total: 0.0000s
Wall time: 0.5298s

## Conclusion
1. Single thread, single process
Fully sequential execution.

Wall time: ~0.71s

Good for simple scripts, but does not scale.
___
2. Multithreading (ThreadPoolExecutor)
Number of threads Wall time (sec):  

| Threads | Wall time |
| --- | --- |
| 2 | 0.60 |
| 4 | 0.28 |
| 8 | 0.19 |
| 16 | 0.11 |


The most efficient approach for I/O-bound tasks.  
Threads are not blocked by the GIL while waiting for a response from the network.  
Easy to implement, low overhead, good scalability.  
With 16 threads, we got the lowest execution time.  
___
3. Multiprocessing (multiprocessing.Pool)
Number of processes Wall time (sec)  

| Processes | Wall time |
| --- | --- |
| 2 | 0.76 |
| 4 | 0.44 |
| 8 | 0.43 |
| 16 | 0.53 (worse) |

Using separate processes did not yield any performance gains.  

Multiprocessing is inefficient for I/O-bound tasks due to overhead (process creation, serialization, interprocess transfer).  

Execution time deteriorates with an excess number of processes due to competition for network resources.
___
—Why didn't we use concurrent.futures.ProcessPoolExecutor and chose multiprocessing.Pool?  
—multiprocessing.Pool is more low-level, tested, reliable.  
If you mix concurrent.futures.ThreadPoolExecutor and ProcessPoolExecutor, the API looks the same, but under the hood there are very different mechanisms:  
* ThreadPoolExecutor runs in a single process.  
* ProcessPoolExecutor uses full multiprocessing.Process, with all the overhead.
The test with multiprocessing. Pool is more transparent for demonstrating the process mechanism, because Pool.map is clearly associated with the fork model.

## Overall conclusion  
* I/O-bound tasks scale best with ThreadPoolExecutor.  
* Multiprocessing should only be used for CPU-bound workloads.  
* Sequential execution is the slowest, but suitable for simple cases.  
* More than 8 threads/processes on this volume of tasks do not provide a significant advantage, and may even harm.
