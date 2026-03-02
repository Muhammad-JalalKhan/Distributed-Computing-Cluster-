import time
from dask.distributed import Client, progress

def heavy_computation(data_chunk):
    """
    Simulates a heavy AI/Mathematical workload.
    """
    start = time.time()
    # Complex math to stress the CPU
    result = sum(i**2 for i in range(data_chunk))
    time.sleep(1) # Artificial delay to visualize the task stream
    return f"Processed {data_chunk} in {time.time() - start:.2f}s"

if __name__ == "__main__":
    # 1. Connect to your cluster
    # REPLACE this IP with the one from your Scheduler terminal (10.90.20.76)
    scheduler_address = 'tcp://10.90.20.76:8786'
    
    try:
        client = Client(scheduler_address)
        print(f"--- Connection Successful ---")
        print(f"Cluster details: {client}")
        
        # 2. Define the workload
        # We create 50 tasks to distribute
        tasks = [10**6] * 50 

        print(f"Launching 50 tasks across the Ryzen + i5 network...")
        
        # 3. Execute and Monitor
        start_time = time.time()
        futures = client.map(heavy_computation, tasks)
        
        # This will show a progress bar in your terminal
        progress(futures)
        
        # Gather results
        results = client.gather(futures)
        
        end_time = time.time()
        
        print(f"\n--- Project Results ---")
        print(f"Total Cluster Time: {end_time - start_time:.2f} seconds")
        print(f"First 5 results: {results[:5]}")
        
    except Exception as e:
        print(f"Error: Could not connect to the cluster. {e}")