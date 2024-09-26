from median_of_medians import median_of_medians
from randomized_select import randomized_select
import time
import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Test arrays of different sizes
    input_sizes = [100, 500 ,1000, 2500, 5000, 10000]

    for size in input_sizes:
        arr = random.sample(range(1, size + 1), size)
        k = size // 2  # Find the median

        start = time.time()
        deterministic_result = median_of_medians(arr, k)
        deterministic_time = time.time() - start

        start = time.time()
        randomized_result = randomized_select(arr, k)
        randomized_time = time.time() - start

        print(f"Array size: {size}, Deterministic time: {deterministic_time:.6f}, Randomized time: {randomized_time:.6f}")