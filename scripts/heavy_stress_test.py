import time
import numpy as np
from dask.distributed import Client, progress

def heavy_math_work(n):
    """
    This function performs a combination of matrix operations 
    and prime searching to stress the CPU and RAM.
    """
    start_time = time.time()
    
    # 1. CPU Stress: Find primes in a large range
    primes = []
    for num in range(n, n + 5000):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
            
    # 2. RAM & CPU Stress: Large Matrix Multiplication
    # Creating a 1000x1000 matrix
    matrix_a = np.random.rand(1000, 1000)
    matrix_b = np.random.rand(1000, 1000)
    result = np.dot(matrix_a, matrix_b)
    
    end_time = time.time()
    return f"Task starting at {n} finished in {end_time - start_time:.2f}s"

if __name__ == "__main__":
    # Connect to your scheduler - Use your Ryzen's IP
    # As per your logs, it's 10.90.20.76
    client = Client('tcp://10.90.20.76:8786')
    print("--- CLUSTER STRESS TEST STARTING ---")
    print(f"Workers Detected: {len(client.scheduler_info()['workers'])}")

    # We will launch 100 heavy tasks. 
    # This will saturate the Ryzen and the i5 for several minutes.
    task_inputs = [i * 10000 for i in range(100)]

    start_total = time.time()
    
    # Map the tasks to the cluster
    futures = client.map(heavy_math_work, task_inputs)
    
    # Track progress in the terminal
    progress(futures)
    
    # Gather results
    results = client.gather(futures)
    
    end_total = time.time()
    
    print(f"\n--- STRESS TEST COMPLETE ---")
    print(f"Total Cluster Time: {end_total - start_total:.2f} seconds")
    print(f"Total Tasks Processed: {len(results)}")