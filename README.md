# Performance analysis of Python Flask in Docker

## Impact of core allocation on the performance

### Senario: Simple Echo Service (echos the response back to the client)
### (Number of Gunicorn workers 8)


| CPU | Memory  | Concurrency  | Think Time (exponential) | Average Latency (ms) | Standard Deviation | TPS (requests/second) | Error % |
|-----|---------|--------------|--------------------------|----------------------|--------------------|-----------------------|---------|
| 0.2 | 10GB    | 500          | 1000                     | 1263                 | 2042               | 168                   | 1.64    |
| 0.5 | 10GB    | 500          | 1000                     | 96                   | 213                | 358                   | 1.28    |
| 1   | 10GB    | 500          | 1000                     | 36                   | 168                | 372                   | 0.85    |
| 2   | 10GB    | 500          | 1000                     | 29                   | 116                | 376.6                 | 0.77    |
|     |         |              |                          |                      |                    |                       |         |
| 0.2 | 1GB     | 500          | 1000                     | 1341                 | 2649               | 187                   | 0.41    |
| 0.5 | 1GB     | 500          | 1000                     | 74                   | 155                | 362                   | 0.54    |
| 1   | 1GB     | 500          | 1000                     | 60                   | 229                | 367                   | 1.03    |
| 2   | 1GB     | 500          | 1000                     | 40                   | 162                | 373                   | 0.52    |

### Observations

* There is a significant performance degradation when you decrease the number of cores below 0.5 

* When we set the memory allocation to 75 MB, we notice no signficant difference in the behaviour. However, when we set memory to 50 M the container got killed due to insufficient memory. 
 
 ### Memory profile
 
 ```
 # install the required packages
pip3 install memory_profiler
pip3 install matplotlib
# run the profiler to record the memory usage
# sample 0.1s by defaut
mprof run --include-children python apps.py
# plot the recorded memory usage
mprof plot --output memory-profile.png

 ```


![Echo service memory](/memory-profile.png)




