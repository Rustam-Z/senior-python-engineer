## Thread and process

| Thread                                                                                 | Process                   |
|----------------------------------------------------------------------------------------|---------------------------|
| A segment of process, sequence of instructions of process                              | A program in execution    |
| One process can spawn multiple threads but all of them will be sharing the same memory | Processes are isolated    |
| Lightweight                                                                            | Not lightweight           |
| Share data with each other, two threads can write to the same memory at the same time  | Do not share data/objects |

## Concurrency and parallelism

Concurrency = one core, done using context switching, simulation of parallelism 

Parallelism = many cores, literally at the same time

- More
    - Running multiple tasks concurrently, means that the processor performs context switching so that multiple tasks can be in-progress at the same time. Done in single CPU core. 
    - In **parallelism** multiple tasks (or even several components of one task) **can literally run at the same time** (e.g. on a multicore processor or on a machine with multiple CPUs). Therefore, it is not possible to have parallelism on machines with a single processor and single core
         
    - Combinations:
        - **Neither concurrent, nor parallel:** sequential execution.
        - **Concurrent, but not parallel**: tasks make progress *seemingly* at the same time, but in fact the system switches between various tasks that are concurrently in progress, until all of them are executed.
        - **Parallel, but not concurrent:** This is a fairly rare scenario where only one task is being executed at any given time, but the task itself is broken down into sub-tasks that are being processed in parallel. Every task though, must be completed before the next task is picked up and executed.
        - **Concurrent and parallel:** Application is able to work on multiple tasks concurrently but at the same time it also breaks down each individual task into sub-tasks so these sub-tasks can eventually be executed in parallel.

## Multiprocessing and multithreading

| Multiprocessing                                                                                                                      | Multithreading                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I/O bound                                                                                                                            | CPU bound                                                                                                                                                                                                         |
| CPUs are added for increasing computing power                                                                                        | Many threads are created of a single process for increasing computing power.                                                                                                                                      |
| Many processes are executed simultaneously                                                                                           | Many threads of a process are executed simultaneously.                                                                                                                                                            |
| Reliability: multiprocess applications are usually more reliable because the crash of a process does not affect the other processes. | If you need data shared among different execution entities. Message passing mechanisms are less fast and flexible than shared memory. Therefore, in some cases, it is better to use threads instead of processes. |
| multiprocessing or concurrent.futures.ProcessPoolExecutor                                                                            | threading or ThreadPoolExecutor                                                                                                                                                                                   |
- CPU-bound code will have no performance gain with Python multi-threading because of GIL.
- A **Python process cannot run threads in parallel, but it can run them concurrently through context switching during I/O bound operations.**
    - This limitation is actually enforced by GIL.
    - The **Python Global Interpreter Lock** (GIL) prevents threads within the same process to be executed at the same time.

## **GIL = Global Interpreter Lock**

- *“Only one thread can execute Python code at once”*
- GIL is a mutex solution for dealing with shared resources (memory), when two threads try to modify the same resource at the same time. Solution is a global lock on the interpreter when a thread is interacting with the shared resource. Python’s GIL accomplishes this by locking the entire interpreter, meaning that it’s not possible for another thread to step on the current one. When CPython handles memory, it uses the GIL to ensure that it does so safely.

## References

- [https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29](https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29)
- [https://realpython.com/python-gil/](https://realpython.com/python-gil/)