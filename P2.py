import sys
import timeit

# Create a tuple and a list
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Check memory size
print("Size of tuple:", sys.getsizeof(numbers_tuple), "bytes")
print("Size of list:", sys.getsizeof(numbers_list), "bytes")

# Measure creation time
tuple_time = timeit.timeit(
    stmt="(1,2,3,4,5,6,7,8,9,10)",
    number=1000000
)

list_time = timeit.timeit(
    stmt="[1,2,3,4,5,6,7,8,9,10]",
    number=1000000
)

# Display creation time
print("Creation time for tuple (in seconds):", tuple_time)
print("Creation time for list (in seconds):", list_time)