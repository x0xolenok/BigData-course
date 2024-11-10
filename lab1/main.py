import random
import time
import multiprocessing
import statistics
import matplotlib.pyplot as plt


# Function to generate random array
def generate_random_array(size):
    return [random.randint(-1000000000, 1000000000) for _ in range(size)]


# Function for standard average calculation
def calculate_average_standard(arr):
    return sum(arr) / len(arr)


# MapReduce function for average calculation
def map_reduce(arr_chunk):
    return sum(arr_chunk) / len(arr_chunk)


def calculate_average_mapreduce(arr, num_processes):
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(map_reduce, chunks)

    return sum(results) / len(results), time.time()


# Function to compare average calculation methods
def plot_comparison(array_sizes, num_processes_list):
    plt.figure(figsize=(14, 8))

    mean_times = []
    standard_times = []

    # Limiting the maximum array size for visualization
    max_array_size = 1000000  # Change this limit as needed

    for size in array_sizes:
        if size > max_array_size:
            size = max_array_size

        arr = generate_random_array(size)

        # Time for statistics.mean
        start_time = time.time()
        mean_result = statistics.mean(arr)
        end_time = time.time()
        mean_times.append(end_time - start_time)
        print(
            f"Array size: {size} - statistics.mean result: {mean_result:.4f}, Time: {end_time - start_time:.10f} seconds")

        # Time for standard method
        start_time = time.time()
        standard_result = calculate_average_standard(arr)
        end_time = time.time()
        standard_times.append(end_time - start_time)
        print(
            f"Array size: {size} - Standard method result: {standard_result:.4f}, Time: {end_time - start_time:.10f} seconds")

    # Plotting the statistics.mean and standard method times
    plt.plot(array_sizes, mean_times, label='statistics.mean (single thread)', linestyle='--', color='black')
    plt.plot(array_sizes, standard_times, label='Standard method (single thread)', linestyle='--', color='gray')

    # Plotting the MapReduce method times for each number of processes
    for num_processes in num_processes_list:
        mapreduce_times = []

        for size in array_sizes:
            if size > max_array_size:
                size = max_array_size

            arr = generate_random_array(size)

            start_time = time.time()
            mapreduce_result, processing_time = calculate_average_mapreduce(arr, num_processes)
            end_time = time.time()
            mapreduce_times.append(end_time - start_time)
            print(
                f"Array size: {size} - MapReduce (Processes: {num_processes}) result: {mapreduce_result:.4f}, Time: {end_time - start_time:.10f} seconds")

        plt.plot(array_sizes, mapreduce_times, label=f'MapReduce (Processes: {num_processes})')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Average Calculation Methods')
    plt.legend()
    plt.grid(True)
    plt.show()


# Main execution
if __name__ == "__main__":
    # Input the array size and number of processes for MapReduce
    array_sizes = [100, 500, 1000, 5000, 10000, 50000]  # Modify as needed
    num_processes_list = [2, 4, 8]  # Modify with the number of processes you want to test

    plot_comparison(array_sizes, num_processes_list)
