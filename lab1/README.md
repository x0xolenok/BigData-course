# MapReduce
1. The task is implemented using the ‘standard method’ and MapReduce 
2. Multithreading is really present
3. MapReduce is faster than the ‘standard implementation’. The ‘competition’ should be fair 
4. The results of the MapReduce implementation are analysed and conclusions are drawn 

# Results:
![image](https://github.com/user-attachments/assets/2b77e720-1b01-43f0-8372-de4d9a99a90d)

```bash
Array size: 100 - statistics.mean result: 62014893.5500, Time: 0.0000000000 seconds
Array size: 100 - Standard method result: 62014893.5500, Time: 0.0000000000 seconds
Array size: 500 - statistics.mean result: -9308588.8700, Time: 0.0000000000 seconds
Array size: 500 - Standard method result: -9308588.8700, Time: 0.0000000000 seconds
Array size: 1000 - statistics.mean result: 16384742.8900, Time: 0.0000000000 seconds
Array size: 1000 - Standard method result: 16384742.8900, Time: 0.0000000000 seconds
Array size: 5000 - statistics.mean result: 16388858.8200, Time: 0.0010004044 seconds
Array size: 5000 - Standard method result: 16388858.8200, Time: 0.0000000000 seconds
Array size: 10000 - statistics.mean result: 4430599.1590, Time: 0.0020000935 seconds
Array size: 10000 - Standard method result: 4430599.1590, Time: 0.0000000000 seconds
Array size: 50000 - statistics.mean result: -5907017.7372, Time: 0.0109977722 seconds
Array size: 50000 - Standard method result: -5907017.7372, Time: 0.0010006428 seconds
Array size: 100 - MapReduce (Processes: 2) result: -60307705.8300, Time: 1.0729975700 seconds
Array size: 500 - MapReduce (Processes: 2) result: -26294973.2960, Time: 1.3400113583 seconds
Array size: 1000 - MapReduce (Processes: 2) result: 14300499.0280, Time: 1.1610081196 seconds
Array size: 5000 - MapReduce (Processes: 2) result: 558879.2548, Time: 1.0570032597 seconds
Array size: 10000 - MapReduce (Processes: 2) result: -7545471.9881, Time: 0.9870076180 seconds
Array size: 50000 - MapReduce (Processes: 2) result: 102571.3489, Time: 1.2034027576 seconds
Array size: 100 - MapReduce (Processes: 4) result: -13403105.5900, Time: 1.2199902534 seconds
Array size: 500 - MapReduce (Processes: 4) result: 21378645.6460, Time: 0.9919996262 seconds
Array size: 1000 - MapReduce (Processes: 4) result: -2542571.1200, Time: 0.9739999771 seconds
Array size: 5000 - MapReduce (Processes: 4) result: 10272282.8552, Time: 1.0160074234 seconds
Array size: 10000 - MapReduce (Processes: 4) result: 1804668.8887, Time: 1.0570001602 seconds
Array size: 50000 - MapReduce (Processes: 4) result: 965389.7142, Time: 1.0300030708 seconds
Array size: 100 - MapReduce (Processes: 8) result: 2430557.9167, Time: 1.6075625420 seconds
Array size: 500 - MapReduce (Processes: 8) result: 35135720.9892, Time: 1.3210110664 seconds
Array size: 1000 - MapReduce (Processes: 8) result: 6536401.8740, Time: 1.3029863834 seconds
Array size: 5000 - MapReduce (Processes: 8) result: 10858471.3332, Time: 1.2825548649 seconds
Array size: 10000 - MapReduce (Processes: 8) result: 5077618.8868, Time: 1.2880024910 seconds
Array size: 50000 - MapReduce (Processes: 8) result: -1582015.9653, Time: 1.2840023041 seconds
```
