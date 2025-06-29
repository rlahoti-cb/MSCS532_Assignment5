import random
import time

# call quicksort on an input array with a default strategy of random
# strategy options are "random", "middle"
def quicksort_wrapper(i, strategy="random"):
    if not isinstance(i, list):
        return None
    if len(i) <= 1:
        return i.copy()
    
    ic = i.copy()
    quicksort(ic, 0, len(ic) - 1, strategy)
    return ic

def quicksort(i, l, h, strategy):
    while l < h:
        # if strategy is random, we choose a random pivot
        if strategy == "random":
            pivot_idx = random_partition(i, l, h)
        # if strategy is middle, we choose the middle element as the pivot
        elif strategy == "middle":
            pivot_idx = middle_element_partition(i, l, h)
        # otherwise unexpected strategy supplied and we raise error
        else:
            raise RuntimeError("Invalid pivot strategy chosen")

        
        if pivot_idx - l < h - pivot_idx:
            quicksort(i, l, pivot_idx - 1, strategy)
            l = pivot_idx + 1
        else:
            quicksort(i, pivot_idx + 1, h, strategy)
            h = pivot_idx - 1

# random element pivot approach 
def random_partition(i, l, h):
    pivot_idx = random.randint(l, h)
    i[pivot_idx], i[h] = i[h], i[pivot_idx]
    return partition(i, l, h)

# middle element pivot approach
def middle_element_partition(i, l, h):
    midpoint = l + (h - l) // 2
    i[midpoint], i[h] = i[h], i[midpoint]
    return partition(i, l, h)

def partition(i, l, h):
    pivot = i[h]
    x = l - 1
    for y in range(l, h):
        if i[y] <= pivot:
            x = x + 1
            i[x], i[y] = i[y], i[x]
    i[x + 1], i[h] = i[h], i[x + 1]
    return x + 1

# generate random data based
def generate_random_data(size):
    out = [random.randint(0, size) for x in range(size)]
    return out

# generate sorted data based
def generate_sorted_data(size):
    out = list(range(size))
    return out

# generate reversed sorted data
def generate_reversed_sorted_data(size):
    out = list(range(size, 0, -1))
    return out

# generate random
def generate_repeated_data(size):
    num_replace = size // 2
    data = generate_sorted_data(size)
    random_value = data[random.randint(0, size - 1)]
    data[-num_replace:] = [random_value] * num_replace
    random.shuffle(data)
    return data

# executes the code to run quicksort (pivot = middle element) and randomized quicksort
# on varying input data sizes (1000, 10000, 100000) on varying input data distributions
# such as random data, sorted data, reversed sorted data, and repeated data
# output for each sorting call is calculated and reported to the terminal
def experiment():
    for data_size in (1000, 10000, 100000):
        print(">>>> Testing input data size of " + str(data_size) + " elements")
        random_data = generate_random_data(data_size)
        sorted_data = generate_sorted_data(data_size)
        reversed_sorted_data = generate_reversed_sorted_data(data_size)
        repeated_data = generate_repeated_data(data_size)

        # randomized quicksort on random data
        start_time = time.time()
        quicksort_wrapper(random_data, strategy="random")
        end_time = time.time()
        print(">>>Randomized Pivot Quicksort on Random Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        # randomized quicksort on sorted data
        start_time = time.time()
        quicksort_wrapper(sorted_data, strategy="random")
        end_time = time.time()
        print(">>>Randomized Pivot Quicksort on Sorted Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        # randomized quicksort on reversed sorted data
        start_time = time.time()
        quicksort_wrapper(reversed_sorted_data, strategy="random")
        end_time = time.time()
        print(">>>Randomized Pivot Quicksort on Reversed Sorted Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        # randomized quicksort on repeated random data
        start_time = time.time()
        quicksort_wrapper(repeated_data, strategy="random")
        end_time = time.time()
        print(">>>Randomized Pivot Quicksort on Repeated Random Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        # quicksort on random data choosing middle element as pivot
        start_time = time.time()
        quicksort_wrapper(random_data, strategy="middle")
        end_time = time.time()
        print(">>>Middle Element Pivot Quicksort on Random Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        # quicksort on sorted data choosing middle element as pivot
        start_time = time.time()
        quicksort_wrapper(sorted_data, strategy="middle")
        end_time = time.time()
        print(">>>Middle Element Pivot Quicksort on Sorted Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        # quicksort on reversed sorted data choosing middle element as pivot
        start_time = time.time()
        quicksort_wrapper(reversed_sorted_data, strategy="middle")
        end_time = time.time()
        print(">>>Middle Element Pivot Quicksort on Reversed Sorted Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        # quicksort on repeated random data choosing middle element as pivot
        start_time = time.time()
        quicksort_wrapper(repeated_data, strategy="middle")
        end_time = time.time()
        print(">>>Middle Element Pivot Quicksort on Repeated Random Data")
        print("took " + str(end_time - start_time) + " seconds\n")

        print("\n\n")

if __name__ == "__main__":
    experiment()
